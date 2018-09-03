class bunch(dict):
    # Create class container w/ arbitrary arguments!
    def __init__(self, *args, **kwds):
        super(bunch, self).__init__(*args, **kwds)
        self.__dict__ = self