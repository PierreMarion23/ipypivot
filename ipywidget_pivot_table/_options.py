
from ._wrapper import Wrapper
from ._state import state_Pivot, state_PivotUI


class Pivot_Options(Wrapper):
    """
    Options for Pivot object

    Ref: https://github.com/nicolaskruchten/pivottable/wiki/Parameters#options-object-for-pivot
    """

    def __init__(self):
        Wrapper.__init__(self, state_Pivot)

class PivotUI_Options(Wrapper):
    """
    Options for Pivot object

    Ref: https://github.com/nicolaskruchten/pivottable/wiki/Parameters#options-object-for-pivotui
    """

    def __init__(self):
        Wrapper.__init__(self, state_PivotUI)

