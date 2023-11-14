/** @odoo-module **/
import PosComponent from 'point_of_sale.PosComponent';
import {useListener} from "@web/core/utils/hooks";
import Registries from 'point_of_sale.Registries';
import {session} from '@web/session';
import { Gui } from 'point_of_sale.Gui';
const { onWillUnmount, useRef } = owl;

class ProductListScreen extends PosComponent {
    setup() {
        super.setup();
        console.log('Product List')
//        useListener('click-save', () => this.env.bus.trigger('save-partner'));
//        useListener('save-changes', useAsyncLockedMethod(this.saveChanges));
//        this.searchWordInputRef = useRef('search-word-input-partner');
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
    back() {
        this.trigger('close-temp-screen');
    }
    editProduct(ev) {
        console.log("Ev", ev)
        console.log(this)
    }
}
ProductListScreen.template = 'ProductListScreen';
Registries.Component.add(ProductListScreen);