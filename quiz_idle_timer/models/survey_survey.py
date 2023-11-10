# -*- coding: utf-8 -*-
from odoo import fields, models


class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    inactivity_duration = fields.Integer(string='Inactivity Duration',
                                         help='You can set duration of'
                                              'inactivity')
    countdown_time = fields.Integer(string='Countdown Time',
                                    help='You can set countdown time for Idle'
                                         'Timer')
