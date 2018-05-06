var ipypivot = require('./widget.js');
var jupyterlab_widgets = require('@jupyter-widgets/jupyterlab-manager');
var base = require('@jupyter-widgets/base');
var version = require('../package.json').version;

module.exports = {
  id: 'ipypivot',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'ipypivot',
          version: version,
          exports: ipypivot
      });
  },
  autoStart: true
};