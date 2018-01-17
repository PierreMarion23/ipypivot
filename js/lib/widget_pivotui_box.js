"use strict";

var ipywidgets = require("@jupyter-widgets/controls");
var $ = require("jquery");
var pivot_table = require("./pivot-table");
require("./style.css");

// Custom Model. Custom widgets models must at least provide default values
// for model attributes, including
//
//  - `_view_name`
//  - `_view_module`
//  - `_view_module_version`
//
//  - `_model_name`
//  - `_model_module`
//  - `_model_module_version`
//
//  when different from the base class.

// When serialiazing the entire widget state for embedding, only values that
// differ from the defaults will be specified.

var PivotUIBoxModel = ipywidgets.VBoxModel.extend({
  defaults: $.extend(ipywidgets.VBoxModel.prototype.defaults(), {})
});

var PivotUIBoxView = ipywidgets.VBoxView.extend({
  render: function() {
    console.log("ipypivot PivotUIModel start render");

    window.boxview = this; // debug
    ipywidgets.VBoxView.prototype.render.call(this); // call default render
    this.childrenviews = this.children_views.views; // get children views

    var buttons = this.childrenviews[0];
    var pivot = this.childrenviews[1];

    var that = this; // explicit

    pivot.then(function(view_pivot) {
      that.view_pivot = view_pivot;

      var button_save_clicked = function() {
        console.log(
          "ipypivot PivotUIModel start button_save_clicked"
        );
        // save triggers all views rendering
        pivot_table.save_to_model(view_pivot);
      };

      var button_restore_clicked = function() {
        console.log(
          "ipypivot PivotUIModel start button_restore_cliked"
        );
        // call_pivottablejs
        pivot_table.call_pivottablejs(view_pivot, "pivotui", "update");
      };

      buttons.then(function(view_buttons) {
        view_buttons.children_views.views[0].then(function(button_save) {
          // add new event listener
          button_save.el.addEventListener("click", button_save_clicked);
        });

        view_buttons.children_views.views[1].then(function(button_restore) {
          // add new event listener
          button_restore.el.addEventListener("click", button_restore_clicked);
        });
      });
    });
  }
});

module.exports = {
  PivotUIBoxModel: PivotUIBoxModel,
  PivotUIBoxView: PivotUIBoxView
};
