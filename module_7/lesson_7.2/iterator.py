class MulIterator:
    def __init__(self,seq,stop=1):
        self.seq = seq
        self.stop = stop
        self.index = 0
        self.loop = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.loop > self.stop:
            raise StopIteration
        value = self.seq[self.index]
        self.index +=1
        if self.index == len(self.seq):
            self.index = 0
            self.loop +=1
        return value
    
sequence = [1,4,5,6,'$', None]

my_iterator = MulIterator(sequence,2)

for value in my_iterator:
    print(value, end='\t')