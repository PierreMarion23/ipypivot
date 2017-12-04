from .__meta__ import version_info, __version__

from .example import *
from .widget import *

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'pivot-table-widget',
        'require': 'pivot-table-widget/extension'
    }]
