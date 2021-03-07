class Counter:
    def __init__(self,time,startActive=False):
        self.startTime = time
        self.time = time if startActive else 0
    def update(self):
        self.time = max(0, self.time - 1)
    def reset(self,newStartTime = -1):
        if(newStartTime > 0):
            self.startTime = newStartTime
        self.time = self.startTime
    def done(self):
        return self.time <= 0
    def __bool__(self):
        return self.time > 0     