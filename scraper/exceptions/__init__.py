class EmptyFiltersError(Exception):
    def __init__(self):
        super().__init__()


class InvalidFilterException(Exception):
    def __init__(self):
        super().__init__()


class EmptyDataFrame(Exception):
    def __init__(self):
        super().__init__()
