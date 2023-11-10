/* @odoo-module */
import {registry} from '@web/core/registry';
const { Component, useRef, onMounted } = owl;

export class WorkReportChart extends Component {
    setup() {
        this.chartRef = useRef("chart")
        this.chart = null
        onMounted(() => {
            this.renderChart();
            this.env.bus.on('updateWorkReport', this, this.updateChart)
        })
    }
    updateChart(ev) {
        this.chart.data = {
            labels: ev.xdata,
            datasets: [{
                label: '#workreport',
                backgroundColor: this.getRandomColor(this.props.xdata),
                data: ev.ydata
            }]};
        this.chart.update();
    }
    renderChart() {
        this.chart = new Chart (this.chartRef.el, {
            type: 'bar',
            data: {
                labels: this.props.xdata,
                datasets: [{
                    label: '#workreport',
                    backgroundColor: this.getRandomColor(this.props.xdata),
                    data: this.props.ydata
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        })
    }
    getRandomColor(data) {
        var colors = [];
        function generateRandomHexColor() {
            const letters = "0123456789ABCDEF";
            let color = "#";
            for (let i = 0; i < 6; i++) {
                color += letters[Math.floor(Math.random() * 16)];
            }
            return color;
        }
        data.forEach(function () {
            colors.push(generateRandomHexColor());
        });
        return colors;
    }
}
WorkReportChart.template = 'daily_work_report.WorkReportChart';
