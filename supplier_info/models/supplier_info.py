# -*- coding: utf-8 -*-
from odoo import fields, models


class SupplierInfo(models.Model):
    """to add fields in supplier tree"""
    _name = 'supplier.info'
    _description = 'Supplier Information'

    purchase_order_id = fields.Many2one('purchase.order')
    partner_id = fields.Many2one('res.partner')
    product_id = fields.Many2one('product.product')
    price_unit = fields.Integer(string="Unit Price")
    quantity = fields.Integer(string="Quantity")
    best_price = fields.Boolean(default=False)

    def action_create_order(self):
        """action to create purchase order."""
        self.env['purchase.order'].create({
            'partner_id': self.partner_id.id,
            'order_line': [(fields.Command.create({
                'product_id': self.product_id.id,
                'product_qty': self.quantity,
                'price_unit': self.price_unit
            }))]
        })
        for record in self.purchase_order_id.order_line:
            if record.product_id.id == self.product_id.id:
                record.unlink()
