# -*- coding: utf-8 -*-
from odoo import api, models


class ReportStockReport(models.AbstractModel):
    _name = 'report.stock_report.report_stock_report'
    _description = "Stock Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        """to pass values to template"""
        return {
            'doc_ids': docids,
            'doc_model': 'stock.report.wizard',
            'docs': self.env['stock.report.wizard'].browse(docids),
            'data': data,
        }
