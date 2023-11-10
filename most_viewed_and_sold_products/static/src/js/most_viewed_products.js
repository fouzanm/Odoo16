odoo.define('most_viewed_products.viewed_products', function (require) {
    var PublicWidget = require('web.public.widget');
    var rpc = require('web.rpc');
    var core = require('web.core');
    var qweb = core.qweb;
    var Dynamic = PublicWidget.Widget.extend({
        selector: '.most_viewed_products',
        events: {
            'click .carousel-view-next': 'carouselViewedNext',
            'click .carousel-view-prev': 'carouselViewedPrev',
        },
        willStart: async function(){
            var self = this;
            await rpc.query({
                route: '/most_viewed_products',
            }).then((data) => {
                this.data = data;
            });
        },
        start: function() {
            var chunks = _.chunk(this.data, 4)
            chunks[0].is_active = true;
            this.$el.find('#viewed_products_carousel').html(
                qweb.render('most_viewed-and_sold_products.viewed_product_snippet_carousel', {
                    chunks
                })
            )
        },
        carouselViewedNext: function(event) {
            this.$(".viewed_products").carousel('next')
        },
        carouselViewedPrev: function(event) {
            this.$(".viewed_products").carousel('prev')
        },
    });
    PublicWidget.registry.most_viewed_products = Dynamic;
    return Dynamic;
});