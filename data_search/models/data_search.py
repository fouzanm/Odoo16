# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import MissingError, ValidationError


class DataSearch(models.TransientModel):
    """model for search data"""
    _name = 'data.search'

    content = fields.Char(string="Content", required=True)
    models_id = fields.Many2many(comodel_name='ir.model', string="Model",
                                 required=True)
    fields_id = fields.Many2many(comodel_name='ir.model.fields', string="Field",
                                 domain="[('model_id', 'in', models_id)]")
    record_ids = fields.One2many(comodel_name='data.record',
                                 inverse_name='data_id')

    @api.onchange('models_id')
    def _onchange_models(self):
        for record in self.fields_id:
            if record.model_id.id not in self.models_id.ids:
                self.fields_id = False

    def action_data_search(self):
        """action to create search data based on conditions."""
        self.update({
            'record_ids': [(fields.Command.clear())]
        })
        item = []
        for model in self.models_id:
            if self.env[model.model].sudo()._abstract:
                raise ValidationError("Abstract models are not allowed")
            for record in self.env[model.model].sudo().search_read([]):
                if self.fields_id:
                    for field in self.fields_id:
                        if (self.content.lower() in
                                str(record[field.name]).lower()):
                            item.append({
                                'id': record['id'],
                                'field': field.name,
                                'data': record[field.name],
                                'model_name': model.name,
                                'model': model.model})
                else:
                    for key, value in record.items():
                        if self.content.lower() in str(value).lower():
                            item.append({
                                'id': record['id'],
                                'field': key,
                                'data': value,
                                'model_name': model.name,
                                'model': model.model})
        if not item:
            raise MissingError("No results found for your condition.")
        for record in item:
            self.write({'record_ids': [fields.Command.create({
                'field': record['field'],
                'data': record['data'],
                'model_name': record['model_name'],
                'model': record['model'],
                'record_id': record['id']
            })]})
