/** @odoo-module **/
import PosComponent from 'point_of_sale.PosComponent';
import ProductScreen from 'point_of_sale.ProductScreen';
import {useListener} from "@web/core/utils/hooks";
import Registries from 'point_of_sale.Registries';
class ClearAllButton extends PosComponent {
    setup() {
        super.setup();
        useListener('click', this.clearAll);
    }
    async clearAll() {
//        button action for clear all order lines
        const order = this.env.pos.get_order();
        const orderlines = order.orderlines.slice();
        orderlines.forEach(function (line) {
            order.remove_orderline(line);
        });
    }
}
ClearAllButton.template = 'ClearAllButton';
ProductScreen.addControlButton({
    component: ClearAllButton,
    condition: function() {
        return this.env.pos;
    },
});
Registries.Component.add(ClearAllButton);