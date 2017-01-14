
def time_now():
    """
    Get a date integer
    """
    return int(time.time())

def convert_ps_shortcode(short):
    return short.replace('_', '')

class Namespace:
    """
    A thing
    """
    def __init__(self, *args, **kwargs):
        self.COLON = ':'
        self.COMMA = ','
        self.SEMICOLON = ';'
        self.NEWLINE = '\n'
        self.SPACE = ' '
        self.TAB = '\t'
        self.SLASH = '/'
        self.LPARENS = '('
        self.RPARENS = ')'
        self.AT = '@'

        # Useful regexp phrases
        self.DOT = '.'
        self.ASTER = '*'

        self._args = args
        for arg in self._args:
            kwargs.update(arg.__dict__)
        self.__dict__.update(kwargs)

    def dict_from_dict(self):
        return {key: value for key, value in self.__dict__.items() if not key.startswith('_')}

    def __call__(self, output):
        return output.format(*self._args, **self.dict_from_dict())

    @classmethod
    def string(cls, astring, *args, **kwargs):
        for arg in args:
            kwargs.update(arg.__dict__)
        return cls(*args, **kwargs)(astring)

    @property
    def kwargs(self):
        return {key: value for key, value in self.__dict__.items() if key.islower() and not key.startswith('_')}

    @property
    def declared_kwargs(self):
        return {key: value for key, value in self.__dict__.items() if key.islower() and not key.startswith('_')}


    def __repr__(self):
        """
        VERY MEAGER WAY TO OUTPUT THIS DATA
        """
        return str({k: v for k, v in self.__dict__.items() if k!=k.upper() and not k.startswith('_')})

class ExpandingDict(dict):
    def update_and_append(self, d):
        for key in [k for k in d.keys() if isinstance(d[k], list)]:
            value = d[key]
            if not key in self:
                self[key] = []
            if not isinstance(self[key], list):
                raise AttributeError("Cannot append a list to a key ("'{}'") that isn't already a list for {}".format(key, self))
            self[key].extend(value)
            del d[key]
        self.update(d)

if __name__ == "__main__":

    this = ExpandingDict()
