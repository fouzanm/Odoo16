# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    multiple_reference_ids = fields.Many2many('multiple.reference',
                                              readonly=True,
                                              string="Other Reference",
                                              help='Multiple Reference')
    reference_count = fields.Integer(compute='_compute_reference_count',
                                     string="Reference count",
                                     help='compute reference count')

    @api.depends('multiple_reference_ids')
    def _compute_reference_count(self):
        """compute reference count and add other references to other reference
         field"""
        for record in self:
            reference = self.env['multiple.reference'].search([
                ('product_id', '=', record.id)])
            record.reference_count = len(reference)
            record.multiple_reference_ids = reference.ids

    def create_reference(self):
        """action to open multiple reference model to create reference"""
        reference = self.env['multiple.reference'].search([
            ('name', '=', self.default_code),
            ('product_id', '=', self.id)])
        if not reference and self.default_code:
            self.env['multiple.reference'].create({
                'name': self.default_code,
                'product_id': self.id})
        return {
            'name': 'Multiple Reference',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'res_model': 'multiple.reference',
            'view_mode': 'tree, form',
            'views': [(False, 'tree'), (False, 'form')],
            'context': {'default_product_id': self.id},
            'domain': [('product_id', '=', self.id)],
        }
