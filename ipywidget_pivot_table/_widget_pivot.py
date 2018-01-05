
import ipywidgets as widgets
import pandas as pd


from traitlets import observe
from traitlets import Unicode, Dict, List, Int

from io import StringIO

from ._options import Pivot_Options


@widgets.register
class Pivot(widgets.DOMWidget):
    """An example widget."""
    _view_name = Unicode('PivotView').tag(sync=True)
    _model_name = Unicode('PivotModel').tag(sync=True)
    _view_module = Unicode('ipywidget-pivot-table').tag(sync=True)
    _model_module = Unicode('ipywidget-pivot-table').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)

    data = List([]).tag(sync=True)
    options_init = Dict({}).tag(sync=True)

    def __init__(self,
                 df_data=None,
                 options=None):
        """
        """
        super().__init__()

        if df_data is not None:
            arr = df_data.values.tolist()
            arr.insert(0, list(df_data.columns))
            self.data = arr

        if options is not None:
            if isinstance(options, dict):
                self.options_init = options
            if isinstance(options, Pivot_Options):
                self.options_init = options.to_dict()
