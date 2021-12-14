from datetime import datetime

class Timer():
    def __init__(self):
        dt = datetime.now()
        self.starttime = int(dt.timestamp() * 1000)
        return
    
    def start(self):
        dt = datetime.now()
        self.starttime = int(dt.timestamp() * 1000)
        return self.starttime
            
    def end(self):   
        dt = datetime.now()
        self.endtime = int(dt.timestamp() * 1000)
        return (self.endtime - self.starttime)

    
