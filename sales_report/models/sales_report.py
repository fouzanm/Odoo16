# -*- coding: utf-8 -*-
import base64
import datetime

from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models


class SalesReport(models.Model):
    _name = 'sales.report'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Report No:", readonly=True,
                       default=lambda self: _('New'), copy=False)
    customers_ids = fields.Many2many(comodel_name='res.partner',
                                     string='Customers', required=True)
    team_id = fields.Many2one(comodel_name='crm.team', string="Sales Team")
    period = fields.Selection(selection=[('weekly', 'Weekly'),
                                         ('monthly', 'Monthly')],
                              required=True)

    @api.model
    def create(self, vals):
        """to create sales report sequence"""
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'sales.report.number') or _('New')
        res = super(SalesReport, self).create(vals)
        return res

    def action_weekly_send_report(self):
        """action to send weekly sale report"""
        to_date = datetime.date.today()
        from_date = datetime.date.today() - relativedelta(days=7)
        for record in self.search([('period', '=', 'weekly')]):
            query = f"""select so.name, so.state, so.amount_total,
            so.date_order, rp.name as customer, st.name as team from
            sale_order as so 
            inner join res_partner as rp on rp.id = so.partner_id
            inner join crm_team as st on st.id = so.team_id
            where DATE(date_order) between '{from_date}' and '{to_date}'"""
            if record.team_id:
                query += f"""and st.id = {record.team_id.id}"""
            self.env.cr.execute(query)
            report = self.env.cr.dictfetchall()
            data = {'report': report,
                    'from_date': from_date.strftime('%b %d %Y'),
                    'to_date': to_date.strftime('%b %d %Y')}
            current_date = datetime.date.today().strftime('%b %d %Y')
            sales_report = self.env.ref(
                'sales_report.sales_report_pdf_action')
            data_record = base64.b64encode(
                self.env['ir.actions.report'].sudo()._render_qweb_pdf(
                    sales_report, data=data)[0])
            ir_values = {
                'name': "Weekly Sale Report",
                'type': 'binary',
                'datas': data_record,
                'store_fname': data_record,
                'mimetype': 'application/x-pdf',
                'res_id': record.id,
                'res_model': 'sales.report',
            }
            customers = [rec.email for rec in record.customers_ids]
            data_id = self.env['ir.attachment'].sudo().create(ir_values)
            mail_template = self.env.ref(
                'sales_report.sales_report_email_template')
            mail_template.attachment_ids = [fields.Command.set(data_id.ids)]
            email_values = {'email_to': customers[0],
                            'email_from': self.env.user.email,
                            'email_cc': customers[1:],
                            'subject': f'Weekly Sales Report {current_date}'}
            mail_template.send_mail(self.id, email_values=email_values,
                                    force_send=True)
            mail_template.attachment_ids = [fields.Command.unlink(data_id.id)]
            report_message = f"Weekly Sales Report sent on {current_date}"
            record.message_post(body=report_message, attachment_ids=data_id.ids)


    def action_monthly_send_report(self):
        """action to send monthly sale report"""
        to_date = datetime.date.today()
        from_date = datetime.date.today() - relativedelta(months=1)
        for record in self.search([('period', '=', 'monthly')]):
            query = f"""select so.name, so.state, so.amount_total,
            so.date_order, rp.name as customer, st.name as team from
            sale_order as so 
            inner join res_partner as rp on rp.id = so.partner_id
            inner join crm_team as st on st.id = so.team_id
            where DATE(date_order) between '{from_date}' and '{to_date}'"""
            if record.team_id:
                query += f"""and st.id = {record.team_id.id}"""
            self.env.cr.execute(query)
            report = self.env.cr.dictfetchall()
            data = {'report': report,
                    'from_date': from_date.strftime('%b %d %Y'),
                    'to_date': to_date.strftime('%b %d %Y')}
            current_date = datetime.date.today().strftime('%b %d %Y')
            sales_report = self.env.ref(
                'sales_report.sales_report_pdf_action')
            data_record = base64.b64encode(
                self.env['ir.actions.report'].sudo()._render_qweb_pdf(
                    sales_report, data=data)[0])
            ir_values = {
                'name': "Monthly Sale Report",
                'type': 'binary',
                'datas': data_record,
                'store_fname': data_record,
                'mimetype': 'application/x-pdf',
                'res_id': record.id,
                'res_model': 'sales.report',
            }
            customers = [rec.email for rec in record.customers_ids]
            data_id = self.env['ir.attachment'].sudo().create(ir_values)
            mail_template = self.env.ref(
                'sales_report.sales_report_email_template')
            mail_template.attachment_ids = [fields.Command.set(data_id.ids)]
            email_values = {'email_to': customers[0],
                            'email_from': self.env.user.email,
                            'email_cc': customers[1:],
                            'subject': f'Monthly Sales Report {current_date}'}
            mail_template.send_mail(self.id, email_values=email_values,
                                    force_send=True)
            mail_template.attachment_ids = [fields.Command.unlink(data_id.id)]
            report_message = f"Monthly Sales Report sent on {current_date}"
            record.message_post(body=report_message, attachment_ids=data_id.ids)
