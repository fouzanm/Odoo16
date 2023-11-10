# -*- coding: utf-8 -*-
from odoo import api, models


class CommissionReport(models.AbstractModel):
    _name = 'report.commission_plan.report_commission'
    _description = "Commission Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        return {
            'doc_ids': docids,
            'doc_model': 'commission.report.wizard',
            'docs': self.env['commission.report.wizard'].browse(docids),
            'data': data,
        }
