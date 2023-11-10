# -*- coding: utf-8 -*-
{
    'name': 'Commission Plan',
    'version': '16.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Commission Plan',
    'description': 'Commission Plan',
    'author': 'Fouzan M',
    'depends': ['base', 'sale_management', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_commission.xml',
        'views/commission_productwise.xml',
        'views/commission_revenuewise.xml',
        'views/res_users.xml',
        'views/crm_team.xml',
        'views/sale_order.xml',
        'wizard/commission_report_wizard.xml',
        'report/commission_report.xml',
        'report/commission_report_template.xml',
        'views/commission_menus.xml',
    ],
    'assets': {
                'web.assets_backend': [
                    'commission_plan/static/src/js/action_manager.js',
                ],
            },
    'application': True,
    'license': 'LGPL-3'
}
