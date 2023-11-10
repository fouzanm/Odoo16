# -*- coding: utf-8 -*-
from odoo import api, fields, models


class DataRecord(models.TransientModel):
    """model to save search record"""
    _name = 'data.record'

    record_id = fields.Integer(string="ID")
    field = fields.Char(string="Field")
    data = fields.Char(string="Data")
    model = fields.Char()
    model_name = fields.Char(string='Model')
    data_id = fields.Many2one(comodel_name='data.search')

    def action_to_view_data(self):
        """action to view data"""
        return {
            'name': "Data View",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': self.model,
            'res_id': self.record_id,
            'target': 'new',
        }
