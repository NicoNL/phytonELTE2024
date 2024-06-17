class Queue:
    def __init__(self):
        self.q = []
    def put(self,element):
        self.q.append(element)
    def get(self):
        if(len(self.q) == 0):  raise ValueError("Empty Queue")
        element = self.q[0]
        self.q.pop(0)
        return element

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except :
    print("Queue error")
    