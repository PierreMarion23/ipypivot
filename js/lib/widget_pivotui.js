"use strict";

var widgets = require("@jupyter-widgets/base");
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

var PivotUIModel = widgets.DOMWidgetModel.extend({
  defaults: $.extend(widgets.DOMWidgetModel.prototype.defaults(), {
    _model_name: "PivotUIModel",
    _view_name: "PivotUIView",
    _model_module: "jupyter-widget-pivot-table",
    _view_module: "jupyter-widget-pivot-table",
    _model_module_version: "~0.1.0",
    _view_module_version: "~0.1.0",
    _data: [],
    _options: {},
    _data_tsv: ""
  })
});

var PivotUIView = widgets.DOMWidgetView.extend({
  render: function() {
    console.log("jupyter-widget-pivot-table PivotUIModel start render");

    // explicit
    var that = this;

    // build pivottable and append it to dom
    pivot_table.createPivotUI(that);

    // event listener
    that.model.on("change:_options", that.options_changed, that);

    // debug
    window.dom = that.el;
  },

  options_changed: function() {
    console.log("options changed");
    var that = this;
    pivot_table.call_pivottablejs(that, "pivotui", "update");
  }
});

module.exports = {
  PivotUIModel: PivotUIModel,
  PivotUIView: PivotUIView
};
