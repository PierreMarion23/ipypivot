
import ipywidgets as widgets
import pandas as pd

from copy import deepcopy
from traitlets import observe
from traitlets import Unicode, Dict, List, Int

from io import StringIO

from ._options import PivotUI_Options
from ._widget_util import shape_df


@widgets.register
class PivotUI(widgets.DOMWidget):
    """An example widget."""
    _view_name = Unicode('PivotUIView').tag(sync=True)
    _model_name = Unicode('PivotUIModel').tag(sync=True)
    _view_module = Unicode('ipywidget-pivot-table').tag(sync=True)
    _model_module = Unicode('ipywidget-pivot-table').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)

    data = List([]).tag(sync=True)
    options = Dict({}).tag(sync=True)
    data_tsv = Unicode('Empty').tag(sync=True)
    counter = Int(0)

    @observe('data_tsv')
    def tsv_to_df(self, change):
        # print(change['old'])
        # print(change['new'])
        df_tsv = pd.read_csv(StringIO(self.data_tsv),
                             sep=r'\t',
                             lineterminator=r'\n',
                             engine='python')
        self.df_export = shape_df(df_tsv,
                                  self.options)

    def __init__(self,
                 df_data=None):
        """
        """
        super().__init__()
        self.options_object = PivotUI_Options(self)

        if df_data is not None:
            arr = df_data.values.tolist()
            arr.insert(0, list(df_data.columns))
            self.data = arr

    @observe('counter')
    def change_options_object(self, change):
        print('change counter')
        self.options = self.options_object.to_dict()

    @observe('options')
    def change_options_dic(self, change):
        print('change options')
        for key, value in self.options.items():
            if key not in ['aggregators', 'derivedAttributes', 'renderers', 'sorters', 'rendererOptions']:
                if key not in self.options_object.__dict__.keys() or getattr(self.options_object, key) != value:
                    object.__setattr__(self.options_object, key, value)
