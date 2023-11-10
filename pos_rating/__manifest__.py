# -*- coding: utf-8 -*-
{
    'name': 'POS Rating',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'summary': 'POS Rating',
    'description': 'POS Rating',
    'author': 'Fouzan M',
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/product_product.xml',
    ],
    'assets': {
       'point_of_sale.assets': [
           'pos_rating/static/src/js/pos_rating.js',
           'pos_rating/static/src/xml/pos_screen.xml',
           'pos_rating/static/src/xml/pos_receipt.xml',
       ],
    },
    'application': True,
    'installable': True,
    'license': 'LGPL-3'
}
