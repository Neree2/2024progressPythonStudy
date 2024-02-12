class First:
    def __init__(self, data=None) :
        self.data=data
        self.node=None
class Second:
    def __init__(self) :
        self.f=First()
    def append(self,data):
        new_node=First(data)
        idk=self.f
        while idk.next is not None:
            idk = idk.next
        idk.next = new_node
    def delete(self,num):
        cur_node = self.f
        while cur_node.next is num:
            cur_node=None
            