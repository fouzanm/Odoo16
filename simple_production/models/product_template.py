# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    """to add fields in Product Template"""
    _inherit = 'product.template'
    _description = 'Product Template'

    component_ids = fields.One2many('simple.component.product',
                                    'product_tmpl_id')
