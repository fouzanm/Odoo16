# -*- coding: utf-8 -*-
from odoo import fields, models


class CrmTeam(models.Model):
    """This is used to set commission type in Sales Team."""
    _inherit = "crm.team"
    _description = 'Sales Team'

    commission_plan_id = fields.Many2one('crm.commission')
