class Node:
    def __init__(self,**kwargs):
        self.props = kwargs
    def __repr__(self):
        return f'{self.props}'
    def __str__(self):
        return f'{self.props}'
    def get_prop(self,prop_name):
        return self.props[prop_name]

        