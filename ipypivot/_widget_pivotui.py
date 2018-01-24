
import ipywidgets as widgets
import pandas as pd

from traitlets import observe
from traitlets import Unicode, Dict, List, Int

from io import StringIO

from ._options import PivotUI_Options
from ._widget_util import shape_df


# from IPython.display import display


@widgets.register
class PivotUI(widgets.DOMWidget):
    """PivotUI widget"""
    _view_name = Unicode('PivotUIView').tag(sync=True)
    _model_name = Unicode('PivotUIModel').tag(sync=True)
    _view_module = Unicode('ipypivot').tag(sync=True)
    _model_module = Unicode('ipypivot').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)

    _data = List([]).tag(sync=True)
    _options = Dict({}).tag(sync=True)
    _data_tsv = Unicode('Empty').tag(sync=True)
    _counter = Int(0)

    @observe('_data_tsv')
    def tsv_to_df(self, change):
        # print(change['old'])
        # print(change['new'])
        df_tsv = pd.read_csv(StringIO(self._data_tsv),
                             sep=r'\t',
                             lineterminator=r'\n',
                             engine='python')
        self.df_export = shape_df(df_tsv,
                                  self._options)
        # display(self.df_export)

    def __init__(self,
                 df_data=None):
        """
        """
        super().__init__()
        self.options = PivotUI_Options(self)

        if df_data is not None:
            arr = df_data.values.tolist()
            arr.insert(0, list(df_data.columns))
            self._data = arr

    @observe('_counter')
    def change_options(self, change):
        # print('change _counter')
        self._options = self.options.to_dict()

    @observe('_options')
    def change_options_dic(self, change):
        # print('change options')
        for key, value in self._options.items():
            if key not in ['aggregators', 'derivedAttributes', 'renderers', 'sorters', 'rendererOptions']:
                if key not in self.options.__dict__.keys() or getattr(self.options, key) != value:
                    object.__setattr__(self.options, key, value)
