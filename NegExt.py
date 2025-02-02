class NegExt:
    def __neg__(self):
        mro = self.__class__.mro()[2]
        
        if hasattr(mro, '__neg__'):
            return self.__class__(super().__neg__()) 
        
        if isinstance(self, dict):
            return self.__class__(self) 
        
        if hasattr(mro, '__getitem__'):
            try:
                return self.__class__(self[1:-1])
            except TypeError: 
                pass    
        return self.__class__(self)
    
