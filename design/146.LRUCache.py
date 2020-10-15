from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.lrucache=  OrderedDict()

    def get(self, key: int) -> int:
        # print('get', self.lrucache)
        if key in self.lrucache:
                self.lrucache.move_to_end(key)
                
                return (self.lrucache[key])

        return (-1)
        

    def put(self, key: int, value: int) -> None:
        

        if key in self.lrucache:
            self.lrucache.move_to_end(key)
        
        
        elif len(self.lrucache)==self.cap:
            self.lrucache.popitem (last=False)
        self.lrucache[key]=value




####Optimized###


from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.lrucache=  OrderedDict()

    def get(self, key: int) -> int:
        
        if key in self.lrucache:
                
                value= self.lrucache.pop(key)
                self.lrucache[key]=value
                return (value)

        return (-1)
        

    def put(self, key: int, value: int) -> None:
        

        if key in self.lrucache:
            self.lrucache.pop (key)
        
        
        if len(self.lrucache)==self.cap:
            self.lrucache.popitem (last=False)
        self.lrucache[key]=value
        
