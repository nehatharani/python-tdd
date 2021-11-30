class ValueTooSmallError(Exception):
    ''' Raise when value is less than Zero '''


    def __init__(self, num, message="Negative numbers are not supported!!"):
        self.num = num
        self.message = message
        super().__init__(self.message)
    
    def __str__(self) -> str:
        return f'{self.num} - {self.message}'
