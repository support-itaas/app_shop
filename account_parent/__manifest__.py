# -*- coding: utf-8 -*-
##############################################################################
#    Copyright (C) 2019 Technaureus Info Solutions Pvt. Ltd.
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################
{
    'name': "Parent Account",
    'summary': """
        Adds Parent account and ability to open chart of account list view based on the date and moves""",
    'description': """
This module will be very useful for those who are still using v7/v8 because of the no parent account and chart of account heirarchy view in the latest versions
        * Adds parent account in account
        * Adds new type 'view' in account type
        * Adds Chart of account heirachy view
        * Adds credit, debit and balance in account
        * Shows chart of account based on the date and target moves we have selected
        * Provide Pdf and Xls reports
    - Need to set the group show chart of account structure to view the chart of account heirarchy.
    
    Contact us for any need of customisation or chart of account migration from v7/v8 - v9/v10
    """,

    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'website': 'http://www.technaureus.com',
    'category': 'Accounting &amp; Finance',
    'version': '11.0.1.6.0',
    'depends': ['account'],
    'data': [
        'security/account_parent_security.xml',
        'views/account_view.xml',
        'views/open_chart.xml',
        'data/account_type_data.xml',
        'views/account_parent_template.xml',
        'views/report_coa_heirarchy.xml',
    ],
    'demo': [
    ],
    'qweb': [
        'static/src/xml/account_parent_backend.xml',
    ],
    'currency': 'EUR',
    'price': '50.0',
    'installable':True,
}
