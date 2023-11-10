# -*- coding: utf-8 -*-
{
    'name': 'Website Product Return',
    'version': '16.0.1.0.0',
    'category': 'Website',
    'summary': 'Website Product Return',
    'description': 'Website Product Return',
    'author': 'Fouzan M',
    'depends': ['base', 'website', 'sale', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'data/product_return_sequence.xml',
        'views/product_return.xml',
        'views/website_product_return.xml',
        'views/website_return_form.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3'
}
