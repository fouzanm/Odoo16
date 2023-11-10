# -*- coding: utf-8 -*-
{
    'name': 'Stock Report',
    'version': '16.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Stock Report',
    'description': 'Stock Report',
    'author': 'Fouzan M',
    'depends': ['base', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'data/stock_report_email.xml',
        'data/stock_report_cron_scheduler.xml',
        'views/res_config_settings.xml',
        'report/stock_report_pdf_action.xml',
        'report/stock_report_template.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3'
}
