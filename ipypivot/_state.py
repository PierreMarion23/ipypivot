
import os
import json
from ._config import API_DIR, PIVOT_OPTION_FILE, PIVOTUI_OPTION_FILE


class State(object):
    """
    Contains all 'ezvis3d' API, options and methods
    """

    def __init__(self, src):
        """
        """
        self._OPTION = self._load_resource(src)

    def _load_resource(self, src):
        """
        """
        _dir = os.path.dirname(__file__)
        path = os.path.join(_dir, API_DIR, src)
        with open(path, 'r') as f:
            return json.load(f)


state_Pivot = State(PIVOT_OPTION_FILE)
state_PivotUI = State(PIVOTUI_OPTION_FILE)
