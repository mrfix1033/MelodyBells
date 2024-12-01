class File:
    def __init__(self, path):
        self.path = path

    def open(self):
        return open(self.path)
