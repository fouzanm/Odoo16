# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProductTemplate(models.Model):
    """to inherit product template"""
    _inherit = 'product.template'
    _description = 'Product Template'

    sale_count = fields.Integer(compute="_compute_sale_count")

    def _compute_sale_count(self):
        """to find count of product sale"""
        for record in self:
            record.sale_count = self.sales_count

    @api.onchange('list_price')
    def _onchange_list_price(self):
        """to change unit price if order is in draft stage"""
        orders = self.env['sale.order.line'].search([
            ('product_template_id', '=', self.ids[0]),
            ('state', '=', 'draft')
        ])
        orders.price_unit = self.list_price

