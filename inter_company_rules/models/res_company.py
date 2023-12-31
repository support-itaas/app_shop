# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import Warning


class res_company(models.Model):

    _inherit = 'res.company'

    so_from_po = fields.Boolean(string="Create Sales Orders when buying to this company",
        help="Generate a Sales Order when a Purchase Order with this company as vendor is created.\n The intercompany user must at least be Sale User.")
    po_from_so = fields.Boolean(string="Create Purchase Orders when selling to this company",
        help="Generate a Purchase Order when a Sales Order with this company as customer is created.\n The intercompany user must at least be Purchase User.")
    auto_generate_invoices = fields.Boolean(string="Create Invoices/Credit Notes when encoding invoices/credit notes made to this company",
        help="Generate Customer/Vendor Bills (and credit notes) when encoding invoices (or credit notes) made to this company.\n e.g: Generate a Customer Invoice when a Vendor Bill with this company as vendor is created.")
    auto_validation = fields.Boolean(string="Sale/Purchase Orders Auto Validation",
        help="When a Sales Order or a Purchase Order is created by a multi company rule for this company, it will automatically validate it")
    intercompany_user_id = fields.Many2one("res.users", string="Inter Company User", default=SUPERUSER_ID,
        help="Responsible user for creation of documents triggered by intercompany rules.")
    warehouse_id = fields.Many2one("stock.warehouse", string="Warehouse",
        help="Default value to set on Purchase(Sales) Orders that will be created based on Sale(Purchase) Orders made to this company")

    @api.model
    def _find_company_from_partner(self, partner_id):
        company = self.sudo().search([('partner_id', '=', partner_id)], limit=1)
        return company or False

    @api.one
    @api.constrains('po_from_so', 'so_from_po', 'auto_generate_invoices')
    def _check_intercompany_missmatch_selection(self):
        if (self.po_from_so or self.so_from_po) and self.auto_generate_invoices:
            raise Warning(_('''You cannot select to create invoices based on other invoices
                    simultaneously with another option ('Create Sales Orders when buying to this
                    company' or 'Create Purchase Orders when selling to this company')!'''))

