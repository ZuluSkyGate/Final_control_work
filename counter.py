class Counter:
    def __init__(self):
        self.count = 0
        self.is_open = False

    def __enter__(self):
        self.is_open = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.is_open = False

    def add(self):
        if not self.is_open:
            raise RuntimeError("Counter must be used in a with statement")
        self.count += 1

    def get_count(self):
        return self.count