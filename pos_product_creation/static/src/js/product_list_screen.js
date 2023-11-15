/** @odoo-module **/
import PosComponent from 'point_of_sale.PosComponent';
import Registries from 'point_of_sale.Registries';
import { Gui } from 'point_of_sale.Gui';
const { onMounted, useRef } = owl;

class ProductListScreen extends PosComponent {
    setup() {
        super.setup();
        this.state = { query : null };
        this.searchWordInputRef = useRef('search-word-input-product');
        onMounted(() => {
            this.env.posbus.on('updateProductList', this, this.updateProductList)
        })
    }
    updateProductList(ev) {
        console.log('1')
        var editedProduct = (this.props.products).filter((proxy) => proxy.id === parseInt(ev.productId));
        editedProduct[0].display_name = ev.data.name
        editedProduct[0].lst_price = ev.data.lst_price
        console.log('2')
        if (ev.data.image_1920) {
            editedProduct[0].image = `data:image/jpeg;base64,${ev.data.image_1920}`
        }
        console.log('3')
        if(ev.data.pos_categ_id) {
            var posCategory = Object.values(this.env.pos.db.category_by_id).filter((obj) => obj.id === ev.data.pos_categ_id);
            editedProduct[0].pos_categ_id = Object.values(posCategory[0])
        }
        console.log('4')

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
        var productId = ev.target.getAttribute('data-product-id')
        var product = (this.props.products).filter((proxy) => proxy.id === parseInt(productId));
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
    async updateSuggestProduct(ev) {
        this.state.query = ev.target.value;
        const result = await this.searchProducts();
    }
    _clearSearch() {
        this.searchWordInputRef.el.value = null
        this.state.query = null
        this.searchProducts();
    }
    searchProducts() {
        const products = this.props.products
        const searchFields = ["display_name", "default_code", "pos_categ_id"];
        for (const item of Object.entries(products)) {
            let filteredProduct = false
            for (const field of searchFields) {
                const key = field === 'pos_categ_id' ? item[1][field][1] : item[1][field];
                if(key && this.state.query && (key.toLowerCase()).includes((this.state.query).toLowerCase())) {
                    filteredProduct = true;
                }
            }
            if (filteredProduct || !this.state.query) {
                const trElement = document.getElementById(item[1]['id'])
                trElement.style.display = '';
            } else {
                 const trElement = document.getElementById(item[1]['id'])
                 trElement.style.display = 'none';
            }
        }
    }
}
ProductListScreen.template = 'ProductListScreen';
Registries.Component.add(ProductListScreen);