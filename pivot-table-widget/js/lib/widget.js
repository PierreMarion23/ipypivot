var widgets = require('@jupyter-widgets/base');
var _ = require('lodash');
// var pivot_table = require('./pivot_table');
var $ = require("jquery");
require("jquery-ui-bundle");
require('./style.css');
var pivottable = require('pivottable');
var export_renderer = require('pivottable/dist/export_renderers.min.js');
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
	defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
		_model_name: 'PivotModel',
		_view_name: 'PivotView',
		_model_module: 'pivot-table-widget',
		_view_module: 'pivot-table-widget',
		_model_module_version: '0.1.0',
		_view_module_version: '0.1.0',
		value: 'Hello World',
		config : {},
		content_string: '',
		data : []
	})
});


// Custom View. Renders the widget model.
var PivotView = widgets.DOMWidgetView.extend({
	render: function () {
		window.my_view = this;
		window.jquery = $;
		window.el = this.el;
		console.log("Creating html");
		title = document.createElement("h3");
		title.setAttribute("class", "pivot-title")
		title.textContent = this.model.get("value")
		this.el.appendChild(title)
		
		var table = document.createElement("div")
		this.table = table;
		table.setAttribute("class", "pivotable")
		
		this.el.appendChild(table);

		var renderers = $.extend($.pivotUtilities.renderers, $.pivotUtilities.export_renderers);
		// window.renderers = renderers;

		// $(function(){	
		// 	$(table).pivotUI(	
		// 		[
		// 			{color: "blue", shape: "circle"},
		// 			{color: "red", shape: "triangle"}
		// 		],
		// 		{
		// 			renderers: renderers,
		// 			rows: ["color"],
		// 			cols: ["shape"]
		// 		}
		// 	);
		//  });
		this.config_changed();


		//window.table = table;
		var view = this;
		var jquery = $;

		var save_js_to_python = function(){
			alert('in save');
			let config = jquery(table).data("pivotUIOptions");
			window.config = config;
			window.view_in_save = view;
			let config_copy = JSON.parse(JSON.stringify(config));
			//delete some values which will not serialize to JSON
			delete config_copy["aggregators"];
			delete config_copy["renderers"];
			view.model.set({'value':'toto'});
			view.model.set({'config': config_copy})
			view.touch();
		};

		var export_table_content = function(){
			alert('in export table content');
			var temp_table = document.createElement("div");
			window.temp_table = temp_table;
			let config = jquery(table).data("pivotUIOptions");
			var config_copy = Object.assign({}, config);
			config_copy['rendererName'] = 'TSV Export'
			var data = view.model.get('data');
			jquery.when(
				jquery(function(){	
					jquery(temp_table).pivotUI(data, config_copy);
				})
			).then(function(){
				alert('in callback');
				// view.el.appendChild(temp_table);
				test = temp_table.children[0].children[2].children[1];
				console.log(temp_table.children[0].children[2].innerHTML)
				// delay the execution for one millisecond. Else does not work !
				setTimeout(function(){
					content_string = temp_table.children[0].children[2].children[1].children[0].innerHTML;
					console.log(content_string);
					window.view_in_time_out = view;
					view.model.set({'content_string': content_string});
					view.touch();
				}, 1);
				// content_string = temp_table.children[0].children[2].children[1].children[0].innerHTML;
				// console.log(content_string);
				// view.model.set({'content_string': content_string});
				// view.touch();
			});		
		};

		var restore_config = function(){
			view.config_changed();
		};

		var buttons = document.createElement("div")
		buttons.setAttribute("class", "pivot-buttons")

		button_save = document.createElement("button");
		button_save.addEventListener('click', save_js_to_python);
		button_save.innerHTML = 'Save table config'
		buttons.appendChild(button_save);

		button_restore = document.createElement("button");
		button_restore.addEventListener('click', restore_config);
		button_restore.innerHTML = 'Restore saved config'
		buttons.appendChild(button_restore);

		button_export = document.createElement("button");
		button_export.addEventListener('click', export_table_content);
		button_export.innerHTML = 'Export table content'
		buttons.appendChild(button_export);

		this.el.appendChild(buttons);

		this.model.on('change:config', this.config_changed, this);
		this.model.on('change:data', this.data_changed, this);
		// this.model.on('change:value', function(){alert('in value changed');}, this);
		// console.log(this.model);
	},

	

	config_changed: function () {
		alert('in config changed');
		var view = this;
		config = view.model.get('config');
		window.new_config = config;
		var renderers = $.extend($.pivotUtilities.renderers, $.pivotUtilities.export_renderers);
		config['renderers'] = renderers;
		var data = this.model.get("data");
		console.log(data);
		$(function(){	
			$(view.table).pivotUI(data, config, true);
		 });
	},

	data_changed: function () {
		alert('in data changed');
		var data = this.model.get("data");
		var config = this.model.get("config");
		// add renderers to the config JSON
		var renderers = $.extend($.pivotUtilities.renderers, $.pivotUtilities.export_renderers);
		config['renderers'] = renderers;
		var view = this;
		$(function(){	
			$(view.table).pivotUI(data, config, true);
		 });
	}
});


module.exports = {
	PivotModel: PivotModel,
	PivotView: PivotView
};

