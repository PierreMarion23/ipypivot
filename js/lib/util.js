
'use strict';

// these lib may be used in functions input as string by user
var $ = require('jquery');
var c3 = require('c3');
var d3 = require('d3');
var Utilities = require('react-pivottable/Utilities')

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
		else if (valueCompact.substring(0, 9) == 'Utilities') {
			r = eval('(' + value + ')');
			return r;
		}
		else {
			return value;
		}
	});
};

var formatDate = function (d) {
	// var options = {
	// 	month: 'short',
	// 	day: 'numeric',
	// 	hour: '2-digit',
	// 	minute: '2-digit',
	// 	second: '2-digit'
	// };
	// return d.toLocaleDateString('en-US', options);

	var dateStr = d.getHours() + ':' + d.getMinutes() + ':' + d.getSeconds();
	return dateStr;
};


var util = {
	JSONPivotTable: JSONPivotTable,
	formatDate: formatDate
};

module.exports = util;