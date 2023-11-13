# -*- coding: utf-8 -*-
{
    'name': 'Multiple Reference Per Product',
    'version': '16.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Multiple Reference Per Product',
    'description': 'Multiple Reference Per Product',
    'author': 'Fouzan M',
    'depends': ['base', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/multiple_reference.xml',
        'views/product_template.xml',
        'views/product_product.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3'
}