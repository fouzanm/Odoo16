# -*- coding: utf-8 -*-
{
    'name': 'Employee Dashboard',
    'version': '16.0.1.0.0',
    'category': 'Human Resources/Employees',
    'summary': 'Employee Dashboard',
    'description': 'Employee Dashboard',
    'author': 'Fouzan M',
    'depends': ['base', 'hr'],
    'data': [
        'views/employee_dashboard_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'employee_dashboard/static/src/dashboard/employee_dashboard.js',
            'employee_dashboard/static/src/dashboard/employee_chart.js',
            'employee_dashboard/static/src/dashboard/employee_dashboard.xml',
            'employee_dashboard/static/src/dashboard/employee_chart.xml',
        ]
    },
    'application': False,
    'license': 'LGPL-3'
}
