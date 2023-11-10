# -*- coding: utf-8 -*-
from odoo import fields, models

class SaleOrder(models.Model):
    """to inherit sale order"""
    _inherit = 'sale.order'
    _description = 'Sale order'

    purchase_count = fields.Integer(compute='_compute_purchase_order')

    def action_confirm(self):
        """action to create purchase order"""
        for record in self.order_line:
            product = self.env['product.product'].search([
                ('product_tmpl_id', '=', record.product_template_id.id)
            ])
            self.env['purchase.order'].create({
                'origin': self.name,
                'partner_id': record.product_template_id.seller_ids.partner_id[0].id,
                'order_line': [fields.Command.create({
                    'product_id': product.id,
                    'product_qty': record.product_uom_qty
                })]
            })
        return super(SaleOrder, self).action_confirm()

    def _compute_purchase_order(self):
        """to compute purchase order count"""
        for record in self:
            record.purchase_count = self.env['purchase.order'].search_count(
                [('origin', '=', self.name)])
    def action_purchase_order_view(self):
        """action to view purchase orders of corresponding products"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Purchase',
            'view_mode': 'tree,form',
            'res_model': 'purchase.order',
            'domain': [('origin', '=', self.name)]
        }
