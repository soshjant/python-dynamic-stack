class stack :
    def __init__ (self , size = None) :
        self.size = size
        self.list = [None] * size
        self.top = -1

    def push(self , x) :
        if self.top >= self.size -1 :
            print('stack is full')
            self.new_size(self.size*2)
            print('the list has been resized')    
        self.top = self.top+1
        self.list[self.top] = x
    def pop(self):
        if self.top == -1 :
            print('stack is empty')
            return
        itm = self.list[self.top ]
        self.top = self.top -1
        return itm
    def peak(self ):
        if self.top ==-1 :
            print ('stack is empty')
            return
        return self.list[self.top]
    def new_size(self , size2):
        list2 = [None] * size2
        for i in range (self.top+1):
            list2[i]= self.list[i]
        self.size = size2
        self.list = list2


    def show_size_top(self):
        return self.top+1, (self.size - self.top-1)
    def is_empty (self):
        return self.top == -1
    def __len__(self):
        return self.top+1


