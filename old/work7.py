class Animals:
    def detail(self,name,weight):
        self.name = name
        self.weight = weight
    def showData(self):
        print(self.name)
        print(self.weight)

anm1 = Animals()
anm1.detail('bird',53)
anm2 = Animals()
anm2.detail('chicken',42)
anm3 = Animals()
anm3.detail('duck',63)

anm1.showData()
anm2.showData()
anm3.showData()