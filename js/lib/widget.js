
'use strict';

var pivot = require('./widget_pivot');
var pivotui = require('./widget_pivotui');
var pivotui_box = require('./widget_pivotui_box');


module.exports = {
	PivotModel: pivot.PivotModel,
	PivotView: pivot.PivotView,
	PivotUIModel: pivotui.PivotUIModel,
	PivotUIView: pivotui.PivotUIView,
	PivotUIBoxModel: pivotui_box.PivotUIBoxModel,
	PivotUIBoxView: pivotui_box.PivotUIBoxView
};

