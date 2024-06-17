class CountingStack():
    def __init__(self):
        self.stk = []
        self.cnt = 0

    def push(self, val):
        self.stk.append(val)

    def pop(self):
        val = self. stk[-1]
        del self. stk[-1]
        self.cnt += 1
        return val

    def get_counter(self):
        return self.cnt

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()

print(stk.get_counter())