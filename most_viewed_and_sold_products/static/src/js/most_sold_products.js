odoo.define('most_sold_products.sold_products', function (require) {
    var PublicWidget = require('web.public.widget');
    var rpc = require('web.rpc');
    var core = require('web.core');
    var qweb = core.qweb;
    var Dynamic = PublicWidget.Widget.extend({
        selector: '.most_sold_products',
        events: {
            'click .carousel-sold-next': 'carouselSoldNext',
            'click .carousel-sold-prev': 'carouselSoldPrev',
        },
        willStart: async function(){
            var self = this;
            await rpc.query({
                route: '/most_sold_products',
            }).then((data) => {
                this.data = data;
            });
        },
        start: function() {
            var chunks = _.chunk(this.data, 4)
            chunks[0].is_active = true;
            this.$el.find('#sold_products_carousel').html(
                qweb.render('most_viewed-and_sold_products.sold_product_snippet_carousel', {
                    chunks
                })
            )
        },
        carouselSoldNext: function(event) {
            this.$(".sold_products").carousel('next')
        },
        carouselSoldPrev: function(event) {
            this.$(".sold_products").carousel('prev')
        },
    });
    PublicWidget.registry.most_sold_products = Dynamic;
    return Dynamic;
});