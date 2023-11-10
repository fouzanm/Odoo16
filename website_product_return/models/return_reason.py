# -*- coding: utf-8 -*-
from odoo import fields, models


class ReturnReason(models.Model):
    _name = 'return.reason'

    name = fields.Char(string="Reason")
