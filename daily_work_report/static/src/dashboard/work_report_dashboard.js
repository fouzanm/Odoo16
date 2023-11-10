/* @odoo-module */
import { useService } from "@web/core/utils/hooks";
import { registry } from '@web/core/registry';
import { WorkReportChart } from './work_report_chart';
const { Component, useState, onWillStart } = owl;
export class WorkReportDashboard extends Component {
    setup() {
        this.orm = useService("orm");
        this.workReportData = {};
        this.date = null;
        this.employee = null;
        onWillStart(async () => {
            await this.loadChartJs()
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
    async handleReportDate(ev) {
        this.date = ev.target.value
        await this.loadDashboardData();
        this.env.bus.trigger('updateWorkReport', {
            xdata: this.workReportData.xdata,
            ydata: this.workReportData.ydata,
        })
    }
    async handleChartEmployee(ev) {
        this.employee = ev.target.value
        await this.loadDashboardData();
        this.env.bus.trigger('updateWorkReport', {
            xdata: this.workReportData.xdata,
            ydata: this.workReportData.ydata,
        })
    }
    async loadDashboardData() {
        this.workReportData = await this.orm.call('daily.work.report', 'get_data', [], {
            context: {
                'date': this.date,
                'employee': this.employee
            }
        })
    };
}
registry.category("actions").add("work_report_dashboard", WorkReportDashboard);
WorkReportDashboard.components = { WorkReportChart };
WorkReportDashboard.template = 'daily_work_report.WorkReportDashboard';