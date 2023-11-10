# -*- coding: utf-8 -*-
{
    'name': 'Sales Report',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'summary': 'Sales Report',
    'description': 'Sales Report',
    'author': 'Fouzan M',
    'depends': ['base', 'sale', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sales_report_monthly_scheduler.xml',
        'data/sales_report_weekly_scheduler.xml',
        'data/sales_report_number.xml',
        'data/sales_report_email_template.xml',
        'views/sales_report.xml',
        'report/sales_report_pdf_action.xml',
        'report/sales_report_template.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3'
}
