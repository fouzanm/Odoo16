# -*- coding: utf-8 -*-
{
    'name': 'POS Category Wise Discount',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'summary': 'POS Category Wise Discount',
    'description': 'POS Category Wise Discount',
    'author': 'Fouzan M',
    'depends': ['base', 'point_of_sale', 'pos_discount'],
    'data': [
        'views/res_config_settings.xml',
    ],
    'assets': {
       'point_of_sale.assets': [
           'pos_category_wise_discount/static/src/js/categ_discount_limit.js',
       ],
    },
    'application': True,
    'installable': True,
    'license': 'LGPL-3'
}
