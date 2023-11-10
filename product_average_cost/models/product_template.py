# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    """to add field in product template model"""
    _inherit = 'product.template'
    _description = 'Product Template'

    average_cost = fields.Float(string="Average Cost",
                                compute="_compute_average_cost")

    def _compute_average_cost(self):
        """function to compute average product cost"""
        for record in self:
            purchase_order = self.env['purchase.order.line'].search([
                ('state', '=', 'purchase'),
                ('product_id.product_tmpl_id', '=', record.id)
            ])
            quantity = 0
            subtotal = 0
            for rec in purchase_order:
                quantity += rec.product_qty
                subtotal += rec.price_subtotal
            record.average_cost = subtotal/quantity if quantity > 0 else 0
