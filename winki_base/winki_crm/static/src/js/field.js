odoo.define('winki_crm.field', function (require) {
    "use strict";

    var FormController = require('web.FormController');

    FormController.include({
        _render: function () {
            this._super.apply(this, arguments);
            this.$('input[data-required="true"]').addClass('o_custom_required');
        },
    });
});
