# Priority Queue
# Yohannes Dawit

class PriorityQueue:

    def __init__(self,items =[]):
        self.heap = [None]+list(items)
        self._build_heap()

    def _largest_child(self, i):
        """ returns index of node i's largest child or None when node i is a leaf """
        if i*2 >=len(self.heap):
            return None

        if i*2+1 >= len(self.heap):
            return i*2

        if self.heap[i*2]>self.heap[i*2+1]:
            return i*2
        
        return i*2+1
        
        
    def _bubble_up(self, i):
        """ restore heap by bubbling up from node i """
        while i >= 1 and self.heap[i] >self.heap[i//2]:
            if i ==2:
                self.heap[1],self.heap[2]= self.heap[2],self.heap[1]
                break
                
            self.heap[i],self.heap[i//2]= self.heap[i//2],self.heap[i]
            i = i //2
            

    def _bubble_down(self, i):
        """ restore heap by bubbling down from node i """
        while i*2 <= len(self.heap)-1 and self.heap[i] < self.heap[self._largest_child(i)]:#min(self.heap[i*2],self.heap[i*2+1]):
            x = self._largest_child(i)
            self.heap[i],self.heap[x] = self.heap[x],self.heap[i]
            i = x
            
            

    def _build_heap(self):
        """ builds an initial heap bottom-up"""
        n = len(self.heap)-1
        for i in range(n//2,0,-1):
            k = i
            v = self.heap[k]
            heap = False
            while not heap and 2*k <= n:
                j = 2*k
                if j<n:
                    if self.heap[j]<self.heap[j+1]:
                        j+=1
                if v >= self.heap[j]:
                    heap = True
                else:
                    self.heap[k] = self.heap[j]
                    k = j
            self.heap[k] = v


  
        

    def add(self, item):
        """ add item to the queue """
        self.heap.append(item)
        self._bubble_up(len(self.heap)-1)

    def get_max(self):
        """ returns and removes highest priority item """
        if len(self.heap) == 1:
            return None
        
        result = self.heap[1]
        last = self.heap.pop()
        
        if len(self.heap)>1:
            self.heap[1] = last
            self._bubble_down(1)
        return result

def heapsort(lst):
    pq = PriorityQueue(lst)
    sorted_lst = []
    i = pq.get_max()
    while i is not None:
        sorted_lst.append(i)
        i = pq.get_max()

    return sorted_lst

    
def main():
    nums = str(input("Please enter a list of numbers separated by commas"))
    lst = [int(item) for item in nums.split(",")]
    sorted_lst = heapsort(lst)
    print ("The sorted numbers are:")
    print(sorted_lst)
    qt = input("press any key to quit")
if __name__== "__main__":
    main()
        

        
