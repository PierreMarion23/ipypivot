
import os
import json
import inspect

class subHelper:
    pass

class Helpers:
    """
    """

    def __init__(self):
        """
        """
        _dir = os.path.dirname(os.path.realpath(__file__))

        path = os.path.join(_dir, 'helpers.json')
        with open(path) as json_data:
            dic = json.load(json_data)

        for key, list_values in dic.items():
            subhelper = subHelper()
            for value in list_values:
                if key == 'aggregators':
                    string = self.toFunction(key, value)
                else:
                    string = self.toString(key, value)
                setattr(subhelper, value, string)
            setattr(self, key, subhelper)

    def function(self, name, *args):
        if len(args) > 0:
            return name + '(' + str(args[0]) + ')'
        return name + '()'

    def toFunction(self, key, value):
        value = value.replace('_', ' ').replace('EightyPercent', '80%')
        function_name = '$.pivotUtilities.' + key + '["' + value + '"]'
        return lambda *args: self.function(function_name, *args)
        
    def toString(self, key, value):
        value = value.replace('_', ' ').replace('EightyPercent', '80%')
        return '$.pivotUtilities.' + key + '["' + value + '"]'

helpers = Helpers()
