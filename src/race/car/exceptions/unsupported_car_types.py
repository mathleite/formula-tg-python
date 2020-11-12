class UnsupportedCarTypes(Exception):
    def __init__(self):
        super().__init__('Unsupported car type!')
