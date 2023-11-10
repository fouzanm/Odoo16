# -*- coding: utf-8 -*-
from odoo import fields, models


class PurchaseOrderLine(models.Model):
    """to add field Tolerance in Purchase order line"""
    _inherit = 'purchase.order.line'
    _description = 'Purchase order line'

    tolerance = fields.Integer(string="Tolerance",
                               help="to set tolerance for a product")
