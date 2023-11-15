# -*- coding: utf-8 -*-
{
    'name': 'POS Product Creation',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'summary': 'POS Product Creation',
    'description': 'POS Product Creation',
    'author': 'Fouzan M',
    'depends': ['base', 'point_of_sale'],
    'assets': {
       'point_of_sale.assets': [
           'pos_product_creation/static/src/js/pos_product.js',
           'pos_product_creation/static/src/js/product_list_screen.js',
           'pos_product_creation/static/src/js/create_product_popup.js',
           'pos_product_creation/static/src/js/edit_product_popup.js',
           'pos_product_creation/static/src/xml/product_button.xml',
           'pos_product_creation/static/src/xml/product_list_screen.xml',
           'pos_product_creation/static/src/xml/create_product_popup.xml',
           'pos_product_creation/static/src/xml/edit_product_popup.xml',
       ],
    },
    'application': True,
    'installable': True,
    'license': 'LGPL-3'
}
