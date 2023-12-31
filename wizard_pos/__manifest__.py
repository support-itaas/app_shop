# -*- coding: utf-8 -*-
# Copyright (C) 2019-Today  Technaureus Info Solutions Pvt Ltd.(<http://technaureus.com/>).
# 11.0.3.8 - 30/06/2021 - fix wizard pos make pos loading screen taking long time
{
    'name': 'Wizard POS',
    'version': '11.0.3.13',
    'category': 'pos',
    'sequence': 1,
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'summary': 'This module is for creating a wizard in pos',
    'website': 'http://www.technaureus.com/',
    'description': """This module is for creating a wizard in pos
""",
    'depends': ['wizard_coupon', 'tis_pos_customer_required', 'operating_unit'],
    'data': [
        'security/coupon_security.xml',
        'views/pos_config_views.xml',
        'views/pos_order.xml',
        'views/pos_session.xml',
        'views/wizard_pos_template.xml',
        'views/project_views.xml',
        'views/res_partner_views.xml',
        'data/pos_category_data.xml',
        'data/pos_data.xml',
    ],
    'qweb': ['static/src/xml/pos.xml'],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
