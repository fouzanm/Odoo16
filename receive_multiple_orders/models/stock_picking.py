# -*- coding: utf-8 -*-
from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    purchase_order_ids = fields.Many2many('purchase.order',
                                          domain="[('partner_id','=', partner_id),"
                                                 "('state', '=', 'purchase'),"
                                                 "('receipt_status', '!=', 'full')]",
                                          string='Purchase Order')
    is_incoming = fields.Boolean(default=False)

    @api.onchange('partner_id', 'purchase_order_ids', 'picking_type_id')
    def get_products(self):
        self.update({
            'move_ids': [(fields.Command.clear())]
        })
        if self.picking_type_id.code == 'incoming':
            self.is_incoming = True
        order_line = self.env['purchase.order.line'].search([
            ('order_id', 'in', self.purchase_order_ids.ids)])
        stock_move = self.env['stock.move'].search([
            ('purchase_line_id', 'in', order_line.ids)
        ])
        for record in stock_move:
            self.sudo().write({'move_ids': [fields.Command.create({
                'product_id': record.product_id,
                'product_uom_qty': record.product_qty,
                'name': record.product_id.name,
                'location_id': record.location_id.id,
                'location_dest_id': record.location_dest_id
            })]})

