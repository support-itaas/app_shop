# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Sales Commissions Based on Target with Amount Ranges by Sales/Invoice/Payment',
    'version' : '1.1',
    'price' : 149.0,
    'currency': 'EUR',
    'category': 'Sales',
    'license': 'Other proprietary',
   # 'live_test_url': 'https://youtu.be/-wK3ouvQw2I',
    'description': """
Sales Commission by Sales/Invoice/Payment
Sales Commissions with Amount Ranges by Sales/Invoice/Payment
sales Commission
sale_commission
sales_Commission
sale Commission
sales Commissions
sales order Commission
Target Based Sales Commission
sales commission based on target
commission based on target
commission target
sales Incentive
sale Incentive
Target Based Sales Commission
Odoo Sales Commission / Incentive Management
Incentive Management
Odoo Sales Commission
sale_commission_target
Create your own targets based on teams
Linking of sales manager and salesman commission
Further customizable as per your business requirements.
order Commission
sales person Commission
sales team Commission
sale team Commission
sale person Commission
team Commission
Commission
sales order on Commission
invoice on Commission
payment on Commission
Commission invoice
Commission vendor invoice
sales Commision
Commission sales user invoice

Sales Commission (form)
Sales Commission (form)
Sales Commission List (tree)
Sales Commission List (tree)
Sales Commission Search (search)
Sales Commission Search (search)
sales_commission_id (qweb)
sales_commission_worksheet_id (qweb)

Sales Commission by Sales/Invoice/Payment

This module provide feature to manage sales commision by Sales/Invoice/Payments


This module allow company to manage sales commision with different options. You can configure after installing module what option/policy your company is following to give commissions to your sales users.
We are allowing you to select When to Pay and Calculation based on . Here you can define policy which will be used to give commission to your sales team.


For every Calcalulation based on we are allowing you to select:
1. Sales Manager Commission %
2. Sales Person Commission %

If you keep Sales Manager Commission 0% then system will not create sales commision lines and sales commision worksheet. System will work only with single option at time ie for example you can select When to Pay = Invoice confirm and calculation based on = Product category so system will run on that and create commission.

Please note that When to Pay = Customer payment is only supported with Calculation based on Sales Team. - Other options are supported in matrix. 
Workflow will be:
Option1 : Sales Confirmation -> Create Sales commission worksheet (if not created for current month) -> Add Sales commission lines on worksheet -> For every sales of current month, system will append sales commission lines on worksheet. -> End of month Accouant may review worksheet and create commision invoice to pay/release commision to sales person.
Option2 : Invoice Validate -> Create Sales commission worksheet (if not created for current month) -> Add Sales commission lines on worksheet -> For every invoice validation of current month, system will append sales commission lines on worksheet. -> End of month Accouant may review worksheet and create commision invoice to pay/release commision to sales person.
Option3 : Customer Payment -> Create Sales commission worksheet (if not created for current month) -> Add Sales commission lines on worksheet -> For every payment from customer of current month, system will append sales commission lines on worksheet. -> End of month Accouant may review worksheet and create commision invoice to pay/release commision to sales person.
Commission to sales person always will be in company currency. Multi currency is supported for this module so sales order/ invoice / payment can be in different currency but system will take care for it and create commission lines in company currency.
Sales Commission product is created using data and you still can change commission product on commission worksheet to create commission invoice.

Menus
---- Invoicing/Commissions
---- ---- Invoicing/Commissions/Commission Worksheets
---- ---- Invoicing/Commissions/Sales Commissions Lines
---- Sales/Commissions
---- ---- Sales/Commissions/Commission Worksheets
---- ---- Sales/Commissions/Sales Commissions Lines

Configuration for Sales Commission

Commission to sales person always will be in company currency. Multi currency is supported for this module so sales order/ invoice / payment can be in different currency but system will take care for it and create commission lines in company currency.
Sales Commission product is created using data and you still can change commission product on commission worksheet to create commission invoice.
Commission amount will be based on Net Revenue Model where it consider amounts without taxes. (This module does not support Gross Margin Model)
This module provide feature to manage Sales Commissions with Amount Ranges by Sales/Invoice/Payment


            """,
    'summary' : 'This module provide feature to manage Sales Commissions based on target with Amount Ranges by Sales/Invoice/Payment',
    'author' : 'Probuse Consulting Service Pvt. Ltd.',
    'website' : 'www.probuse.com',
    'depends' : ['account','sale_management'],
    'support': 'contact@probuse.com',
    'data' : [
              'security/ir.model.access.csv',
              'security/sales_commission_security.xml',
              'data/commission_sequence.xml',
              'data/product_data.xml',
              'view/sale_config_settings_views.xml',
              'view/crm_team_view.xml',
              'view/product_template_view.xml',
#               'view/product_view.xml',
              'view/product_category_view.xml',
              'view/sales_commission_view.xml',
              'view/account_invoice_view.xml',
              'view/report_sales_commission.xml',
              'view/report_sales_commission_worksheet.xml',
              'view/account_payment.xml',
              'view/sale_view.xml',
              ],
    'installable' : True,
    'images': ['static/description/img1.jpg'],
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
