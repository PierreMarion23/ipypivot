
from IPython.display import HTML, display

from ._config import NAME, TYPE, DEFAULT, DESCRIPTION
from ._state import State


class Wrapper(object):

    def __init__(self,
                 state,
                 path=''):
        self.path = path
        self.state = state

    def __getattr__(self, item):
        _path = item if not self.path else self.path + '.' + item
        for attr in self.state._OPTION:
            if _path == attr.get(NAME):
                var = Wrapper(_path)
                if len(dir(var)):
                    setattr(self, item, var)
                # setattr(self, item, var if len(dir(var)) else '')
                return var

    def __dir__(self):
        _dir = []
        _path = self.path.split('.')
        if len(_path) == 1 and self.path is '':
            for attr in self.state._OPTION:
                if len(attr.get(NAME).split('.')) == 1:
                    _dir.append(attr.get(NAME))
        else:
            for attr in self.state._OPTION:
                _attr_path = attr.get(NAME).split('.')
                if len(_path) < len(_attr_path):
                    if _path[len(_path) - 1] == _attr_path[len(_path) - 1] \
                            and len(_attr_path) == len(_path) + 1:
                        _dir.append(_attr_path[len(_path)])
        return _dir

    def to_dict(self):
        _dic = dict(self.__dict__)
        _dic.pop('path')
        _dic.pop('_pivot')

        for k in list(_dic.keys()):
            if isinstance(_dic[k], list):
                for i, e in enumerate(_dic[k]):
                    if isinstance(e, Wrapper):
                        _dic[k][i] = _dic[k][i].to_dict()
                    elif isinstance(e, dict):
                        pass
                    elif _dic[k][i] == {} or _dic[k][i] == None or isinstance(_dic[k][i], State):
                        _dic[k].pop(i)
            else:
                if isinstance(_dic[k], Wrapper):
                    _dic[k] = _dic[k].to_dict()
                elif isinstance(_dic[k], dict):
                    pass
                elif _dic[k] == {} or _dic[k] == None or isinstance(_dic[k], State):
                    _dic.pop(k)

        return _dic

    @property
    def __doc__(self):
        for attr in self.state._OPTION:
            if self.path == attr.get(NAME):
                _type = attr.get(TYPE)
                _default = attr.get(DEFAULT)
                _desc = attr.get(DESCRIPTION)
                break

        doc = "Documentation for '%s'\n\n" % self.path + \
            "Type\n%s\n\n" % _type + \
            "Default\n%s\n\n" % _default + \
            "Description\n%s\n\n" % _desc

        return doc

    def info(self):
        if self.path != '':
            for attr in self.state._OPTION:
                if self.path == attr.get(NAME):
                    _type = attr.get(TYPE)
                    _default = attr.get(DEFAULT)
                    _desc = attr.get(DESCRIPTION)
                    break

        doc = "<h4> Documentation for '%s' </h4><br>" % self.path + \
            "<li>Type </li>%s<br><br>" % _type + \
            "<li>Default </li>%s<br><br>" % _default + \
            "<li>Description </li>%s<br><br>" % _desc

        display(HTML(doc))

