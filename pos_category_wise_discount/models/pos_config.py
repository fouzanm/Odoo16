# -*- coding: utf-8 -*-
from odoo import fields, models


class PosConfig(models.Model):
    """to add field in Pos configuration"""
    _inherit = 'pos.config'

    pos_categ_ids = fields.Many2many('pos.category',
                                     string='POS Product Category',
                                     relation='pos_product_category')
    pos_categ_discount = fields.Boolean(string="Limit Category Discount")
    discount_limit = fields.Float(string="Max Discount Limit")
