# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class MultipleReference(models.Model):
    _name = 'multiple.reference'
    _description = 'Multiple Reference'

    name = fields.Char(string="Reference", help="Reference")
    product_id = fields.Many2one('product.product', string='Product',
                                 help="Product")
    is_default_code = fields.Boolean(compute='_compute_default_code',
                                     string='Default Code')

    @api.depends('name')
    def _compute_default_code(self):
        """to compute default code"""
        for record in self:
            record.is_default_code = True if \
                record.name == record.product_id.default_code else False


    def action_to_set_default(self):
        """action to set current reference as default code"""
        self.product_id.default_code = self.name
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'type': 'success',
                'message': _('Default code is updated'),
                'next': {
                    'type': 'ir.actions.act_window_close'
                },
            }
        }

    def action_to_view_data(self):
        """action to view product page"""
        return {
            'name': 'Product Product',
            'type': 'ir.actions.act_window',
            'res_model': 'product.product',
            'view_type': 'form',
            'view_mode': 'form',
            'res_id': self.product_id.id,
        }
