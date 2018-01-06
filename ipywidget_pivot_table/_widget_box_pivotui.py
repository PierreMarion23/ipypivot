
import os
import datetime as dt
import ipywidgets as widgets


from IPython.display import display, Markdown
from ipywidgets import Button, HTML, Layout, Box, HBox, VBox

from ._widget_pivotui import PivotUI


class PivotUI_Box:
    """
    """

    def __init__(self,
                 df_data=None,
                 options=None):
        """
        """
        self.table = PivotUI(df_data=df_data,
                             options=options)

        self.box = self._build_box(self.table)

    def show(self,
             verbose=False):
        if verbose:
            _dir = os.path.dirname(os.path.realpath(__file__))
            path = os.path.join(_dir, 'markdown', 'pivotui.md')
            with open(path, 'r') as f:
                md = f.read()
                display(Markdown(md))
        return self.box

    def save(self):
        self.table.counter_save += 1

    def restore(self):
        self.table.counter_restore += 1

    def _build_box(self, table):
        """
        """

        self.html = HTML(value='', layout=Layout(width='200px'))

        def on_save_clicked(b):
            table.counter_save += 1
            msg = 'Last Save: <b>{}</b>'
            msg = msg.format(self._now())
            self.html.value = msg

        def on_restore_clicked(b):
            table.counter_restore += 1

        button_save = Button(description='Save',
                             layout=Layout(width='100px'))
        button_save.on_click(on_save_clicked)

        button_restore = Button(description='Restore',
                                layout=Layout(width='100px'))
        button_restore.on_click(on_restore_clicked)

        items = [button_save, button_restore, self.html]

        box_layout = Layout(display='flex',
                            justify_content='space-around',
                            width='500px')
        controls = HBox(children=items,
                        layout=box_layout)

        items = [controls, table]

        box_layout = Layout(display='flex',
                            justify_content='flex-start',)
        self.box = VBox(children=items, layout=box_layout)

        # add timestamp
        on_save_clicked(None)

        return self.box

    @staticmethod
    def _now():
        """
        """
        return dt.datetime.now().strftime('%d %h %H:%M:%S')
