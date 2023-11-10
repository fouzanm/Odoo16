# -*- coding: utf-8 -*-
from odoo import api, models


class ReportSalesReport(models.AbstractModel):
    _name = 'report.sales_report.report_sales_report'
    _description = "Sales Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        """to pass values to template"""
        return {
            'doc_ids': docids,
            'doc_model': 'sales.report',
            'docs': self.env['sales.report'].browse(docids),
            'data': data,
        }
