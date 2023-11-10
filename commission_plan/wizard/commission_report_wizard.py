# -*- coding: utf-8 -*-
import io
import json
from odoo import fields, models
from odoo.tools import date_utils
try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter


class CommissionReportWizard(models.TransientModel):
    """to add fields and options to print commission report"""
    _name = 'commission.report.wizard'

    report_type = fields.Selection(selection=[('sale_team', 'Sale Team'),
                                              ('sale_person', 'Sale Person')])
    sale_person_id = fields.Many2one('res.users')
    sale_team_id = fields.Many2one('crm.team')

    def print_pdf(self):
        """to print report in pdf format"""
        query = """select so.name,rp.name as customer,ct.name as sale_team,
                resp.name as sale_person,cc.name as commission,cc.type,
                cc.revenue_type,so.amount_total as total,so.commission as amount
                from sale_order as so
                inner join crm_commission as cc on so.commission_plan_id = cc.id
                inner join crm_team as ct on so.team_id = ct.id
                inner join res_partner as rp on so.partner_id = rp.id
                inner join res_users as ru on so.user_id = ru.id
                inner join res_partner as resp on ru.partner_id = resp.id
                """
        if self.report_type == 'sale_team':
            query += f"""where so.team_id = {self.sale_team_id.id}"""
        elif self.report_type == 'sale_person':
            query += f"""where so.user_id = {self.sale_person_id.id}"""
        self.env.cr.execute(query)
        report = self.env.cr.dictfetchall()
        for record in report:
            record['type'] = record['type'].replace("_", " ").title()
            if record['revenue_type']:
                record['revenue_type'] = (record['revenue_type'].
                                          replace("_", " ").title())
        data = {'report': report,
                'type': self.report_type,
                'sale_team': self.sale_team_id.name,
                'sale_person': self.sale_person_id.name}
        if self.report_type:
            data['type'] = self.report_type.replace("_", " ").title()
        return self.env.ref('commission_plan.commission_report_view_action').\
            report_action(None, data=data)

    def print_xlsx(self):
        """to print report in xlsx format"""
        query = """select so.name,rp.name as customer,ct.name as sale_team,
                resp.name as sale_person,cc.name as commission,cc.type,
                cc.revenue_type,so.amount_total as total,so.commission as amount
                from sale_order as so
                inner join crm_commission as cc on so.commission_plan_id = cc.id
                inner join crm_team as ct on so.team_id = ct.id
                inner join res_partner as rp on so.partner_id = rp.id
                inner join res_users as ru on so.user_id = ru.id
                inner join res_partner as resp on ru.partner_id = resp.id
                """
        if self.report_type == 'sale_team':
            query += f"""where so.team_id = {self.sale_team_id.id}"""
        elif self.report_type == 'sale_person':
            query += f"""where so.user_id = {self.sale_person_id.id}"""
        self.env.cr.execute(query)
        report = self.env.cr.dictfetchall()
        for record in report:
            record['type'] = record['type'].replace("_", " ").title()
            if record['revenue_type']:
                record['revenue_type'] = (record['revenue_type'].
                                          replace("_", " ").title())
        data = {'report': report,
                'type': self.report_type}
        if self.report_type:
            data['type'] = self.report_type.replace("_", " ").title()
        return {
            'type': 'ir.actions.report',
            'data': {'model': 'commission.report.wizard',
                     'options': json.dumps(data,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Commission Report',
                     },
            'report_type': 'commission_xlsx',
        }

    def get_xlsx_report(self, data, response):
        """to add values and fields in sheet"""
        report_type = data['type']
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format(
            {'font_size': '12px', 'align': 'center'})
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        txt = workbook.add_format({'font_size': '10px', 'align': 'center'})
        sheet.merge_range('F2:M3', 'Commission Report', head)
        if report_type:
            sheet.merge_range('A6:B6', 'Report Type:', cell_format)
            sheet.merge_range('C6:D6', report_type, txt)
        sheet.merge_range('A8:B8', 'Sale Order', cell_format)
        sheet.merge_range('C8:D8', 'Customer', cell_format)
        sheet.merge_range('E8:F8', 'Sale Person', cell_format)
        sheet.merge_range('G8:H8', 'Sale Team', cell_format)
        sheet.merge_range('I8:J8', 'Commission Plan', cell_format)
        sheet.merge_range('K8:L8', 'Commission Type', cell_format)
        sheet.merge_range('M8:N8', 'Revenue Type', cell_format)
        sheet.merge_range('O8:P8', 'Total Amount', cell_format)
        sheet.merge_range('Q8:R8', 'Commission', cell_format)
        line = 9
        for record in data['report']:
            name = record['name']
            customer = record['customer']
            sale_person = record['sale_person']
            sale_team = record['sale_team']['en_US']
            commission = record['commission']
            commission_type = record['type']
            revenue_type = record['revenue_type']
            total = record['total']
            amount = record['amount']
            sheet.merge_range(f'A{line}:B{line}', name, txt)
            sheet.merge_range(f'C{line}:D{line}', customer, txt)
            sheet.merge_range(f'E{line}:F{line}', sale_person, txt)
            sheet.merge_range(f'G{line}:H{line}', sale_team, txt)
            sheet.merge_range(f'I{line}:J{line}', commission, txt)
            sheet.merge_range(f'K{line}:L{line}', commission_type, txt)
            sheet.merge_range(f'M{line}:N{line}', revenue_type, txt)
            sheet.merge_range(f'O{line}:P{line}', total, txt)
            sheet.merge_range(f'Q{line}:R{line}', amount, txt)
            line += 1
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
