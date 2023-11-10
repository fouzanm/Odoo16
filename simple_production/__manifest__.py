# -*- coding: utf-8 -*-
{
    'name': 'Simple Production',
    'version': '16.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Simple Production',
    'description': 'Simple Production',
    'author': 'Fouzan M',
    'depends': ['base', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template.xml',
        'views/simple_component_product.xml',
        'views/simple_production.xml',
        'data/simple_production_sequence.xml',
    ],
    'application': True,
    'license': 'LGPL-3'
}