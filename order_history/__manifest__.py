# -*- coding: utf-8 -*-
{
    'name': 'Order History',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'summary': 'Order History Details',
    'description': 'Order History Details',
    'author': 'Fouzan M',
    'depends': ['base', 'sale_management', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'data/order_history_cron_scheduler.xml',
        'views/res_partner.xml',
        'views/product_template.xml',
        'views/sale_order.xml',
        'views/order_history.xml',
    ],
    'application': True,
    'license': 'LGPL-3'
}
