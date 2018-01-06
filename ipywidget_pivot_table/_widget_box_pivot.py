
import datetime as dt
import ipywidgets as widgets


from IPython.display import display
from ipywidgets import Button, HTML, Layout, Box, HBox, VBox

from ._widget_pivot import Pivot


class Pivot_Box:
    """
    """

    def __init__(self,
                 df_data=None,
                 options=None):
        """
        """
        self.table = Pivot(df_data=df_data,
                           options=options)

        self.box = self._build_box(self.table)

    def show(self):
        return self.box

    def _build_box(self, table):
        """
        """
        return self.table
