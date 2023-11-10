# -*- coding: utf-8 -*-
{
    'name': 'Calculator in POS Screen',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'summary': 'Calculator in POS Screen',
    'description': 'Calculator in POS Screen',
    'author': 'Fouzan M',
    'depends': ['base', 'point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            'calculator_in_pos/static/src/js/calculator_in_pos.js',
            'calculator_in_pos/static/src/js/calculator_popup.js',
            'calculator_in_pos/static/src/xml/calculator_in_pos.xml',
            'calculator_in_pos/static/src/xml/calculator_popup.xml',
            'calculator_in_pos/static/src/css/calculator.css',
        ],
    },
    'application': True,
    'installable': True,
    'license': 'LGPL-3'
}
