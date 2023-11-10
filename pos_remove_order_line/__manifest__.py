# -*- coding: utf-8 -*-
{
    'name': 'POS Remove Order line',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'summary': 'POS Remove Order line',
    'description': 'POS Remove Order line',
    'author': 'Fouzan M',
    'depends': ['base', 'point_of_sale'],
    'assets': {
       'point_of_sale.assets': [
           'pos_remove_order_line/static/src/js/remove_order_line.js',
           'pos_remove_order_line/static/src/js/clear_order.js',
           'pos_remove_order_line/static/src/xml/remove_order_line.xml',
           'pos_remove_order_line/static/src/xml/clear_order.xml',
       ],
    },
    'application': True,
    'installable': True,
    'license': 'LGPL-3'
}
