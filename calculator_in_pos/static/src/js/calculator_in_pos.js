/** @odoo-module **/
import PosComponent from 'point_of_sale.PosComponent';
import ProductScreen from 'point_of_sale.ProductScreen';
import {useListener} from "@web/core/utils/hooks";
import Registries from 'point_of_sale.Registries';
import { Gui } from 'point_of_sale.Gui';

class CalculatorInPos extends PosComponent {
    setup() {
        super.setup();
        useListener('click', this.calculator)
    }
    async calculator() {
        Gui.showPopup("CalculatorPopup", {});
    }
}
CalculatorInPos.template = 'PosCalculator'
ProductScreen.addControlButton({
    component: CalculatorInPos,
    condition: function() {
        return this.env.pos;
    }
});
Registries.Component.add(CalculatorInPos);