# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    """to add field Tolerance in Customer"""
    _inherit = 'res.partner'
    _description = 'Partner'

    tolerance = fields.Integer(string="Tolerance",
                               help="to set tolerance for a product")
