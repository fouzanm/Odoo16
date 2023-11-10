# -*- coding: utf-8 -*-
from odoo import api, models


class EmployeeDashboard(models.AbstractModel):
    _name = 'employee.dashboard'

    @api.model
    def get_data(self):
        """Returns data to the dashboard"""
        user = self.env.user.employee_id
        employee = self.env['hr.employee'].sudo().search([
            ('parent_id', '=', user.id)])
        employees = [record.name for record in employee]
        payslip = self.env['hr.payslip'].sudo().search([
            ('employee_id', 'in', (employee.ids + user.ids))])
        payslip_employee = list(set([record.employee_id.name
                                     for record in payslip]))
        payslip_xdata = []
        payslip_ydata = []
        payslip_line = [self.env['hr.payslip.line'].sudo().search([
            ('slip_id', '=', record.id), ('code', '=', 'NET')
        ]) for record in payslip]
        if employees:
            for record in payslip_employee:
                amount = 0
                for rec in payslip_line:
                    if record == rec.employee_id.name:
                        amount += rec.amount
                payslip_ydata.append(amount)
            payslip_xdata = payslip_employee
        else:
            for record in payslip_line:
                payslip_xdata.append(record.slip_id.number)
                payslip_ydata.append(record.amount)

        attendance = self.env['hr.attendance'].sudo().search([
            ('employee_id', 'in', (employee.ids + user.ids))])
        attendance_employee = list(set([record.employee_id.name
                                        for record in attendance]))
        work_hours = []
        for record in attendance_employee:
            total_hour = 0
            for rec in attendance:
                if record == rec.employee_id.name:
                    total_hour += rec.worked_hours
            work_hours.append(total_hour)
        leaves = self.env['hr.leave'].sudo().search([
            ('employee_id', 'in', (employee.ids + user.ids))])
        total_leave = []
        leave_employee = list(set([record.employee_id.name
                                   for record in leaves]))
        for record in leave_employee:
            total_days = 0
            for rec in leaves:
                if record == rec.employee_id.name:
                    total_days += rec.number_of_days
            total_leave.append(total_days)
        project = self.env['project.project'].sudo().search([
            ('user_id.employee_id', 'in', (employee.ids + user.ids))
        ])
        project_manager = list(set([record.user_id.name for record in project]))
        project_xdata = []
        project_ydata = []
        if employees:
            for record in project_manager:
                count = 0
                for rec in project:
                    if record == rec.user_id.name:
                        count += 1
                project_ydata.append(count)
            project_xdata = project_manager
        else:
            for record in project:
                project_xdata.append(record.name)
                task = [self.env['project.task'].sudo().search_count([
                    ('project_id', '=', record.id)
                ])]
                project_ydata.append(task)
        task = self.env['project.task'].sudo().search([])
        task_xdata = []
        task_ydata = []
        if employees:
            task_xdata = [record.name for record in project]
            for record in project:
                count = 0
                for rec in task:
                    if record.id == rec.project_id.id:
                        count += 1
                task_ydata.append(count)
        else:
            state = self.env['project.task.type'].search([])
            for record in state:
                count = 0
                for rec in task:
                    if rec.stage_id == record:
                        count += 1
                if count > 0:
                    task_xdata.append(record.name)
                    task_ydata.append(count)
        details = {
            'name': user.name,
            'mobile': user.work_phone,
            'email':  user.work_email,
            'department': user.department_id.name,
            'job': user.job_id.name,
            'parent_id': user.parent_id,
            'image': user.image_1920,
            'employees': employees
        }
        return {
            'payslip_xdata': payslip_xdata,
            'payslip_ydata': payslip_ydata,
            'attendance_xdata': attendance_employee,
            'attendance_ydata': work_hours,
            'leave_xdata': leave_employee,
            'leave_ydata': total_leave,
            'project_xdata': project_xdata,
            'project_ydata': project_ydata,
            'task_xdata': task_xdata,
            'task_ydata': task_ydata,
            'details': details,
        }
