
'use script';

// var $ = require('jquery');
// require('jquery-ui-bundle');
// require('pivottable');
// require('pivottable/dist/export_renderers.min.js');
// require('pivottable/dist/c3_renderers.min.js');
// require('pivottable/dist/d3_renderers.min.js');

// require('./pivot-table.css');
require('./style.css');
// require('./c3.css');

var util = require('./util');


var React = require('react');
var PivotTableUI = require('react-pivottable/PivotTableUI');
var PivotTable = require('react-pivottable/PivotTable');
var ReactDOM = require('react-dom');
var TableRenderers = require('react-pivottable/TableRenderers');
var Plot = require('react-plotly.js');
var createPlotlyRenderers = require('react-pivottable/PlotlyRenderers');
require('react-pivottable/pivottable.css');

// create Plotly renderers via dependency injection
const PlotlyRenderers = createPlotlyRenderers(Plot);


var _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; };

class AppUI extends React.Component {
    constructor(props) {
        super(props);
		// this.state = props[0];
		this.data = props[0];
		this.state = props[1];
    }

    render() {
        return React.createElement(PivotTableUI, _extends({
			data: this.data,
			onChange: s => this.setState(s),
			renderers: Object.assign({}, TableRenderers, PlotlyRenderers)
        }, this.state));
    }
}

class App extends React.Component {
    constructor(props) {
        super(props);
		// this.state = props[0];
		this.data = props[0];
		this.state = props[1];
    }

    render() {
        return React.createElement(PivotTable, _extends({
			data: this.data,
			onChange: s => this.setState(s),
			renderers: Object.assign({}, TableRenderers, PlotlyRenderers)
        }, this.state));
    }
}


var createPivot = function (that) {
	console.log('ipypivot start createPivot');

	var divElmt = document.createElement('div');
	divElmt.setAttribute('width', '100%');	// useless?

	// append elmt to dom
	that.el.appendChild(divElmt);

	// add hook to divElmt
	that.tableElmt = divElmt;

	// set class
	that.el.setAttribute('class', 'jupyter-widget pivot-table');	// what for?

	// set mode='pivot' to indicate origin
	this.call_pivottablejs(that, 'pivot', 'create');

	console.log('end createPivot');
};

var createPivotUI = function (that) {
	console.log('ipypivot start createPivotUI');

	// create elmt
	var divElmt = document.createElement('div');
	divElmt.setAttribute('width', '100%');

	// append elmt to dom
	that.el.appendChild(divElmt);

	// add hook to divElmt
	that.tableElmt = divElmt;

	// set class
	that.el.setAttribute('class', 'jupyter-widget pivotui-table');

	// set mode='pivotui' to indicate origin
	this.call_pivottablejs(that, 'pivotui', 'create');

	console.log('end createPivotUI');
};


var call_pivottablejs = function (that, mode, intent) {
	// mode = 'pivot' - call from createPivot
	// mode = 'pivotui' - call from createPivotUI

	console.log('ipypivot PivotUIModel start call_pivottablejs');

	// get data from model
	let data = that.model.get('_data');

	// get options
	let options = that.model.get('_options');
	options = util.JSONPivotTable.parse(JSON.stringify(options));

	if (intent == 'update'){
		// react component rerenders automatically when the setState method is called
		that.react_object.setState((prevState, props) => {
			newState = Object.assign({}, prevState);
			Object.assign(newState, options);
			return newState;
		});
		if (mode == 'pivotui') {
			// save new options + rendered dataframe to model
			this.save_to_model(that);
		}
		return;
	}

	if (mode == 'pivot') {
		console.log('call pivot');
		element = ReactDOM.render(React.createElement(App, [data, options]), that.tableElmt);
		that.react_object = element;
	}
	if (mode == 'pivotui') {
		console.log('call pivotUI');
		element = ReactDOM.render(React.createElement(AppUI, [data, options]), that.tableElmt);
		that.react_object = element;
		// save new options + rendered dataframe to model
		this.save_to_model(that);
	}

	

	console.log('end call_pivottablejs');

	// debug
	window.that = that;
	window.$ = $;
	window.data = data;

};

var save_to_model = function (that) {

	console.log('ipypivot start save_to_model');

	// get data from model
	let data = that.model.get('_data');

	// deepcopy current pivotUI options
	options = Object.assign({}, that.react_object.state);

	// add only TSV export renderer
	optionsExport = Object.assign({}, options);
	optionsExport.rendererName = 'Exportable TSV'

	// create new elemt - which is never added to the dom
	var TsvTable = React.createElement(AppUI, [data, optionsExport]);
	tempDiv = document.createElement('div')
	element = ReactDOM.render(TsvTable, tempDiv);
	// extract tsv string
	data_tsv = tempDiv.getElementsByClassName("pvtOutput")[0].children[0].innerHTML;


	// delete attributes with functions because
	// (1) they won't be changed from JS side, so no need to pass them to Python
	// (2) anyway the functions are removed in the JS->Python link, so leaving the attributes without the
	// functions inside makes no sense
	delete options['aggregators'];
	delete options['renderers'];
	delete options['sorters'];
	delete options['derivedAttributes'];
	delete options['tableColorScaleGenerator'];
	delete options['onChange'];
	delete options['data']; // temporary ?

	console.log('update model');
	that.model.set({
		'_data_tsv': data_tsv,
		'_options': options
	});

	// that.model.save_changes();
	that.touch();

	console.log('end save_to_model');
};


var pivot_table = {
	createPivot: createPivot,
	createPivotUI: createPivotUI,
	call_pivottablejs: call_pivottablejs,
	save_to_model: save_to_model,
};

module.exports = pivot_table;

