/** @odoo-module **/
import AbstractAwaitablePopup from 'point_of_sale.AbstractAwaitablePopup';
import Registries from 'point_of_sale.Registries';
const { useRef } = owl;
class CalculatorPopup extends AbstractAwaitablePopup {
    setup() {
        super.setup();
        this.input = useRef('calculator-input')
        this.dot = false;
        this.operators = ['+', '-', '*', '/']
        this.isResult = false;
        this.leftPart = 0;
    }
    ButtonPress(ev) {
        if (ev.target.tagName === 'IMG') {
            var button = ev.target.closest('.key.operator');
            if (button) {
                var value = button.value;
            }
        } else {
            var value = ev.target.value;
        }
        if (!isNaN(Number(value))) {
            if (this.input.el.value === '0') {
                this.input.el.value = value;
            } else {
                this.input.el.value += value
            }
            if (this.isResult) {
                this.input.el.value = value
                this.isResult = false
            }
        } else if (!this.dot && value === '.') {
            this.dot = true
            this.input.el.value += value
            if (this.isResult) {
                this.isResult = false
            }
        } else if ((this.operators).includes(value)) {
            this.total = Number(this.input.el.value)
            this.dot = false
            for (var i = 0; i < (this.input.el.value).length; i++) {
                if ((this.operators).includes((this.input.el.value).slice(-1))) {
                    this.input.el.value = this.input.el.value.slice(0,-1)
                } else {
                    break
                }
            }
            this.subTotal = eval(this.input.el.value)
            this.input.el.value += value
            this.leftPart = this.input.el.value
            if (this.isResult) {
                this.isResult = false
            }
        } else if (value === '%') {
            var percentage = 0
            for (var i = 0; i < (this.input.el.value).length; i++) {
                percentage += this.input.el.value[i]
                if ((this.operators).includes(this.input.el.value[i])) {
                    percentage = 0
                }
            }
            if (this.leftPart === 0) {
                this.input.el.value = this.input.el.value / 100
            } else {
                var result = this.subTotal *  Number(percentage) / 100
                this.input.el.value = this.leftPart + String(result)
            }
        } else if (value === '=') {
            for (var i = 0; i < (this.input.el.value).length; i++) {
                if ((this.operators).includes((this.input.el.value).slice(-1)) || (this.input.el.value).slice(-1) === '.') {
                    this.input.el.value = this.input.el.value.slice(0,-1)
                } else {
                    break
                }
            }
            var result = eval(this.input.el.value)
            this.input.el.value = result
            this.isResult = true
        } else if ( value === 'ac') {
            this.input.el.value = 0
            this.dot = false
            this.leftPart = 0
            this.subTotal = 0
        } else if ( value === 'clear') {
            if (this.input.el.value.slice(-1) === '.') {
                this.dot = this.dot = false
            }
            this.input.el.value = this.input.el.value.slice(0, -1)
        }
    }
}
CalculatorPopup.template = 'CalculatorPopupTemplate';
CalculatorPopup.defaultProps = {
    cancelText: 'Exit',
    title: 'Calculator',
    body: '',
};
Registries.Component.add(CalculatorPopup);