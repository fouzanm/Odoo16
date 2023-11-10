# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    show_quantity = fields.Boolean(string="Instant Quantity", store=True)

    def set_values(self):
        result = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('show_quantity',
                                                         self.show_quantity)
        return result

    @api.model
    def get_values(self):
        result = super(ResConfigSettings, self).get_values()
        result['show_quantity'] = (self.env['ir.config_parameter'].sudo().
                                   get_param('show_quantity'))
        return result
