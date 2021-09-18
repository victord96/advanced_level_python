import time

class FiboIter:
    """Iterator that prints the fibonacci sequence up to a specified number
    """

    def __init__(self, limit):
        self.limit = limit    


    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        self.aux = 0
        return self


    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else: 
            self.aux = self.n1 + self.n2
            #   self.n1 = self.n2
            #   self.n2 = self.aux 
            if self.aux < self.limit:
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
            else:
                raise StopIteration    


if __name__ == '__main__':
    fibonacci = FiboIter(100) 
    for i in fibonacci:
        print(i)
        #time.sleep(1)