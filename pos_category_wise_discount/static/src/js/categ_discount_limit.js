/** @odoo-module **/
import ProductScreen from 'point_of_sale.ProductScreen';
import Registries from 'point_of_sale.Registries';

const CategoryDiscountLimit = (ProductScreen) => class CategoryDiscountLimit extends ProductScreen {
    setup() {
            super.setup();
        }
    async _onClickPay(){
        var orderLines = this.env.pos.get_order().get_orderlines()
        var selectedCateg = this.env.pos.config.pos_categ_ids
        var discountLimit = this.env.pos.config.discount_limit
        var withinLimit = true
        var categ = {}
        for (let i = 0; i < selectedCateg.length; i++) {
            categ[selectedCateg[i]] = 0;
        }
        if (this.env.pos.config.pos_categ_discount === true) {
            for (let i=0; i<orderLines.length; i++) {
                if (selectedCateg.includes(orderLines[i].product.pos_categ_id[0])) {
                    let price = orderLines[i].price * orderLines[i].quantity
                    let discountPrice = price * orderLines[i].discount / 100;
                    categ[orderLines[i].product.pos_categ_id[0]] += parseFloat(discountPrice.toFixed(2));
                }
            }
            for (let i in categ){
                if ( categ[i] > discountLimit) {
                    withinLimit = false
                    const { confirmed } = await this.showPopup('ErrorPopup', {
                    //Error pop when the discount exceeded than discount limit
                        title:this.env._t('Discount Limit Exceed'),
                        body: this.env._t(`Discount limit exceeded for the category ${this.env.pos.db.category_by_id[i].name}`)
                    })
                }
            }
        }
        if (withinLimit){
            super._onClickPay(...arguments);
        }
    }
}
Registries.Component.extend(ProductScreen, CategoryDiscountLimit);
