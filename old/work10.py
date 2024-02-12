# program รับค่าความยาวด้านทั้ง3 ด้านของสามเหลี่ยมใดๆ คำนวนพื้นที่จากสูตรรากที่สองของ 
# s(s-a)(s-b)(s-c) โดยที่ s เท่ากับ (a+b+c)/2 a,b,c =ความยาวทั้งสาม

class Area():

    def input_side(self,a,b,c,s):
        self.a = a
        self.b = b
        self.c = c
        self.s = s
    def output_side(self):
        print(self.a,self.b,self.c,self.s)
    
targ1=Area(3,4,5,8)
targ1.output_side()