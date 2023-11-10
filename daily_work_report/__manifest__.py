# -*- coding: utf-8 -*-
{
    'name': 'Daily Work Report',
    'version': '16.0.1.0.0',
    'category': 'Extra',
    'summary': 'Daily Work Report',
    'description': 'Daily Work Report',
    'author': 'Fouzan M',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/daily_work_report.xml',
        'views/daily_work_report_dashboard.xml',
        'wizard/work_report_wizard.xml',
        'report/work_report.xml',
        'report/work_report_template.xml',
        'views/daily_work_report_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'daily_work_report/static/src/dashboard/work_report_dashboard.js',
            'daily_work_report/static/src/dashboard/work_report_dashboard.xml',
            'daily_work_report/static/src/dashboard/work_report_chart.js',
            'daily_work_report/static/src/dashboard/work_report_chart.xml',
        ]
    },
    'application': True,
    'installable': True,
    'license': 'LGPL-3'
}
