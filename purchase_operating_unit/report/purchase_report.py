# Copyright 2019 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0).



from odoo import api, fields, models, tools


class PurchaseReport(models.Model):

    _inherit = "purchase.report"

    operating_unit_id = fields.Many2one('operating.unit', 'Operating Unit')

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'purchase_report')
        self._cr.execute("""
                create view purchase_report as (
                    WITH currency_rate as (%s)
                    select
                        min(l.id) as id,
                        s.date_order as date_order,
                        s.state,
                        s.operating_unit_id,
                        s.date_approve,
                        s.dest_address_id,
                        spt.warehouse_id as picking_type_id,
                        s.partner_id as partner_id,
                        s.create_uid as user_id,
                        s.company_id as company_id,
                        s.fiscal_position_id as fiscal_position_id,
                        l.product_id,
                        p.product_tmpl_id,
                        t.categ_id as category_id,
                        s.currency_id,
                        t.uom_id as product_uom,
                        sum(l.product_qty/u.factor*u2.factor) as unit_quantity,
                        extract(epoch from age(s.date_approve,s.date_order))/(24*60*60)::decimal(16,2) as delay,
                        extract(epoch from age(l.date_planned,s.date_order))/(24*60*60)::decimal(16,2) as delay_pass,
                        count(*) as nbr_lines,
                        sum(l.price_unit / COALESCE(NULLIF(cr.rate, 0), 1.0) * l.product_qty)::decimal(16,2) as price_total,
                        avg(100.0 * (l.price_unit / COALESCE(NULLIF(cr.rate, 0),1.0) * l.product_qty) / NULLIF(ip.value_float*l.product_qty/u.factor*u2.factor, 0.0))::decimal(16,2) as negociation,
                        sum(ip.value_float*l.product_qty/u.factor*u2.factor)::decimal(16,2) as price_standard,
                        (sum(l.product_qty * l.price_unit / COALESCE(NULLIF(cr.rate, 0), 1.0))/NULLIF(sum(l.product_qty/u.factor*u2.factor),0.0))::decimal(16,2) as price_average,
                        partner.country_id as country_id,
                        partner.commercial_partner_id as commercial_partner_id,
                        analytic_account.id as account_analytic_id,
                        sum(p.weight * l.product_qty/u.factor*u2.factor) as weight,
                        sum(p.volume * l.product_qty/u.factor*u2.factor) as volume
                    from purchase_order_line l
                        join purchase_order s on (l.order_id=s.id)
                        join res_partner partner on s.partner_id = partner.id
                            left join product_product p on (l.product_id=p.id)
                                left join product_template t on (p.product_tmpl_id=t.id)
                                LEFT JOIN ir_property ip ON (ip.name='standard_price' AND ip.res_id=CONCAT('product.product,',p.id) AND ip.company_id=s.company_id)
                        left join product_uom u on (u.id=l.product_uom)
                        left join product_uom u2 on (u2.id=t.uom_id)
                        left join stock_picking_type spt on (spt.id=s.picking_type_id)
                        left join account_analytic_account analytic_account on (l.account_analytic_id = analytic_account.id)
                        left join currency_rate cr on (cr.currency_id = s.currency_id and
                            cr.company_id = s.company_id and
                            cr.date_start <= coalesce(s.date_order, now()) and
                            (cr.date_end is null or cr.date_end > coalesce(s.date_order, now())))
                    group by
                        s.company_id,
                        s.create_uid,
                        s.partner_id,
                        s.operating_unit_id,
                        u.factor,
                        s.currency_id,
                        l.price_unit,
                        s.date_approve,
                        l.date_planned,
                        l.product_uom,
                        s.dest_address_id,
                        s.fiscal_position_id,
                        l.product_id,
                        p.product_tmpl_id,
                        t.categ_id,
                        s.date_order,
                        s.state,
                        spt.warehouse_id,
                        u.uom_type,
                        u.category_id,
                        t.uom_id,
                        u.id,
                        u2.factor,
                        partner.country_id,
                        partner.commercial_partner_id,
                        analytic_account.id
                )
            """ % self.env['res.currency']._select_companies_rates())

    # def _select(self):
    #     select_str = super(PurchaseReport, self)._select()
    #     select_str += """
    #         ,s.operating_unit_id
    #     """
    #     return select_str
    #
    # def _group_by(self):
    #     group_by_str = super(PurchaseReport, self)._group_by()
    #     group_by_str += """
    #         ,s.operating_unit_id
    #     """
    #     return group_by_str
