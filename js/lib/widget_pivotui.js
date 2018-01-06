
'use strict';

var widgets = require('@jupyter-widgets/base');
var $ = require('jquery');
var pivot_table = require('./pivot-table');


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
		_model_name: 'PivotUIModel',
		_view_name: 'PivotUIView',
		_model_module: 'ipywidget-pivot-table',
		_view_module: 'ipywidget-pivot-table',
		_model_module_version: '~0.1.0',
		_view_module_version: '~0.1.0',
		data: [],
		options: {},
		options_init: {},
		counter_save: 0,
		counter_restore: 0,
		data_tsv: '',
	})
});

var PivotUIView = widgets.DOMWidgetView.extend({
	render: function () {

		console.log('jupyter-widget-pivot-table PivotUIModel start render');

		// explicit
		var that = this;

		// build pivottable and append it to dom
		pivot_table.createPivotUI(that);

		// event listener
		that.model.on('change:counter_save', that.counter_save_changed, that);
		that.model.on('change:counter_restore', that.counter_restore_changed, that);

		// debug
		// window.dom = that.el;
	},

	counter_save_changed: function () {

		console.log('jupyter-widget-pivot-table PivotUIModel start counter_save_changed');

		// explicit
		var that = this;

		// update
		pivot_table.counter_save_changed(that);
	},

	counter_restore_changed: function () {

		console.log('jupyter-widget-pivot-table PivotUIModel start counter_restore_changed');

		// explicit
		var that = this;

		// update
		pivot_table.counter_restore_changed(that);
	},

});

module.exports = {
	PivotUIModel: PivotUIModel,
	PivotUIView: PivotUIView
};

