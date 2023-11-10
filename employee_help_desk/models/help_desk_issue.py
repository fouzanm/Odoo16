# -*- coding: utf-8 -*-
from odoo import fields, models


class HelpDeskIssue(models.Model):
    """to create issue type"""
    _name = 'help.desk.issue'

    name = fields.Char(string="Issues")
