# -*- coding: utf-8 -*-
import datetime

from odoo import _, api, fields, models
from odoo.exceptions import MissingError


class ProductReturn(models.Model):
    _name = 'product.return'
    _description = "Website Product Return"

    name = fields.Char(readonly=True, default=lambda self: _('New'), copy=False)
    order_id = fields.Many2one('sale.order', string="Sale Order", copy=False,
                               domain="[('state', '=', 'sale')]", required=True)
    partner_id = fields.Many2one('res.partner', string="Customer", required=True
                                 , related="order_id.partner_id", copy=False,
                                 readonly=False)
    date = fields.Date(default=datetime.date.today())
    user_id = fields.Many2one('res.users', string="Responsible", copy=False,
                              related="order_id.user_id", readonly=False)
    status = fields.Selection(selection=[('draft', 'Draft'),
                                         ('confirm', 'Confirm'),
                                         ('done', 'Done')],
                              default='draft')
    reason_id = fields.Many2one('return.reason', string='Reason', copy=False)
    company_id = fields.Many2one('res.company', readonly=False, copy=False,
                                 related="order_id.company_id")
    order_line_ids = fields.One2many('return.order.line', 'return_id',
                                     copy=False)
    transfer_count = fields.Integer(compute='_compute_transfer_count')
    is_delivered = fields.Boolean(compute='_compute_is_delivered')

    @api.model
    def create(self, vals):
        """to generate return sequence"""
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'product.return.sequence') or _('New')
        res = super(ProductReturn, self).create(vals)
        return res

    @api.onchange('order_id')
    def create_order_line(self):
        """create orderline based on sale order"""
        self.update({
            'order_line_ids': [(fields.Command.clear())]
        })
        for record in self.order_id.order_line:
            picking = self.env['stock.picking'].search([
                ('origin', '=', self.order_id.name),
                ('picking_type_id.code', '=', 'outgoing')])
            if picking:
                del_location = picking[0].location_dest_id
                self.sudo().write({'order_line_ids': [fields.Command.create({
                    'product_id': record.product_id.id,
                    'name': record.product_id.name,
                    'location_id': del_location,
                    'location_dest_id': self.env['stock.move'].search([
                        ('sale_line_id', '=', record.id),
                        ('location_dest_id', '=', del_location.id)])[
                        0].location_id,
                })]})

    def _compute_transfer_count(self):
        """to compute transfer count"""
        for record in self:
            record.transfer_count = self.env['stock.picking'].search_count(
                [('origin', '=', record.order_id.name)])

    def get_transfer(self):
        """action for smart button to view transfers"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Transfer',
            'view_mode': 'tree,form',
            'res_model': 'stock.picking',
            'domain': [('origin', '=', self.order_id.name)],
            'context': "{'create': False}"
        }

    @api.depends('order_id')
    def _compute_is_delivered(self):
        """to check the transfer is delivered or not"""
        for record in self:
            order = self.env['stock.picking'].sudo().search([
                ('sale_id', '=', record.order_id.id), ('state', '=', 'done')])
            is_delivered = False
            for rec in order:
                if rec.state == 'done':
                    is_delivered = True
            record.is_delivered = True if is_delivered else False

    def action_return_confirm(self):
        """to confirm return order and validate the delivery is done or not"""
        if self.is_delivered:
            self.status = 'confirm'
            for record in self.order_line_ids:
                if record.quantity == 0:
                    record.unlink()
        else:
            raise MissingError(_("Returns are not possible for orders that "
                                 "have not been delivered."))

    def action_return_done(self):
        """action to create return transfer"""
        order = self.env['stock.picking'].sudo().search([
            ('sale_id', '=', self.order_id.id), ('state', '=', 'done')])
        picking_type = order[0].picking_type_id.return_picking_type_id
        stock_picking = self.env['stock.picking'].sudo().create({
            'picking_type_id': picking_type.id,
            'origin': self.order_id.name,
            'partner_id': self.partner_id.id,
            'move_ids': [fields.Command.create({
                'name': record.name,
                'product_id': record.product_id.id,
                'product_uom_qty': record.quantity,
                'quantity_done': record.quantity,
                'location_id': record.location_id.id,
                'location_dest_id': record.location_dest_id.id
            }) for record in self.order_line_ids]
        })
        stock_picking.action_confirm()
        stock_picking.button_validate()
        self.status = 'done'
