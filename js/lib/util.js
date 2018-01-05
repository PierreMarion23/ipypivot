
'use strict';

// these lib may be used in functions input as string by user
var $ = require('jquery');
var c3 = require('c3');
var d3 = require('d3');

var JSONPivotTable = {};

JSONPivotTable.stringify = function (obj) {
	return JSON.stringify(obj, function (key, value) {
		return (typeof value === 'function') ? value.toString() : value;
	});
};

JSONPivotTable.parse = function (str) {
	return JSON.parse(str, function (key, value) {
		if (typeof value != 'string') return value;

		var valueCompact = value.replace(/\s+/g, '').replace(/\r?\n|\r/g, '');
		var r;

		if (valueCompact.substring(0, 8) == 'function') {
			// console.log('pos function - key: ' + key + ', value: ' + value);
			r = eval('(' + value + ')');
			// console.log('post eval');
			// console.log(r);
			return r;
		}
		else if (valueCompact.substring(0, 16) == '$.pivotUtilities') {
			r = eval('(' + value + ')');
			return r;
		}
		else if (valueCompact.substring(0, 8) == '$.extend') {
			r = eval('(' + value + ')');
			return r;
		}
		else {
			return value;
		}
	});
};


var util = {
	JSONPivotTable: JSONPivotTable
};

module.exports = util;