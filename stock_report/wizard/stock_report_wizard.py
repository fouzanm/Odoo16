# -*- coding: utf-8 -*-
import base64
import datetime
import io
import xlsxwriter

from odoo import fields, models


class StockReportWizard(models.TransientModel):
    """to create stock report"""
    _name = 'stock.report.wizard'

    def stock_email_with_attachment(self):
        """action to send email with stock report"""
        query = """select pp.id, pt.name, pt.list_price, sq.quantity,
        sl.complete_name from product_template as pt
        inner join product_product as pp on pp.product_tmpl_id = pt.id
        inner join stock_quant as sq on sq.product_id = pp.id
        inner join stock_location as sl on sl.id = sq.location_id"""
        self.env.cr.execute(query)
        report = self.env.cr.dictfetchall()
        report = sorted(report, key=lambda x: x['complete_name'])
        data = {'report': report}
        current_date = datetime.date.today().strftime('%b %d %Y')
        report_type = self.env['ir.config_parameter'].sudo().get_param(
            'stock_report_type')
        stock_report = self.env['ir.config_parameter'].sudo().get_param(
            'stock_report')
        if stock_report:
            if report_type == 'pdf':
                stock_report = self.env.ref(
                    'stock_report.stock_report_pdf_action')
                data_record = base64.b64encode(
                    self.env['ir.actions.report'].sudo()._render_qweb_pdf(
                        stock_report, data=data)[0])
                ir_values = {
                    'name': "Stock Report",
                    'type': 'binary',
                    'datas': data_record,
                    'store_fname': data_record,
                    'mimetype': 'application/x-pdf',
                    'res_model': 'stock.report',
                }
            else:
                output = io.BytesIO()
                workbook = xlsxwriter.Workbook(output,
                                               {'in_memory': True})
                sheet = workbook.add_worksheet()
                cell_format = workbook.add_format(
                    {'font_size': '12px', 'align': 'center', 'bold': True})
                head = workbook.add_format(
                    {'align': 'center', 'bold': True, 'font_size': '20px'})
                txt = workbook.add_format({'font_size': '10px',
                                           'align': 'center'})
                sheet.merge_range('C2:I3', 'Stock Report', head)
                sheet.merge_range('B5:C5', 'Date', cell_format)
                sheet.merge_range('D5:E5', current_date, txt)
                sheet.write('B7', 'SI No', cell_format)
                sheet.merge_range('C7:E7', 'Product', cell_format)
                sheet.merge_range('F7:G7', 'Price', cell_format)
                sheet.merge_range('H7:I7', 'Quantity', cell_format)
                sheet.merge_range('J7:M7', 'Location', cell_format)
                line = 8
                item = 1
                for record in data['report']:
                    product = record['name']['en_US']
                    price = record['list_price']
                    quantity = record['quantity']
                    location = record['complete_name']
                    sheet.write(f'B{line}', item, txt)
                    sheet.merge_range(f'C{line}:E{line}', product, txt)
                    sheet.merge_range(f'F{line}:G{line}', price, txt)
                    sheet.merge_range(f'H{line}:I{line}', quantity, txt)
                    sheet.merge_range(f'J{line}:M{line}', location, txt)
                    line += 1
                    item += 1
                workbook.close()
                output.seek(0)
                ir_values = {
                    'name': 'Stock Report.xlsx',
                    'datas': base64.b64encode(output.read()),
                    'res_model': 'stock.report.wizard',
                    'res_id': self.id,
                }
                output.close()
            managers = self.env.ref('stock.group_stock_manager').users
            manager = [record.email for record in managers]
            data_id = self.env['ir.attachment'].sudo().create(ir_values)
            mail_template = self.env.ref(
                'stock_report.stock_report_email_template')
            mail_template.attachment_ids = [fields.Command.set(data_id.ids)]
            email_values = {'email_to': manager[0],
                            'email_from': self.env.user.email,
                            'email_cc': manager[1:],
                            'subject': f'Daily Stock Report {current_date}'}
            mail_template.send_mail(self.id, email_values=email_values,
                                    force_send=True)
            mail_template.attachment_ids = [fields.Command.unlink(data_id.id)]
