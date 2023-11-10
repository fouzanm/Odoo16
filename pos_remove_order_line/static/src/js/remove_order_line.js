/** @odoo-module **/
import Orderline from 'point_of_sale.Orderline';
import Registries from 'point_of_sale.Registries';
const RemoveButton = (Orderline) => class RemoveButton extends Orderline {
    removeButtonClick() {
//        button action for remove order line
        this.env.pos.get_order().remove_orderline(this.props.line)
    }
}
Registries.Component.extend(Orderline, RemoveButton);