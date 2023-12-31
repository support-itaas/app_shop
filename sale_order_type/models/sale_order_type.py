# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrderTypology(models.Model):
    _name = 'sale.order.type'
    _description = 'Type of sale order'
    _order = 'sequence'

    @api.model
    def _get_domain_sequence_id(self):
        seq_type = self.env.ref('sale.seq_sale_order')
        return [('code', '=', seq_type.code)]

    @api.model
    def _get_selection_picking_policy(self):
        return self.env['sale.order'].fields_get(
            allfields=['picking_policy'])['picking_policy']['selection']

    def default_picking_policy(self):
        default_dict = self.env['sale.order'].default_get(['picking_policy'])
        return default_dict.get('picking_policy')

    name = fields.Char(string='Name', required=True, translate=True)
    description = fields.Text(string='Description', translate=True)
    sequence_id = fields.Many2one(
        comodel_name='ir.sequence', string='Entry Sequence', copy=False,
        domain=_get_domain_sequence_id)
    journal_id = fields.Many2one(
        comodel_name='account.journal', string='Billing Journal',
        domain=[('type', '=', 'sale')])
    warehouse_id = fields.Many2one(
        comodel_name='stock.warehouse', string='Warehouse')
    picking_policy = fields.Selection(
        selection='_get_selection_picking_policy', string='Shipping Policy',
        default=default_picking_policy)
    company_id = fields.Many2one(
        'res.company',
        related='warehouse_id.company_id', store=True, readonly=True)
    payment_term_id = fields.Many2one('account.payment.term', 'Payment Term')
    pricelist_id = fields.Many2one('product.pricelist', 'Pricelist')
    incoterm_id = fields.Many2one('stock.incoterms', 'Incoterm')
    sequence = fields.Integer(default=10)
    rule_ids = fields.One2many(
        comodel_name='sale.order.type.rule', inverse_name='order_type_id',
        copy=True)
    operating_unit_id = fields.Many2one(
        comodel_name='operating.unit',
        string='Operating Unit',

    )

    @api.multi
    def matches_order(self, order):
        self.ensure_one()
        return any(rule.matches_order(order) for rule in self.rule_ids)

    @api.multi
    def matches_invoice(self, invoice):
        self.ensure_one()
        return any(rule.matches_invoice(invoice) for rule in self.rule_ids)
