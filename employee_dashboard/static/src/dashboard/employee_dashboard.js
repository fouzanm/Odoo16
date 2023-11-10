/* @odoo-module */
import { EmployeeChart } from './employee_chart';
import { useService } from "@web/core/utils/hooks";
import { registry } from '@web/core/registry';
const { Component, useState, onWillStart } = owl;
export class EmployeeDashboard extends Component {
    setup() {
        this.orm = useService("orm");
        this.employee_data = {}
        this.selectedOption = 'attendance'
        onWillStart(async () => {
            await this.loadChartJs();
            await this.loadDashboardData();
        });

    }
    async loadChartJs() {
        if (typeof Chart !== 'undefined') {
            return Promise.resolve();
        } else {
            return new Promise(function (resolve) {
                var script = document.createElement('script');
                script.src = "https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.min.js";
                script.onload = resolve;
                document.head.appendChild(script);
            });
        }
    }
    async loadDashboardData() {
        const context = {};
        this.employee_data = await this.orm.call('employee.dashboard', 'get_data', [], {
                context: context
            }
        );
    }
    handleChartSelect(ev) {
        this.selectedOption = ev.target.value;
        if (this.selectedOption === 'attendance') {
            document.getElementById('chartHeading').textContent = 'Attendance'
            var xdata = this.employee_data.attendance_xdata
            var ydata = this.employee_data.attendance_ydata
            var label = '#workhours'
        } else {
            document.getElementById('chartHeading').textContent = 'Leave'
            var xdata = this.employee_data.leave_xdata
            var ydata = this.employee_data.leave_ydata
            var label = '#days'
        }
        this.env.bus.trigger('updateChart', {
            chart: 'attendance',
            xdata: xdata,
            ydata: ydata,
            label: label
        })
    }
}
registry.category("actions").add("employee_dashboard", EmployeeDashboard);
EmployeeDashboard.components = { EmployeeChart };
EmployeeDashboard.template = 'employee_dashboard.EmployeeDashboard';