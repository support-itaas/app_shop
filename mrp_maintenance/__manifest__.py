# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Maintenance - MRP',
    'version': '1.0',
    'category': 'Manufacturing',
    'summary': 'Schedule and manage maintenance on machine and tools.',
    'description': """
Maintenance in MRP
==================
* Preventive vs corrective maintenance
* Define different stages for your maintenance requests
* Plan maintenance requests (also recurring preventive)
* Equipments related to workcenters
* MTBF, MTTR, ...
""",
    'depends': ['quality_mrp', 'maintenance'],
    'data': [
        'views/maintenance_views.xml',
        'views/mrp_views.xml'
    ],
    'demo': ['data/mrp_maintenance_demo.xml'],
    'application': True,
    'license': 'OEEL-1',
}
