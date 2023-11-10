# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class DailyWorkReport(models.Model):
    _name = 'daily.work.report'
    _inherit = ['mail.thread']
    _description = 'Daily Work Report'

    name = fields.Char(string="Name")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    email = fields.Char(string="Email")
    date = fields.Date(string="Date")
    body = fields.Html(string="Content")

    @api.model
    def message_new(self, msg_dict, custom_values=None):
        self = self.with_context(default_user_id=False)
        if custom_values is None:
            custom_values = {}
        partner = msg_dict.get('author_id')
        for record in self.env['hr.employee'].sudo().search([]):
            domain = record.action_related_contacts()['domain']
            if partner in self.env['res.partner'].sudo().search(domain).ids:
                employee = record
        defaults = {
            'name': msg_dict.get('subject'),
            'email': msg_dict.get('from'),
            'employee_id': employee.id,
            'date': msg_dict.get('date'),
            'body': msg_dict.get('body')
        }
        defaults.update(custom_values)
        return super(DailyWorkReport, self).message_new(
            msg_dict, custom_values=defaults)

    @api.model
    def get_data(self):
        date = self._context.get('date')
        employee = self._context.get('employee')
        domain = [('date', '=', date)] if date else []
        if employee:
            employees = self.env['hr.employee'].sudo().browse(int(employee))
        else:
            employees = self.env['hr.employee'].sudo().search([])
        report = self.sudo().search(domain)
        xdata, ydata, data = [], [], []
        for record in employees:
            count = 0
            for rec in report:
                if record == rec.employee_id:
                    count += 1
            xdata.append(record.name)
            ydata.append(count)
        data = self.env['hr.employee'].sudo().search_read([])
        return {
            'xdata': xdata,
            'ydata': ydata,
            'data': data
        }
