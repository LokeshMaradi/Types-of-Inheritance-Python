class base1(object):
    def __init__(self):
        super(base1,self).__init__()
        print("base1 class")
class base2(object):
    def __init__(self):
        super(base2,self).__init__()
        print("base2 class")
class derived(base1,base2):
    def __init__(self):
        super(derived,self).__init__()
        print("derived class")
D=derived()
