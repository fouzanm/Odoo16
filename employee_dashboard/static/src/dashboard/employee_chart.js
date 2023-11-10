/* @odoo-module */
import {registry} from '@web/core/registry';
const { Component, useRef, onMounted } = owl;

export class EmployeeChart extends Component {
    setup() {
        this.chartRef = useRef("chart")
        this.charts = {}
        this.updateData = {}
        onMounted(() => {
            this.renderChart();
            this.env.bus.on('updateChart',this, this.updateChart)
        })
    }

    updateChart(ev) {
        this.updateData = {
            labels: ev.xdata,
            datasets: [{
                label: ev.label,
                backgroundColor: this.getRandomColor(this.props.xdata),
                data: ev.ydata
            }]
        }
        if (this.charts[ev.chart]) {
            this.charts[ev.chart].data = this.updateData;
            this.charts[ev.chart].update();
        }
    }

    renderChart() {
        if (this.props.type === 'bar') {
            var data = {
                type: this.props.type,
                data: {
                    labels: this.props.xdata,
                    datasets: [{
                        label: this.props.label,
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
            }
        } else {
            var data = {
                type: this.props.type,
                data: {
                    labels: this.props.xdata,
                    datasets: [{
                        backgroundColor: this.getRandomColor(this.props.xdata),
                        data: this.props.ydata
                    }]
                },
                options: {}
            }
        }
        this.charts[this.props.chart] = new Chart(this.chartRef.el, data)
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
EmployeeChart.template = 'employee_dashboard.EmployeeChart';
