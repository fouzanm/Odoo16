/** @odoo-module **/
import PosComponent from 'point_of_sale.PosComponent';
import ProductScreen from 'point_of_sale.ProductScreen';
import {useListener} from "@web/core/utils/hooks";
import Registries from 'point_of_sale.Registries';

class ProductButton extends PosComponent {
    setup() {
        super.setup();
        useListener('click', this.onClickProducts);
    }
    async onClickProducts() {
        var products = Object.values(this.env.pos.db.product_by_id)
        products.sort((a, b) => a.display_name.localeCompare(b.display_name))
        for (const product of products) {
            product.image = `/web/image?model=product.product&field=image_128&id=${product.id}&unique=${product.__last_update}`;
        }
        const productList = await this.showTempScreen('ProductListScreen', {'products': products})
    }
}
ProductButton.template = 'ProductButton';
ProductScreen.addControlButton({
    component: ProductButton,
    condition: function() {
        return this.env.pos;
    }
});
Registries.Component.add(ProductButton);