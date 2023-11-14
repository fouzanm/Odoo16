/** @odoo-module **/
import AbstractAwaitablePopup from 'point_of_sale.AbstractAwaitablePopup';
import Registries from 'point_of_sale.Registries';
const { useRef } = owl;

class CreateProductPopup extends AbstractAwaitablePopup {
    setup(){
        super.setup();
        this.imageURL = null;
    }
    createProduct(ev) {
        var productName = document.getElementById('product').value
        var productPrice = document.getElementById('price').value
        var productCost = document.getElementById('cost').value
        var productCategory = document.getElementById('category').value
        this.rpc({
            model: 'product.product',
            method: 'create',
            args: [{
                'name': productName,
                'lst_price': productPrice,
                'standard_price': productCost,
                'available_in_pos': true,
                'pos_categ_id': parseInt(productCategory),
                'image_1920': this.imageURL
            }]
        }).then(function (){
            window.location.reload();
        })
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
                image.style.display = 'flex';
                image.style.height = '100px';
                image.style.marginBottom = '10px';
                image.style.marginLeft = '160px';
                const productImageDiv = document.getElementById('product-image');
                console.log(productImageDiv)
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