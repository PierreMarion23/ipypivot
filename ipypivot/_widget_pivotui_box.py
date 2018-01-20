import os
import datetime as dt
import ipywidgets as widgets


from IPython.display import display, Markdown
from ipywidgets import Button, HTML, Layout, Box, HBox, VBox
from traitlets import Unicode

from ._widget_pivotui import PivotUI


class PivotUIBox(VBox):
    """PivotUI and save/restore buttons widget"""
    _view_name = Unicode('PivotUIBoxView').tag(sync=True)
    _model_name = Unicode('PivotUIBoxModel').tag(sync=True)
    _view_module = Unicode('ipypivot').tag(sync=True)
    _model_module = Unicode('ipypivot').tag(sync=True)

    def __init__(self,
                 df_data=None):
        """
        """
        self.table = PivotUI(df_data=df_data)
        self.buttons = self._build_buttons()
        super().__init__([self.buttons, self.table])

    def _build_buttons(self):
        """
        """

        self.button_save = Button(description='Save',
                                  layout=Layout(width='100px'))

        self.button_restore = Button(description='Restore',
                                     layout=Layout(width='100px'))

        self.status = widgets.Text(value='',
                                   disabled=True,
                                   layout=widgets.Layout(width='160px'))

        def on_save_clicked(b):
            self.status.value = 'Last Save: ' + self._now()

        self.button_save.on_click(on_save_clicked)

        items = [self.button_save, self.button_restore, self.status]

        box_layout = Layout(display='flex',
                            justify_content='space-around',
                            width='500px')
        buttons = HBox(children=items,
                       layout=box_layout)

        box_layout = Layout(display='flex',
                            justify_content='flex-start',)

        box = HBox(children=items, layout=box_layout)

        return box

    @staticmethod
    def _now():
        """
        """
        return dt.datetime.now().strftime('%H:%M:%S')
