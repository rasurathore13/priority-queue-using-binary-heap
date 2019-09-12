import random

class Priority_Queue:
    def __init__(self):
        self.array = []

    def push(self, value):
        '''
        Min heap implementation for priority_queue where the smaller integere has higher priority
        '''
        self.array.append(value)
        i = len(self.array) - 1
        while i >= 1:
            flag = True
            parent = i//2 if i%2 != 0 else i//2-1
            if self.array[i] < self.array[parent]:
                self.array[i], self.array[parent] = self.array[parent], self.array[i]
                flag = False
            if flag:
                break
            i = parent
        
    def min_child(self, i):
        if 2*i+2 > len(self.array)-1:
            return 2*i+1
        else:
            if self.array[2*i+1] < self.array[2*i+2]:
                return 2*i+1
        return 2*i+2

    def pop(self):
        return_value = self.array[0]
        self.array[0] = self.array[-1]
        self.array = self.array[:-1]
        i = 0
        while 2*i+1 <= len(self.array) -1:
            flag = True
            mc = self.min_child(i)
            if self.array[i] > self.array[mc]:
                self.array[i], self.array[mc] = self.array[mc], self.array[i]
                flag = False
            if flag:
                break
            i = mc
        return return_value

    def __str__(self):
        return ','.join(str(i) for i in self.array)
    
    def __len__(self):
        return len(self.array)
    
if __name__ == '__main__':
    pq = Priority_Queue()
    arr = []
    while len(arr)!=10:
        while True:
            r = random.randint(1,100)
            if r not in arr:
                arr.append(r)
                break
    print(arr)
    for i in arr:
        pq.push(i)
    while True:
        try:
            print(pq.pop())
        except IndexError:
            break