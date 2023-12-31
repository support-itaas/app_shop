# -*- coding: utf-8 -*-
# Copyright (C) 2016-Today  ITAAS (<http://www.itaas.co.th/>).
{
    "name": "Thailand Accounting Enhancement",
    "category": 'Accounting',
    'summary': 'Thailand Accounting Enhancement.',
    "description": """
        .
    """,
    "sequence": 1,
    "author": "IT as a Service Co., Ltd.",
    "website": "http://www.itaas.co.th/",
    "version": '1.0',
    "depends": ['account','account_accountant','sale','stock','product','purchase','hr','account_asset'],
    "data": [

        'sequence.xml',
        #security
        'security/security_group.xml',
        #view
        'views/payment_journal.xml',
        'views/account_payment_view.xml',
        'views/account_journal_view.xml',
        'views/account_tax_view.xml',
        'views/account_move_view.xml',
        'views/account_account_view.xml',
        'views/customer_billing_view.xml',
        'views/account_invoice_view.xml',
        'views/bahttxt_convert_view.xml',
        'views/sale_order_view.xml',
        'views/purchase_order_view.xml',
        'views/product_view.xml',
        'views/res_company_view.xml',
        'views/res_partner_view.xml',
        'views/stock_valuation_history_view.xml',
        'views/report_stockhistory.xml',
        'views/tax_report_view.xml',
        'views/report_pnd53.xml',
        'views/report_pnd3.xml',
        'views/report_taxsummary.xml',
        'views/report_billing.xml',
        'views/account_asset_asset_view.xml',
        #customize base report
        'report/quotation_report.xml',
        'report/quotation_report1.xml',
        'report/quotation_report_th.xml',
        'report/purchase_report.xml',
        'report/purchase_report1.xml',
        'report/tax_invoice_report.xml',
        'report/tax_invoice_report1.xml',
        'report/receipt_report.xml',
        'report/customer_bill_report.xml',
        'report/customer_bill_report1.xml',
        'report/creditnote_report.xml',
        'report/debitnote_report.xml',
        #general report
        'report/report_reg.xml',
        'report/report_generalledger.xml',
        'report/journal_daily_report.xml',
        'report/journal_summary_report.xml',
        'report/teejai_report.xml',
        'report/teejai_reportRBS.xml',
        'report/teejai_report_journal.xml',
        'report/teejai_report02.xml',
        'report/teejai_report02_journal.xml',
        'report/report_financial.xml',
        'report/product_report.xml',
        'report/sale_tax_report.xml',
        'report/purchase_tax_report.xml',
        # in case for some company define themselves
        'report/debitcredit_report.xml',
        'report/debitcredit_report01.xml',
        'report/debitcredit_report02.xml',
        'report/debitcredit_report03.xml',
        'report/debitcredit_report04.xml',
        'report/debitcredit_report05.xml',
        'report/vendor_report.xml',
        'report/customer_report.xml',
        'report/holdingtax3_report.xml',
        'report/holdingtax53_report.xml',
        'report/asset_labels_report.xml',
        'report/asset_report.xml',
        #wizard
        'wizard/journal_report_view.xml',
        'wizard/creditor_report_view.xml',
        'wizard/receivable_report_view.xml',
        'wizard/asset_report_view.xml',
        #custom report depend on customer
        #'report_custom/receipt_report.xml',
        #'report_custom/report_custom_reg.xml',
        #security
        'security/ir.model.access.csv',


    ],
    'qweb': [],
    "installable": True,
    "application": True,
    "auto_install": False,
}
