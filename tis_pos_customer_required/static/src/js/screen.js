odoo.define('tis_pos_customer_required.screens', function (require) {
"use strict";

var gui = require('point_of_sale.gui');
var screens = require('point_of_sale.screens');
var core = require('web.core');
var models = require('point_of_sale.models');
var QWeb = core.qweb;
var _t = core._t;

models.load_fields('product.product', ['type']);

screens.PaymentScreenWidget.include({

    order_is_valid: function(force_validation) {
        var self = this;
        var res = this._super(force_validation);

        var order = this.pos.get_order();

  if (self.pos.config.required_customer) {
        if(self.pos.config.type == 't_service'){
            var with_service = false;
            var orderlines = order.get_orderlines();
            for (var i = 0; i < orderlines.length; i++) {
                var orderline = orderlines[i];
                if (orderline.product.type == 'service'){
                    with_service = true;
                }
            }
            if ( with_service ) {
                if(!order.get_client()){
                    self.gui.show_popup('alert',{
                        'title': _t('Please select the Customer'),
                        'body': _t('Customer must be chosen for the order.'),
                        confirm: function(){
                            self.gui.show_screen('clientlist');
                           },
                        });
                    return false;
                    }
                  }
                  else{
            return res;
           }
         }
         else{
            if(!order.get_client()){
                 self.gui.show_popup('alert',{
                        'title': _t('Please select the Customer'),
                        'body': _t('Customer must be chosen for the order.'),
                        confirm: function(){
                            self.gui.show_screen('clientlist');
                        },
                    });
                return false;
                }
            }
        }
        return res;
    },
});

});
