
from ._wrapper import Wrapper
from ._state import state_Pivot, state_PivotUI


class Pivot_Options(Wrapper):
    """
    Options for Pivot object

    Ref: https://github.com/nicolaskruchten/pivottable/wiki/Parameters#options-object-for-pivot
    """

    def __init__(self, pivot):
        Wrapper.__init__(self, state_Pivot)
        self._pivot = pivot

    def __setattr__(self, attr, value):
        object.__setattr__(self, attr, value)
        if attr != '_pivot' and attr != 'path' and attr != 'state':     # necessary to avoid errors
            self._pivot._counter += 1

    def __repr__(self):
        return str(self.to_dict())


class PivotUI_Options(Wrapper):
    """
    Options for Pivot object

    Ref: https://github.com/nicolaskruchten/pivottable/wiki/Parameters#options-object-for-pivotui
    """

    def __init__(self, pivot):
        Wrapper.__init__(self, state_PivotUI)
        self._pivot = pivot

    def __setattr__(self, attr, value):
        object.__setattr__(self, attr, value)
        if attr != '_pivot' and attr != 'path' and attr != 'state':     # necessary to avoid errors
            self._pivot._counter += 1

    def __repr__(self):
        return str(self.to_dict())
