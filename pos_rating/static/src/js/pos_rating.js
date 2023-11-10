/** @odoo-module **/
"use strict";
var { Orderline } = require('point_of_sale.models');
var Registries = require('point_of_sale.Registries');
const CustomOrderLine = (Orderline) => class CustomOrderLine extends Orderline {
    //    Extends the default Orderline to add quality rating information when exporting for printing.
    export_for_printing(){
        var result = super.export_for_printing(...arguments);
        result.quality_rating = this.get_product().quality_rating;
        return result;
    }
}
Registries.Model.extend(Orderline, CustomOrderLine)
