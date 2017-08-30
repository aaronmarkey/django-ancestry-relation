class StructuredNode:
    '''
    A simple object to store data in a heirarchical manner.


    '''
    def __init__(self, data, children=[]):
        '''
        data is any object.
        children is a list of objects matching the type of data.
        '''
        self.data = data
        self.children = children
