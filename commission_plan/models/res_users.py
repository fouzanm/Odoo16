# -*- coding: utf-8 -*-
from odoo import fields, models


class ResUsers(models.Model):
    """This is used to set commission type in Sales Person."""
    _inherit = "res.users"
    _description = 'Sales Person'

    commission_plan_id = fields.Many2one('crm.commission')
