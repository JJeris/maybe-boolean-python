import random

class MaybeBoolean:
    """Class for a 'Maybe' boolean."""
    
    def __init__(self):
        self.Maybe = bool(self.maybe())
        
    def maybe(self):
        Maybe = random.randint(0,1)
        return Maybe

# Maybe = MaybeBoolean()
# print(bool(Maybe._return_value()))
