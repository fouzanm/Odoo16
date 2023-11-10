# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PurchaseOrder(models.Model):
    """to inherit purchase order"""
    _inherit = 'purchase.order'
    _description = 'Purchase order'

    supplier_ids = fields.One2many('supplier.info',
                                   'purchase_order_id')

    @api.constrains('order_line', 'partner_id')
    def _create_supplier(self):
        """to display all the supplier and product in supplier tree view for all
        selected products in order line."""
        self.update({
            'supplier_ids': [(fields.Command.clear())]
        })
        for record in self.order_line:
            for rec in record.product_id.seller_ids:
                if rec.partner_id != self.partner_id:
                    self.update({
                        'supplier_ids': [fields.Command.create({
                            'product_id': record.product_id.id,
                            'partner_id': rec.partner_id.id,
                            'price_unit': rec.price,
                            'quantity': record.product_qty,
                        })]
                    })

    def check_best_price(self):
        """to compare the best vendors and prices"""
        self.ensure_one()
        self._create_supplier()
        for record in self.supplier_ids.mapped('product_id'):
            order = self.supplier_ids.filtered(
                lambda r: r.product_id == record).sorted(
                key=lambda r: r.price_unit)
            if order:
                order[0].best_price = True
        return {
            'type': 'ir.actions.act_window',
            'name': 'Check Best Price',
            'view_mode': 'form',
            'res_model': 'best.price.wizard',
            'target': 'new',
            'context': {'default_supplier_ids': [
                (fields.Command.link(record))
                for record in self.supplier_ids.ids
            ]}
        }
