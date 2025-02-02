import asyncio

class FilterQueue(asyncio.Queue):
    def __init__(self, size=0):
        super().__init__(size)
        self._window = None

    @property
    def window(self):
        if self._queue:
            return self._queue[0]
        return None
    
    def __contains__(self, filter_func):
      for item in self._queue:
        if filter_func(item):
          return True
      return False

    def later(self):
        super().put_nowait(super().get_nowait())

    async def get(self, filter_func=None):
        if filter_func is None:
            return await super().get()
        
        if filter_func not in self:
            return await super().get()
        
        item = await super().get()
        while not filter_func(item):
            await super().put(item)
            item = await super().get()
        return item
    

exec(__import__('sys').stdin.read())