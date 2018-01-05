
from .__meta__ import version_info, __version__

from ._widget_box_pivot import Pivot_Box as Pivot
from ._widget_box_pivotui import PivotUI_Box as PivotUI
from ._options import Pivot_Options, PivotUI_Options
from ._sample import samples


def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'jupyter-widget-pivot-table',
        'require': 'jupyter-widget-pivot-table/extension'
    }]
