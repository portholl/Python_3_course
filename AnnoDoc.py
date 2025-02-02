class AnnoDoc(type):
    def __new__(cls, classname, base, attrs): 
       
        doc = attrs.get('__doc__', None)
        for key, value in attrs.get('__annotations__', {}).items():
            if isinstance(value, str):
                doc = doc + f'\n{key}: {value}' if doc else f'\n{key}: {value}' 
        attrs['__doc__'] = doc
        
        anno = {}
        for key in attrs.get('__annotations__', {}):
            if key in attrs:
                anno[key] = type(attrs[key])
        attrs['__annotations__'] = anno
        
        return super().__new__(cls, classname, base, attrs)

exec(__import__('sys').stdin.read())
