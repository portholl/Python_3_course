import asyncio

class Monster:
    def __init__(self, name, position, delay, power):
        self.name = name
        self.position = position
        self.delay = delay
        self.power = power
        self.alive = True
        self.ticks = 0

    async def run(self, start_barrier, end_barrier):
        while True:
            await start_barrier.wait()
            self.ticks += 1
            if self.ticks % self.delay == 0 and self.alive :
                self.position += 1
            await end_barrier.wait()

    def __repr__(self):
      return self.name


async def game(monsters, start_barrier, end_barrier, epochs):
    for _ in range(epochs):
        await start_barrier.wait()
        await end_barrier.wait()
        await asyncio.sleep(0)

        alive_monsters = [monster for monster in monsters if monster.alive]
        if not alive_monsters:
            return "All dead"
        if len(alive_monsters) == 1:
           return alive_monsters[0]
      
        fighting_pair = []
        positions = {}
        for monster in alive_monsters:
          if monster.position in positions:
            positions[monster.position].append(monster)
            if len(positions[monster.position]) == 2:
                fighting_pair = positions[monster.position]
                break
          else:
            positions[monster.position] = [monster]
        
        if fighting_pair:
          monster1, monster2 = fighting_pair[0], fighting_pair[1]
          if monster1.power == monster2.power:
            monster1.alive = False
            monster2.alive = False
          elif monster1.power > monster2.power:
              monster1.power -= monster2.power
              monster2.alive = False
          else:
              monster2.power -= monster1.power
              monster1.alive = False

    surviving_monsters = [monster.name for monster in monsters if monster.alive]
    if len(surviving_monsters) == len(monsters) :
       return "All flee"
    if surviving_monsters:
        return ", ".join(surviving_monsters)
    else:
      return "All dead"

exec(__import__('sys').stdin.read())