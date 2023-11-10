# -*- coding: utf-8 -*-
{
    'name': 'Quiz Idle Timer',
    'version': '16.0.1.0.0',
    'category': 'Marketing',
    'summary': 'Quiz Idle Timer',
    'description': 'Quiz Idle Timer',
    'author': 'Fouzan M',
    'depends': ['base', 'survey'],
    'data': [
        'views/survey_survey.xml',
        'views/idle_timer.xml',
    ],
    'assets': {
            'web.assets_frontend': [
                'quiz_idle_timer/static/src/js/quiz_idle_timer.js',
            ]
        },
    'application': False,
    'license': 'LGPL-3'
}
