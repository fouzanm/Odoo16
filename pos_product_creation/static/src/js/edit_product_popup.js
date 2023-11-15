/** @odoo-module **/
import AbstractAwaitablePopup from 'point_of_sale.AbstractAwaitablePopup';
import Registries from 'point_of_sale.Registries';

class EditProductPopup extends AbstractAwaitablePopup {
    setup(){
        super.setup();
        this.imageURL = null;
    }
    editProduct(ev) {
        var data = {
            'name': document.getElementById('product').value,
            'lst_price': document.getElementById('price').value,
            'available_in_pos': true,
            'pos_categ_id': parseInt(document.getElementById('category').value),
        }
        if (this.imageURL) {
            data.image_1920 = this.imageURL
        }
        var productId = parseInt(ev.target.getAttribute('data-product-id'))
        this.rpc({
            model: 'product.product',
            method: 'write',
            args: [productId, data]
        })
        this.env.posbus.trigger('updateProductList',{
            productId: productId,
            data: data
        })
        this.cancel();
    }
    cancel() {
        this.env.posbus.trigger('close-popup', {
            popupId: this.props.id,
            response: { confirmed: false, payload: null },
        });
    }
    uploadImage(ev) {
        var file = ev.target.files[0]
        if (file) {
            const reader = new FileReader();
            const self = this;
            reader.readAsDataURL(file);
            reader.onload = function (e) {
                var imageURL = e.target.result;
                self.imageURL = imageURL.split(',')[1];
                const image = new Image();
                image.src = imageURL;
                image.style.width = '100px';
                image.style.marginBottom = '10px';
                image.style.verticalAlign = 'middle';
                const productImageDiv = document.getElementById('product-image');
                productImageDiv.innerHTML = '';
                productImageDiv.appendChild(image);
            }
        }
    }
}
EditProductPopup.template = 'EditProductPopup';
EditProductPopup.defaultProps = {
    confirmText: 'Ok',
    cancelText: 'Cancel',
    title: 'Edit Products',
    body: '',
};
Registries.Component.add(EditProductPopup);