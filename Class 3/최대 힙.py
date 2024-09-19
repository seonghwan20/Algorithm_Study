import sys

input = sys.stdin.readline

class Heap:
    def __init__(self):
        self.heap_array = list()
        self.heap_array.append(None)
        
    def swap(self, arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
    
    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)

        self.heap_array.append(data)
        
        self.idx = len(self.heap_array) - 1
        
        while True:
            if self.idx == 1:
                break
            elif self.heap_array[self.idx//2] < self.heap_array[self.idx]:
                self.swap(self.heap_array, self.idx//2, self.idx)
                self.idx //= 2
            else:
                break
            
    def pop(self):
        print(self.heap_array[1])
        self.swap(self.heap_array, 1, -1)
        self.heap_array.pop(-1)
        
        self.idx = 1
        
        while True:
            if self.idx*2 > len(self.heap_array) - 1:
                break
            if self.idx*2 + 1 > len(self.heap_array) - 1:
                if self.heap_array[self.idx] < self.heap_array[self.idx*2]:
                    self.swap(self.heap_array, self.idx, self.idx*2)
                    self.idx *= 2
                else:
                    break
            else:    
                if self.heap_array[self.idx] < self.heap_array[self.idx*2] and self.heap_array[self.idx] < self.heap_array[self.idx*2 + 1]:
                    if self.heap_array[self.idx*2] > self.heap_array[self.idx*2 + 1]:
                        self.swap(self.heap_array, self.idx, self.idx*2)
                        self.idx *= 2
                    else:
                        self.swap(self.heap_array, self.idx, self.idx*2 + 1)
                        self.idx = self.idx*2 + 1
                elif self.heap_array[self.idx] < self.heap_array[self.idx*2] and not (self.heap_array[self.idx] < self.heap_array[self.idx*2 + 1]):
                    self.swap(self.heap_array, self.idx, self.idx*2)
                    self.idx *= 2
                elif not (self.heap_array[self.idx] < self.heap_array[self.idx*2]) and self.heap_array[self.idx] < self.heap_array[self.idx*2 + 1]:
                    self.swap(self.heap_array, self.idx, self.idx*2 + 1)
                    self.idx = self.idx*2 + 1
                else:
                    break

heap = Heap()

N = int(input())

for i in range(N):
    x = int(input())
    if x == 0:
        try:
            heap.pop()
        except:
            print(0)
    else:
        heap.insert(x)