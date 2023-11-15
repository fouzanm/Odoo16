/** @odoo-module **/
import PosComponent from 'point_of_sale.PosComponent';
import Registries from 'point_of_sale.Registries';
import { Gui } from 'point_of_sale.Gui';
const { onMounted } = owl;

class ProductListScreen extends PosComponent {
    setup() {
        super.setup();
        onMounted(() => {
            this.env.posbus.on('updateProductList', this, this.updateProductList)
        })
    }
    updateProductList(ev) {
        var editedProduct = (this.props.products).filter((proxy) => proxy.id === parseInt(ev.productId));
        editedProduct[0].display_name = ev.data.name
        editedProduct[0].lst_price = ev.data.lst_price
        if (ev.data.image_1920) {
            editedProduct[0].image = `data:image/jpeg;base64,${ev.data.image_1920}`
        }
        var posCategory = Object.values(this.env.pos.db.category_by_id).filter((obj) => obj.id === ev.data.pos_categ_id);
        editedProduct[0].pos_categ_id = Object.values(posCategory[0])
    }
    createProduct() {
        var category = Object.values(this.env.pos.db.category_by_id)
        Gui.showPopup("CreateProductPopup", {
            title: this.env._t('Create Product'),
            cancelText: this.env._t('Cancel'),
            confirmText: this.env._t('Create'),
            category: category
        })
    }
    editProduct(ev) {
        console.log(ev)
        console.log(this.props.products)
        var productId = ev.target.getAttribute('data-product-id')
        var product = (this.props.products).filter((proxy) => proxy.id === parseInt(productId));
        console.log(product)
        var category = Object.values(this.env.pos.db.category_by_id)
            Gui.showPopup("EditProductPopup", {
                title: this.env._t('Edit Product'),
                cancelText: this.env._t('Cancel'),
                confirmText: this.env._t('Edit'),
                selectedProduct: product,
                category: category
            })
    }
    back() {
        this.trigger('close-temp-screen');
    }
}
ProductListScreen.template = 'ProductListScreen';
Registries.Component.add(ProductListScreen);