def ind(a, n, f):
    m=[]
    if f==1:
        m.append(a)
        for i in range(n-1):
            a+=n+1
            if a>=n*n:
                m.append(a-n*n)
            else:
                m.append(a)
    if f==-1:
        m.append(a)
        for i in range(n-1):
            a+=n-1
            if a>=n*n:
                m.append(a-n*n)
            else:
                m.append(a)
    return m

class Matrix():
    def __init__(self, m):
        self.dim=int(len(m)**0.5)
        self.m=m
        lines=[m[i*self.dim:(i+1)*self.dim] for i in range(self.dim)]
        lines_i=[list(range(i*self.dim,(i+1)*self.dim)) for i in range(self.dim)]
        self.lines=lines
        self.lines_i=lines_i
        columns=[]
        columns_i=[]
        subc=[]
        subc_i=[]
        c=0
        for j in range(self.dim):
            for i in range(self.dim**2):
                if(i%(self.dim))==c:
                    subc.append(m[i])
                    subc_i.append(i)
                if len(subc)==self.dim:
                    c+=1
                    columns.append(subc)
                    columns_i.append(subc_i)
                    subc=[]
                    subc_i=[]
                    break
        self.columns=columns 
        self.columns_i=columns_i
            
    def show(self):
        for i in range(1,self.dim**2+1):
            print(self.m[i-1],end=' ')
            if i%(self.dim)==0:
                print()
    def det(self):
        if self.dim==1:
            return self.m[0]
        elif self.dim==2:
            return self.m[0]*self.m[3]-self.m[1]*self.m[2]
        pd=0
        nd=0
        pdi=[ind(i,self.dim,1) for i in self.columns_i[0]]
        ndi=[ind(i,self.dim,-1) for i in self.columns_i[self.dim-1]]
        for i in pdi:
            d=1
            for j in i:
                d*=self.m[j]
            pd+=d
        for i in ndi:
            d=-1
            for j in i:
                d*=self.m[j]
            nd+=d
        return pd+nd

def fillMatrix():
    a=input().split()
    m=[]
    for i in range(int(len(a)**0.5)**2):
        try:
            m.append(int(a[i]))
        except:
            print("Wrong input")
    m=Matrix(m)
    m.show()
    a=input('Y/n?\n')
    while True:
        if a=='Y' or a=='y' or a=='д' or a=='Д':
            break
        else:
            a=input().split()
            m=[]
            for i in range(int(len(a)**0.5)**2):
                try:
                    m.append(int(a[i]))
                except:
                    print("Wrong input")
            m=Matrix(m)
            m.show()
            a=input('Y/n?\n')
    return m