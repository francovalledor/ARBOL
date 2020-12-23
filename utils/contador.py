class Contador:
    total = 0

    @classmethod
    def inc(cls):
        cls.total += 1
    
    @classmethod
    def get(cls):
        return cls.total

    @classmethod
    def reset(cls):
        cls.total = 0