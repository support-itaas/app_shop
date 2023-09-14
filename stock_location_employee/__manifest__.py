# -*- coding: utf-8 -*-
# Copyright (C) 2020-today ITAAS (Dev K.Book)

{
    'name' : 'Stock location Employee',
    'version': '11.0.1.2.0',
    "category": "Sale",
    'author': 'IT as a Service Co., Ltd.',
    'website': 'http://www.itaas.co.th/',
    'license': 'AGPL-3',
    "depends": ['stock',],
    "data": [
        # views stock.location
        'views/stock_location_veiw.xml',

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
