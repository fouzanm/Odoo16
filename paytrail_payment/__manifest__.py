# -*- coding: utf-8 -*-
{
    'name': "Paytrail Payment",
    'version': '16.0.1.0.0',
    'category': 'Accounting/Payment Providers',
    'summary': "Paytrail Payment Gateway Integration",
    'author': 'Fouzan M',
    'depends': ['payment'],
    'data': [
        'views/payment_paytrail_template.xml',
        'views/payment_provider_views.xml',
        'data/payment_provider_data.xml',
    ],
    'application': False,
    'license': 'LGPL-3',
}
