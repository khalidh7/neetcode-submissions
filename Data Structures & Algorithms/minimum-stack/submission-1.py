class MinStack:

    def __init__(self):
        self.temp = []
        self.mininum = []

    def push(self, val: int) -> None:
        self.temp.append(val)
        if len(self.mininum) == 0:
            self.mininum.append(val)
        elif val < self.mininum[-1]:
            self.mininum.append(val)
        else:
            self.mininum.append(self.mininum[-1])


    def pop(self) -> None:
        self.temp.pop()
        self.mininum.pop()
        return

    def top(self) -> int:
        return self.temp[len(self.temp)-1]

    def getMin(self) -> int:
        return self.mininum[len(self.mininum)-1]
