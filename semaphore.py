class Semaphore:
    def __init__(self):
        self.isAvailable = True

    def acquire(self):
        if self.isAvailable:
            self.isAvailable = False
            return True
        return False

    def release(self):
        self.isAvailable = True
