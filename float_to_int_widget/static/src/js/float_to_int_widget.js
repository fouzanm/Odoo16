/** @odoo-module **/
import { registry } from '@web/core/registry'
const { Component, useRef } = owl

class FloatToIntWidget extends Component {
    static template = 'FloatToIntFieldTemplate'
    setup() {
        super.setup();
        this.input = useRef('inputfloat')
    }
    onFloatToInt(ev){
        var inputValue = ev.target.value;
        if (!isNaN(inputValue)){
            var floatValue = parseFloat(inputValue);
            var roundValue = Math.round(floatValue);
            this.value = roundValue
            this.props.update(inputValue);
        }
    }
}
registry.category("fields").add("integer_widget", FloatToIntWidget);