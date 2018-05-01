class Process:
    def __init__(self, pid, name ):
        self.pid=pid
        self.name=name
    def __eq__(self, otherid):
        return int(self.pid)==int(otherid.pid) and self.name == otherid.name

