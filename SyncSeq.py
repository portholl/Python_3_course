import asyncio
import sys

class Seq:
    syncronize = []
    
    def __init__(self, name):
        self.name = name
        self.num = len(self.syncronize)
        syncronizeEvent = asyncio.Event()
        self.syncronize.append(syncronizeEvent)
    
    async def run(self):
        if self.num != 0:
            await self.syncronize[self.num - 1].wait()
        print(self.name)
        if self.num + 1 < len(self.syncronize):
            self.syncronize[self.num].set()
        
        return self.name


exec(__import__('sys').stdin.read())
