
import ipywidgets as widgets
import pandas as pd
from copy import deepcopy


from traitlets import observe
from traitlets import Unicode, Dict, List, Int

from io import StringIO

from ._options import Pivot_Options


@widgets.register
class Pivot(widgets.DOMWidget):
    """An example widget."""
    _view_name = Unicode('PivotView').tag(sync=True)
    _model_name = Unicode('PivotModel').tag(sync=True)
    _view_module = Unicode('ipypivot').tag(sync=True)
    _model_module = Unicode('ipypivot').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)

    _data = List([]).tag(sync=True)
    _options = Dict({}).tag(sync=True)
    _counter = Int(0)

    def __init__(self,
                 df_data=None):
        """
        """
        super().__init__()
        self.options = Pivot_Options(self)

        if df_data is not None:
            arr = df_data.values.tolist()
            arr.insert(0, list(df_data.columns))
            self._data = arr

            self.df_data = df_data.copy()

    @observe('_counter')
    def change_options(self, change):
        # print('change')
        self._options = self.options.to_dict()
