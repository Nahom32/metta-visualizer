class Edge:
    def __init__(self,**kwargs):
        self.edges = kwargs
    def __repr__(self):
        return f'{self.edges}'
    def __str__(self):
        return f'{self.edges}'
    def to_dict(self):
        return self.edges