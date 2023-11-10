# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrderLine(models.Model):
    """to add field Tolerance in Sale order line"""
    _inherit = 'sale.order.line'
    _description = 'Sale order line'

    tolerance = fields.Integer(string="Tolerance",
                               help="to set tolerance for a product")
