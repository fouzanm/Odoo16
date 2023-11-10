# -*- coding: utf-8 -*-
from odoo import api, models


class WorkReport(models.AbstractModel):
    _name = 'report.daily_work_report.work_report'
    _description = "Work Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        return {
            'doc_ids': docids,
            'doc_model': 'work.report.wizard',
            'docs': self.env['work.report.wizard'].browse(docids),
            'data': data,
        }
