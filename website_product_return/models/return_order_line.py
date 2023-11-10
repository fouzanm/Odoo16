# -*- coding: utf-8 -*-
from odoo import fields, models


class ReturnOrderLine(models.Model):
    _name = 'return.order.line'

    name = fields.Char(related='product_id.name')
    product_id = fields.Many2one('product.product')
    quantity = fields.Integer(string='Quantity')
    location_id = fields.Many2one('stock.location')
    location_dest_id = fields.Many2one('stock.location')
    return_id = fields.Many2one('product.return')
