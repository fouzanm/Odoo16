# -*- coding: utf-8 -*-
{
    'name': 'Supplier Info',
    'version': '16.0.1.0.0',
    'category': 'Extra',
    'summary': 'Supplier Info',
    'description': 'Supplier Info',
    'author': 'Fouzan M',
    'depends': ['base', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_order.xml',
        'wizard/best_price_wizard.xml'
    ],
    'license': 'LGPL-3'
}