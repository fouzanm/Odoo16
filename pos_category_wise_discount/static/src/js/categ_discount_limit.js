/** @odoo-module **/
"use strict";
import ProductScreen from 'point_of_sale.ProductScreen';
import Registries from 'point_of_sale.Registries';

const CategoryDiscountLimit = (ProductScreen) => class CategoryDiscountLimit extends ProductScreen {
    setup() {
            super.setup();
        }
    async _onClickPay(){
        var orderlines = this.env.pos.get_order().get_orderlines()
        var selected_categ = this.env.pos.config.pos_categ_ids
        var discount_limit = this.env.pos.config.discount_limit
        var within_limit = true
        var categ = {}
        for (let i = 0; i < selected_categ.length; i++) {
            categ[selected_categ[i]] = 0;
        }
        if (this.env.pos.config.pos_categ_discount === true) {
            for (let i=0; i<orderlines.length; i++) {
                if (selected_categ.includes(orderlines[i].product.pos_categ_id[0])) {
                    let price = orderlines[i].price * orderlines[i].quantity
                    let discount_price = price * orderlines[i].discount / 100;
                    categ[orderlines[i].product.pos_categ_id[0]] += parseFloat(discount_price.toFixed(2));
                }
            }
            for (let i in categ){
                if ( categ[i] > discount_limit) {
                    within_limit = false
                    const { confirmed } = await this.showPopup('ErrorPopup', {
                    //Error pop when the discount exceeded than discount limit
                        title:this.env._t('Discount Limit Exceed'),
                        body: this.env._t(`Discount limit exceeded for the category ${this.env.pos.db.category_by_id[i].name}`)
                    })
                }
            }
        }
        if (within_limit === true){
            super._onClickPay(...arguments);
        }
    }
}
Registries.Component.extend(ProductScreen, CategoryDiscountLimit);
