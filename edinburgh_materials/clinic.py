"""
Messing around with AttrDict pattern, where dictionary keys are accessed as
though they were class attributes.

See: https://amir.rachum.com/blog/2016/10/05/python-dynamic-attributes/
"""

class Fruitbowl(dict):

    def count_fruit(self):
        return sum(self.values())

    def __repr__(self):
        contents = ', '.join([key + "=" + str(self[key]) for key in self])
        return 'Fruitbowl(' + contents + ')'

    def __getattr__(self, item):
        return self[item]

    def __dir__(self):
        return super().__dir__() + [str(k) for k in self.keys()]
