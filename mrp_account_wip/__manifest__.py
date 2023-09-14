# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Accounting - MRP - WIP',
    'version': '1.0',
    'category': 'Manufacturing',
    'summary': 'Analytic accounting in Manufacturing',
    'description': """
Analytic Accounting in MRP
==========================

* Cost structure report
""",
    'website': 'https://www.odoo.com/page/manufacturing',
    'depends': ['mrp', 'account'],
    'data': [
        'views/mrp_production_views.xml',
        # 'views/cost_structure_report.xml',
    ],
    # 'demo': ['demo/mrp_account_demo.xml'],
    'installable': True,
    'auto_install': True,
    'license': 'OEEL-1',
}
