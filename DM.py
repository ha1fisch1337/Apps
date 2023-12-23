class rel():
    def __init__(self,m):
        maks=0
        self.m=m
        for i in m:
            maks=max(i[0],i[1],maks)
        self.n=maks+1
    def matrix(self):
        for i in range(self.n):
            for j in range(self.n):
                if i==0 and j==0:
                    print(' ',end=' ')
                elif i==0:
                    print(j,end=' ')
                elif j==0:
                    print(i,end=' ')
                elif (i,j) in self.m:
                    print('+',end=' ')
                else:
                    print('-', end=' ')
            print()
        print()

    def obr(self):
        a=[]
        for i in self.m:
            a.append((i[1],i[0]))
        a=rel(a)
        return a
    
    def dop(self):
        for i in range(self.n):
            for j in range(self.n):
                if i==0 and j==0:
                    print(' ',end=' ')
                elif i==0:
                    print(j,end=' ')
                elif j==0:
                    print(i,end=' ')
                elif (i,j) not in self.m:
                    print('+',end=' ')
                else:
                    print('-', end=' ')
            print()
        print()


    def compose(self,b):
        c=[]
        n=max(self.n,b.n)
        for i in self.m:
            for j in b.m:
                if i[1]==j[0]:
                    c.append((i[0],j[1]))
        c=rel(c)
        c.matrix()
    def kernel(self):
        self.obr().compose(self)

a=[(1,2),(2,3),(3,1),(2,2),(3,2)]
a=rel(a)
a.compose(a)