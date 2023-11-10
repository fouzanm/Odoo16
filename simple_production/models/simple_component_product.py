# -*- coding: utf-8 -*-
from odoo import fields, models


class SimpleComponentProduct(models.Model):
    """to set component products for a product"""
    _name = 'simple.component.product'
    _description = 'Component Product'

    product_tmpl_id = fields.Many2one('product.template')
    product_id = fields.Many2one('product.product')
    quantity = fields.Integer(default="1", string="Quantity")
    simple_production_id = fields.Many2one('simple.production')
    source_location_id = fields.Many2one('stock.location',
                                         string='Source Location',
                                         required=True)
