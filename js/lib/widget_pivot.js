
'use strict';

var widgets = require('@jupyter-widgets/base');
var $ = require('jquery');
var pivot_table = require('./pivot-table');
var util = require('./util');
require('./style.css');


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



var PivotModel = widgets.DOMWidgetModel.extend({
	defaults: $.extend(widgets.DOMWidgetModel.prototype.defaults(), {
		_model_name: 'PivotModel',
		_view_name: 'PivotView',
		_model_module: 'ipypivot',
		_view_module: 'ipypivot',
		_model_module_version: '~0.1.0',
		_view_module_version: '~0.1.0',
		_data: [],
		_options: {},
	})
});

var PivotView = widgets.DOMWidgetView.extend({
	render: function () {

		console.log('ipypivot PivotModel start render');

		// explicit
		var that = this;

		// build pivottable and append it to dom
		pivot_table.createPivot(that);

		// event listener
		that.model.on('change:_options', that.options_changed, that);

		var message = document.createElement('div');
		message.className = 'last-saved';
		message.innerHTML = 'Last Save ' + util.formatDate(new Date());
		this.message = message;

		this.el.insertBefore(message, this.el.firstChild);

		// debug
		// window.dom = that.el;
	},

	options_changed: function () {
		console.log('options changed');
		var that = this;
		that.message.innerHTML = 'Last Save ' + util.formatDate(new Date());
		pivot_table.call_pivottablejs(that, 'pivot', 'update');
	},
});

module.exports = {
	PivotModel: PivotModel,
	PivotView: PivotView
};

