import random

class MaybeBoolean:
    """Class for a 'Maybe' boolean."""
    
    def __init__(self):
        self.Maybe = bool(random.randint(0,1))