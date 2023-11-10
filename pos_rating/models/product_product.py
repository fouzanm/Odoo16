# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductProduct(models.Model):
    """to add field in Product page"""
    _inherit = 'product.product'

    quality_rating = fields.Selection(selection=[('1', '1'), ('2', '2'),
                                                 ('3', '3'), ('4', '4'),
                                                 ('5', '5')],
                                      help='here you can add product quality')
