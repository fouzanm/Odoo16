# -*- coding: utf-8 -*-
import datetime

from odoo import fields, models


class OrderHistory(models.Model):
    """to add fields in order history"""
    _name = 'order.history'
    _description = 'Order history details'
    _rec_name = 'sale_id'

    sale_id = fields.Many2one('sale.order', string="Name")
    purchase_ids = fields.One2many('purchase.order',
                                   'order_history_id',
                                   readonly=True)
    partner_id = fields.Many2one('res.partner', string='Customer')
    date = fields.Date(string='Date')
    salesperson_id = fields.Many2one('res.users',
                                     string="Sales Person")
    # vendor_ids = fields.Many2one('res.partner')

    def action_order_history(self):
        """action to create order history"""
        sale_order = self.env['sale.order'].search([
            ('state', '=', 'sale'),
            ('date_order', '>=', datetime.date.today())
        ])
        for record in sale_order:
            order_history = self.create({
                'sale_id': record.id,
                'partner_id': record.partner_id.id,
                'salesperson_id': record.user_id.id,
                'date': record.date_order
            })
            purchase_order = self.env['purchase.order'].search([
                ('origin', '=', record.name)
            ])
            for order in purchase_order:
                order_history.update({
                    'purchase_ids': [(fields.Command.link(order.id))]
                })
