# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Partner'

    sale_order_ids = fields.One2many('sale.order',
                                     'partner_id')
    product_count = fields.Integer(compute='_compute_product_count')

    def _compute_product_count(self):
        """to compute products"""
        for record in self:
            record.product_count = self.env['product.template'].search_count(
                [('id', 'in', [
                    rec.product_template_id.id for rec in
                    record.sale_order_ids.order_line])])

    def action_product_view(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Product',
            'view_mode': 'tree,form',
            'res_model': 'product.template',
            'domain': [('id', 'in', [
                record.product_template_id.id for record in
                self.sale_order_ids.order_line])]
        }
