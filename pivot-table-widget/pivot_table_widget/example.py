import ipywidgets as widgets
from traitlets import Unicode, Float, Dict, observe, List
import pandas as pd
import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

@widgets.register
class PivotTable(widgets.DOMWidget):
    """An example widget."""
    _view_name = Unicode('PivotView').tag(sync=True)
    _model_name = Unicode('PivotModel').tag(sync=True)
    _view_module = Unicode('pivot-table-widget').tag(sync=True)
    _model_module = Unicode('pivot-table-widget').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)
    value = Unicode('My table').tag(sync=True)
    # data_x = List([]).tag(sync=True)
    # data_y = List([]).tag(sync=True)
    # time = List([]).tag(sync=True)
    config = Dict([]).tag(sync=True)
    content_string = Unicode('No content yet.').tag(sync=True)
    data = List([{"color":"blue", "shape" : "circle"}, {"color" : "red", "shape" : "triangle"}]).tag(sync=True)

    @observe('content_string')
    def content_string_to_df(self, change):
        print(change['old'])
        print(change['new'])
        self.content_df = pd.read_csv(StringIO(self.content_string), sep=r'\t', lineterminator=r'\n', engine='python')

    def __init__(self, df=None):
        super().__init__()
        if df is not None:
            self.data = df.to_dict(orient="records")



