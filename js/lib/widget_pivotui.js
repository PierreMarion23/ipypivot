
'use strict';

var widgets = require('@jupyter-widgets/base');
var ipywidgets = require('@jupyter-widgets/controls');
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



var PivotUIModel = widgets.DOMWidgetModel.extend({
	defaults: $.extend(widgets.DOMWidgetModel.prototype.defaults(), {
		_model_name: 'PivotUIModel',
		_view_name: 'PivotUIView',
		_model_module: 'jupyter-widget-pivot-table',
		_view_module: 'jupyter-widget-pivot-table',
		_model_module_version: '~0.1.0',
		_view_module_version: '~0.1.0',
		_data: [],
		_options: {},
		_data_tsv: '',
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
		that.model.on('change:_options', that.options_changed, that);


		// debug
		window.dom = that.el;
	},

	options_changed: function () {
		console.log('options changed');
		var that = this;
		pivot_table.call_pivottablejs(that, 'pivotui', 'update');
	},


});

var PivotBoxModel = ipywidgets.VBoxModel.extend({
	defaults: $.extend(ipywidgets.VBoxModel.prototype.defaults(), {
	})
});

var PivotBoxView = ipywidgets.VBoxView.extend({
	render:function(){
		console.log("START RENDERING")
		window.boxview = this; // debug
		ipywidgets.VBoxView.prototype.render.call(this); // call default render

		this.childrenviews = this.children_views.views;  // get children views
		// console.log(this.childrenviews);
		
		var that = this; // explicit
		this.childrenviews[1].then(function(view_pivot){
			that.view_pivot = view_pivot;
			var button_save_clicked = function () {
				console.log('jupyter-widget-pivot-table PivotUIModel start button_save_clicked');
				// save triggers all views rendering
				pivot_table.save_to_model(view_pivot);
			};
			var button_restore_clicked = function () {
				console.log('jupyter-widget-pivot-table PivotUIModel start button_restore_cliked');
				// call_pivottablejs
				pivot_table.call_pivottablejs(view_pivot, 'pivotui', 'update');
			};
			that.childrenviews[0].then(function(view_buttons){
				console.log("Hbox view found");
				console.log(view_buttons);
				view_buttons.children_views.views[0].then(function(button_save){
					console.log("Button save found")
					console.log(button_save)
					// add new event listener
					button_save.el.addEventListener('click', button_save_clicked)
				})
				view_buttons.children_views.views[1].then(function(button_restore){
					console.log("Button restore found")
					console.log(button_restore)
					// add new event listener
					button_restore.el.addEventListener('click', button_restore_clicked)
				})

			})
		})
	}
});

// debug
// console.log(PivotBoxModel)

module.exports = {
	PivotUIModel: PivotUIModel,
	PivotUIView: PivotUIView,
	PivotBoxModel: PivotBoxModel,
	PivotBoxView: PivotBoxView
};


