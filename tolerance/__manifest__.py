# -*- coding: utf-8 -*-
{
    'name': 'Tolerance',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'summary': 'Tolerance',
    'description': 'Tolerance',
    'author': 'Fouzan M',
    'depends': ['base', 'sale_management', 'purchase', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/sale_order.xml',
        'views/purchase_order.xml',
        'wizard/stock_picking_wizard.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
    'license': 'LGPL-3'
}
