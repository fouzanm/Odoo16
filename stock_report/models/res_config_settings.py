# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    """to add field in settings"""
    _inherit = 'res.config.settings'

    stock_report = fields.Boolean(default=False)
    stock_report_type = fields.Selection(selection=[('pdf', 'PDF'),
                                                    ('xlsx', 'XLSX')])

    def set_values(self):
        result = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'stock_report', self.stock_report)
        self.env['ir.config_parameter'].sudo().set_param(
            'stock_report_type', self.stock_report_type)
        return result

    @api.model
    def get_values(self):
        result = super(ResConfigSettings, self).get_values()
        result['stock_report'] = (self.env['ir.config_parameter'].sudo().
                                  get_param('stock_report'))
        result['stock_report_type'] = (self.env['ir.config_parameter'].sudo().
                                       get_param('stock_report_type'))
        return result
