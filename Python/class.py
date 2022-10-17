class Human:
    def __init__(self,n,j):
        self.name=n
        self.job=j

    def do_work(self):
        if self.job=="tennis player":
            print(self.name,"plays tennis")
        elif self.job=="actor":
            print(self.name,"acts")

    def speaks(self):
        print(self.name,"how are you?")

a=Human("Tom holland","actor")
a.do_work()
a.speaks()
