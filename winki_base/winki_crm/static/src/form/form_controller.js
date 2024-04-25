/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";
import { Component, onWillStart, useEffect, useRef, onRendered, useState, toRaw } from "@odoo/owl";
import { useBus, useService } from "@web/core/utils/hooks";
import { useModel } from "@web/views/model";
import { SIZES } from "@web/core/ui/ui_service";

import { useViewButtons } from "@web/views/view_button/view_button_hook";
import { useSetupView } from "@web/views/view_hook";
import { useDebugCategory } from "@web/core/debug/debug_context";
import { usePager } from "@web/search/pager_hook";
import { isX2Many } from "@web/views/utils";
import { registry } from "@web/core/registry";
const viewRegistry = registry.category("views");


odoo.__DEBUG__ && console.log("Console log inside the patch function", FormController.prototype, "form_controller");

patch(FormController.prototype, "save",{
    setup() {
        this.props.preventEdit = this.env.inDialog ? false :true;
        this._super();


    },


    async edit(){
        this._super();
        if (!this.env.inDialog){
            await this.model.root.switchMode("edit");
        }
        else {
           await this.model.root.switchMode("readonly");
        }
    },

    async saveButtonClicked(params = {}){
        this._super();
        if (!this.env.inDialog){
            await this.model.root.switchMode("readonly");
        }
        else {
           this.model.actionService.doAction({type: 'ir.actions.act_window_close'});
        }
    },
    async discard(){
        this._super();
        if (!this.env.inDialog){
            await this.model.root.switchMode("readonly");
        }
        else {
           this.model.actionService.doAction({type: 'ir.actions.act_window_close'});
        }
    },
     async beforeLeave() {
        if (this.model.root.isDirty) {
            const confirmation = confirm("Bạn có chắc muốn rời khỏi mà không lưu lại?");
            if (!confirmation) {
                this.model.root.discard();
                return false;  // Ngăn chặn rời khỏi form nếu không đồng ý lưu
            }
        }
        return true;  // Cho phép rời khỏi form nếu không có thay đổi hoặc đã lưu
    }

})

