# -*- coding: utf-8 -*-
{
    'name': 'Employee Helpdesk',
    'version': '16.0.1.0.0',
    'category': 'Human Resources/Employees',
    'summary': 'Employee Helpdesk',
    'description': 'Employee Helpdesk',
    'author': 'Fouzan M',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_helpdesk_ticket.xml',
        'views/website_ticket.xml',
        'views/website_ticket_form.xml',
        'views/employee_helpdesk_menu.xml'
    ],
    'application': True,
    'license': 'LGPL-3'
}
