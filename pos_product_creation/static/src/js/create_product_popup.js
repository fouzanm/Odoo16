/** @odoo-module **/
import AbstractAwaitablePopup from 'point_of_sale.AbstractAwaitablePopup';
import Registries from 'point_of_sale.Registries';

class CreateProductPopup extends AbstractAwaitablePopup {
    setup(){
        super.setup();
        this.imageURL = null;
    }
    async createProduct(ev) {
        if (!document.getElementById('product').value){
            await this.showPopup('ErrorPopup', {
                    title: this.env._t('Validation Error'),
                    body: this.env._t('Product will not be created without a name.'),
                });
        } else {
            this.rpc({
                model: 'product.product',
                method: 'create',
                args: [{
                    'name': document.getElementById('product').value,
                    'lst_price': document.getElementById('price').value,
                    'standard_price': document.getElementById('cost').value,
                    'available_in_pos': true,
                    'pos_categ_id': parseInt(document.getElementById('category').value),
                    'image_1920': this.imageURL
                }]
            }).then(function (){
                window.location.reload();
            })
        }

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
             reader.readAsDataURL(file);
        }
    }
}
CreateProductPopup.template = 'CreateProductPopup';
CreateProductPopup.defaultProps = {
    confirmText: 'Ok',
    cancelText: 'Cancel',
    title: 'Create Products',
    body: '',
};
Registries.Component.add(CreateProductPopup);