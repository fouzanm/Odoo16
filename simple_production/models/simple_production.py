# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SimpleProduction(models.Model):
    """to create model simple production"""
    _name = 'simple.production'
    _description = 'Simple Production'

    name = fields.Char(string="Production No:", readonly=True,
                       default=lambda self: _('New'), copy=False)
    product_id = fields.Many2one('product.template',
                                 string="Product")
    quantity = fields.Integer(default="1", string='Quantity')
    component_ids = fields.One2many('simple.component.product',
                                    'simple_production_id')
    state = fields.Selection(selection=[('draft', 'Draft'),
                                        ('confirm', 'Confirm'),
                                        ('done', 'Done')],
                             default='draft')
    destination_id = fields.Many2one('stock.location',
                                     string='Destination Location')
    transfer_count = fields.Integer(compute='_compute_transfer_count')

    @api.onchange('quantity', 'product_id')
    def _onchange_product(self):
        """function for getting component product"""
        self.update({
            'component_ids': [fields.Command.clear()]
        })
        for record in self.product_id.component_ids:
            self.update({
                'component_ids': [(fields.Command.create({
                    'product_id': record.product_id,
                    'quantity': self.quantity * record.quantity,
                    'source_location_id': record.source_location_id
                }))]
            })

    def _compute_transfer_count(self):
        """to compute count of transfers"""
        for record in self:
            record.transfer_count = self.env['stock.picking'].search_count(
                [('origin', '=', self.name)])

    @api.model
    def create(self, vals):
        """to create simple production sequence"""
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'simple.production.sequence') or _('New')
        res = super(SimpleProduction, self).create(vals)
        return res

    def action_production_confirm(self):
        """action to create component transfer"""
        self.state = 'confirm'
        for record in self.component_ids:
            stock_picking = self.env['stock.picking'].create({
                'location_id': record.source_location_id.id,
                'location_dest_id':
                    self.product_id.property_stock_production.id,
                'picking_type_id':
                    self.env.ref('stock.picking_type_internal').id,
                'origin': self.name,
                'move_ids': [fields.Command.create({
                    'product_id': record.product_id.id,
                    'product_uom_qty': record.quantity,
                    'location_id': record.source_location_id.id,
                    'location_dest_id':
                        self.product_id.property_stock_production.id,
                    'name': record.product_id.name
                })]
            })
            stock_picking.action_confirm()
            stock_picking.move_ids.quantity_done = record.quantity
            stock_picking.button_validate()

    def action_production_done(self):
        """action to create product transfer"""
        self.state = 'done'
        if not self.destination_id:
            self.destination_id = self.env.ref('stock.stock_location_stock')
        stock_picking = self.env['stock.picking'].create({
            'location_id': self.product_id.property_stock_production.id,
            'location_dest_id': self.destination_id.id,
            'picking_type_id':
                self.env.ref('stock.picking_type_internal').id,
            'origin': self.name,
            'move_ids': [fields.Command.create({
                'product_id': self.product_id.product_variant_id.id,
                'name': self.product_id.product_variant_id.name,
                'product_uom_qty': self.quantity,
                'location_id': self.product_id.product_variant_id.
                property_stock_production.id,
                'location_dest_id': self.destination_id.id,
            })]
        })
        stock_picking.action_confirm()
        stock_picking.move_ids.quantity_done = self.quantity
        stock_picking.button_validate()

    def get_transfer(self):
        """action for smart button to view transfers"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Transfer',
            'view_mode': 'tree,form',
            'res_model': 'stock.picking',
            'domain': [('origin', '=', self.name)],
            'context': "{'create': False}"
        }
