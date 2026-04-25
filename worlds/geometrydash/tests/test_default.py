from .testbase import GDTestBase as GDTestBase
from ..Locations import coins
class TestDefault(GDTestBase):
    # no options

    levels = {
    "Stereo Madness",
    "Back On Track",
    "Polargeist",
    "Dry Out",
    "Base After Base",
    "Cant Let Go",
    "Jumper",
    "Time Machine",
    "Cycles",
    "xStep",
    "Clutterfunk",
    "Theory of Everything",
    "Electroman Adventures",
    "Clubstep",
    "Electrodynamix",
    "Hexagon Force",
    "Blast Processing",
    "Theory of Everything 2",
    "Geometrical Dominator",
    "Deadlocked",
    "Fingerdash",
    "Dash",
    "The Tower",
    "The Sewers",
    "The Cellar",
    "The Secret Hollow",
}
    def test_can_goal(self):
        itemstocheck = []
        startingLevels = self.world.startinglevelslist
        for i in startingLevels:
            level = self.levels[i]
            item = self.world.get_location(level).item
            for j in coins.keys():
                if j.startswith(level):
                    coinitem = self.world.get_location(j).item
                    self.collect(coinitem)
                    if coinitem.name.endswith(": Unlock"):
                        itemstocheck.append(coinitem.name)
            if item.name.endswith(": Unlock"):
                itemstocheck.append(item.name.split(": Unlock")[0])
            self.assertIsNotNone(item)
            self.assertIsNotNone(coinitem)
            self.collect(item)
        for item in itemstocheck:
            if item.startswith(level):
                self.assertTrue(self.can_reach(item))
                for j in coins.keys():
                    if j.startswith(level):
                        coinitem = self.world.get_location(j).item
                        self.collect(coinitem)
                        if coinitem.name.endswith(": Unlock"):
                            itemstocheck.append(coinitem.name)
                if item.name.endswith(": Unlock"):
                    itemstocheck.append(item.name.split(": Unlock")[0])
                    self.assertIsNotNone(item)
                    self.assertIsNotNone(coinitem)
                    self.collect(item)
