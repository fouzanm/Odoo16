# -*- coding: utf-8 -*-
from odoo import fields, models


class WorkReportWizard(models.TransientModel):
    _name = 'work.report.wizard'

    employee_ids = fields.Many2many('hr.employee')
    date = fields.Date(string="Report Date")

    def print_pdf(self):
        """to print report in pdf format"""
        query = """select wr.name, he.name as employee, wr.email, wr.date, 
        wr.body from daily_work_report as wr inner join hr_employee as he on 
        he.id = wr.employee_id"""
        if self.employee_ids:
            employee = self.employee_ids.ids
            if len(employee) > 1:
                query += f""" where wr.employee_id in {tuple(employee)}"""
            else:
                query += f""" where wr.employee_id = {self.employee_ids.id}"""
            if self.date:
                query += f""" and DATE(wr.date) = '{self.date}'"""
        elif self.date:
            query += f""" where DATE(wr.date) = '{self.date}'"""
        self.env.cr.execute(query)
        report = self.env.cr.dictfetchall()
        data = {'report': report,
                'date': self.date}
        return self.env.ref('daily_work_report.work_report_action').\
            report_action(None, data=data)
