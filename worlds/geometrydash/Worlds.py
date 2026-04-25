from BaseClasses import Tutorial, ItemClassification, Region
from worlds.AutoWorld import World, WebWorld
from .Items import item_table, GDItem, portals
from .Locations import location_table, ultimate_locations, GDLocation, coins, possible_starting_levels, check_shop_locations
from .WebWorld import GDWebWorld
from .Options import GDOptions
from .Items import GDItem
from .Regions import region_data_table, GDRegionData
from typing import List

class GDWorld(World):
    """Jump and fly your way through danger in this rhythm-based action platformer!"""
    #taken from steam

    game = "Geometry Dash"
    options_dataclass = GDOptions
    options = GDOptions
    topology_present = False
    web = GDWebWorld()

    item_name_to_id = item_table
    location_name_to_id = location_table
    gd_base_id = 130820130
    startinglevelslist = []
    def generate_starting_levels(self):
        global startinglevels
        startinglevels = ""
        key = ""
        random = self.random
        all_levels = list(possible_starting_levels.items())
        for _ in range(self.options.start_levels.value):
            levelNum = random.randint(0, len(all_levels) - 1)
            startinglevels += str(levelNum) + " "
            for key, value in item_table.items():
                if value == levelNum + self.gd_base_id:
                    level = key
                    while level in self.startinglevelslist:
                        levelNum = random.randint(0, len(all_levels) - 1)
                        startinglevels += str(levelNum) + " "
                        for key, value in item_table.items():
                            if value == levelNum + self.gd_base_id:
                                level = key
            self.startinglevelslist.append(level)
            print(startinglevels)
    def create_item(self, name: str, classification: ItemClassification) -> GDItem:
        if self.options.coins.value: 
            item_table.update(portals)
        return GDItem(name, classification, item_table[name], self.player)
    
    def create_items(self):
        item_pool: List[GDItem] = []
        if self.options.coins.value:
            item_table.update(portals)
        for item in item_table:
            if item in self.startinglevelslist:
                item_pool.append(self.create_item("100 Mana Orbs", ItemClassification.filler)) # filler for rn
                continue
            if item == "100 Mana Orbs" or item == "5 Diamonds":
                item_pool.append(self.create_item(item, ItemClassification.filler))
            else:
                item_pool.append(self.create_item(item, ItemClassification.progression))
        unfilledlocations = len(self.multiworld.get_unfilled_locations(self.player))
        numitemstoadd = unfilledlocations - len(item_pool)
        for _ in range(numitemstoadd):
            item = self.random.randint(1, 2)
            if item == 1:
                item_pool.append(self.create_item("100 Mana Orbs", ItemClassification.filler))
            elif item == 2:
                item_pool.append(self.create_item("5 Diamonds", ItemClassification.filler))
        self.multiworld.itempool += item_pool
        
    def create_regions(self):
        # shoutouts to clique once again
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            region.add_locations(location_table, GDLocation)
            #if self.options.ultimate.value:
            #   region.add_locations(ultimate_locations, GDLocation)
            if self.options.coins.value:
                region.add_locations(coins, GDLocation)
            if self.options.check_shop.value:
                region.add_locations(check_shop_locations, GDLocation)

            self.multiworld.regions.append(region)

    def fill_slot_data(self):
        # gotta do all this because apcpp dont got bools it seems
        if self.options.coins.value:
            coinsVal = 1
        else:
            coinsVal = 0
        #if self.options.ultimate.value:
            #   ultimateVal = 1 
        #else:            
            #   ultimateVal = 0
        if self.options.coin_locks.value:
            coinLocksVal = 1
        else:
            coinLocksVal = 0
        if self.options.check_shop.value:
            checkShopVal = 1
        else:
            checkShopVal = 0
        self.generate_starting_levels()
        return {
            "startinglevels": startinglevels,
            "start_levels": self.options.start_levels.value,
            #"ultimate": ultimateVal,
            "death_link": self.options.death_link.value,
            "death_link_amnesty": self.options.death_link_amnesty.value,
            "speed": self.options.speed.value,
            "coins": coinsVal,
            "coin_locks": coinLocksVal,
            "check_shop": checkShopVal
                }