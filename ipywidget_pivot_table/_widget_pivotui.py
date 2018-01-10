
import ipywidgets as widgets
import pandas as pd

from copy import deepcopy
from traitlets import observe
from traitlets import Unicode, Dict, List, Int

from io import StringIO

from ._options import PivotUI_Options


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
    compteur = Int(0)

    @observe('data_tsv')
    def tsv_to_df(self, change):
        # print(change['old'])
        # print(change['new'])
        df_tsv = pd.read_csv(StringIO(self.data_tsv),
                             sep=r'\t',
                             lineterminator=r'\n',
                             engine='python')
        row_names = self.options['rows']
        col_names = self.options['cols']
        self.df_export = self._shape_df(df_tsv,
                                        row_names,
                                        col_names)

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

    @observe('compteur')
    def change_options_object(self, change):
        print('change compteur')
        self.options = self.options_object.to_dict()

    @observe('options')
    def change_options_dic(self, change):
        print('change options')
        for (key, value) in self.options.items():
            if key not in ['aggregators', 'derivedAttributes', 'renderers', 'sorters', 'rendererOptions']:
                if key not in self.options_object.__dict__.keys() or getattr(self.options_object, key) != value:
                    object.__setattr__(self.options_object, key, value)



    def _shape_df(self,
                  df,
                  row_names,
                  col_names):
        """
        """
        if row_names and col_names:
            df2 = df.set_index(row_names)

            row_idx = df2.index
            data = df2.values

            col_tuples = [tuple(e.split('-'))
                          for e in list(df.columns[len(row_names):])]

            col_idx = pd.MultiIndex.from_tuples(tuples=col_tuples,
                                                names=col_names)

            df_res = pd.DataFrame(data=data,
                                  index=row_idx,
                                  columns=col_idx)

        elif row_names and not col_names:
            df2 = df.set_index(row_names)

            df_res = pd.DataFrame(df2)

        elif not row_names and col_names:
            row_idx = df.index
            data = df.values

            col_tuples = [tuple(e.split('-'))
                          for e in list(df.columns)]

            col_idx = pd.MultiIndex.from_tuples(tuples=col_tuples,
                                                names=col_names)

            df_res = pd.DataFrame(data=data,
                                  index=row_idx,
                                  columns=col_idx)

        else:

            df_res = pd.DataFrame()

        return df_res
