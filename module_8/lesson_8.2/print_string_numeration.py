import pickle 

class TextReader:
    def __init__(self,filename):
        self.filename = filename
        self.file = open(self.filename)
        self.line_idx = 0

    def readline(self):
        line = self.file.readline()
        if not line:
            return "End of file"
        
        self.line_idx += 1

        if line.endswith("\n"):
            line = line[:-1]
        return f"{self.line_idx}, {line}"
    
    def __getstate__(self):
        state = self.__dict__.copy()
        del state['file']
        return state
    
    def __setstate__(self,state):
        self.__dict__.update(state)
        file = open(self.filename)
        for _ in range(self.line_idx):
            file.readline()
        self.file = file

reader = TextReader('lines.txt')
print(reader.line_idx)
print(reader.readline())
print(reader.readline())
print(reader.readline())

new_reader = pickle.loads(pickle.dumps(reader))
print(reader.line_idx)
print(new_reader.line_idx)
print(reader.readline())
print(new_reader.readline())
print(new_reader.readline())
print(reader.readline())
print(new_reader.readline())