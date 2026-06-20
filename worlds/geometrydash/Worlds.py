from BaseClasses import Tutorial, ItemClassification, Region, Entrance
from rule_builder.rules import Has, HasAll
from worlds.AutoWorld import World, WebWorld
from .Items import item_table, GDItem, portals
from .Locations import location_table, ultimate_locations, GDLocation, coins, possible_starting_levels, check_shop_locations
from .WebWorld import GDWebWorld
from .Options import GDOptions
from .Items import GDItem
from .Rules import set_all_rules
from typing import List

class GDWorld(World):
    """Jump and fly your way through danger in this rhythm-based action platformer!"""
    #taken from steam

    game = "Geometry Dash"
    options_dataclass = GDOptions
    options = GDOptions
    topology_present = False
    web = GDWebWorld()
    itemstoid = item_table | portals
    item_name_to_id = itemstoid
    locationstoid = location_table | ultimate_locations | coins | check_shop_locations
    location_name_to_id = locationstoid
    gd_base_id = 130820130
    startinglevelslist = []
    def generate_early(self): # change the id thingies
        itemstoid = item_table.copy()
        if self.options.coins.value:
            itemstoid.update(portals)
        self.item_name_to_id = itemstoid
        locationstoid = location_table.copy()
        #if self.options.ultimate.value:
         #   locationstoid.update(ultimate_locations)
        if self.options.coins.value:
            locationstoid.update(coins)
        if self.options.check_shop.value:
            locationstoid.update(check_shop_locations)
        self.location_name_to_id = locationstoid
        return super().generate_early()
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
            self.startinglevelslist.append(level.replace(": Unlock", ""))
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
    def set_rules(self):
        set_all_rules(self, self.startinglevelslist)

    def create_regions(self):
        self.generate_starting_levels()
        region = Region("Menu", self.player, self.multiworld)
        for level in location_table:
            level_region = Region(level, self.player, self.multiworld)
            if level in self.startinglevelslist:
                self.create_entrance(region, level_region)
            else:
                if level.startswith(("Cycles", "xStep", "Clutterfunk")):
                    self.create_entrance(region, level_region, Has("Ball Portal") & Has(level + ": Unlock"), None, True)
                elif level.startswith(("Theory of Everything", "Electroman Adventures", "Clubstep", "Electrodynamix", "Hexagon Force")):
                    self.create_entrance(region, level_region, Has("Ball Portal") & Has("UFO Portal") & Has(level + ": Unlock"), None, True)
                elif level.startswith(("Blast Processing", "Theory of Everything 2")):
                    self.create_entrance(region, level_region, Has("Ball Portal") & Has("UFO Portal") & Has("Wave Portal") & Has(level + ": Unlock"), None, True)
                elif level.startswith(("Geometrical Dominator", "Deadlocked")):
                    self.create_entrance(region, level_region, Has("Ball Portal") & Has("UFO Portal") & Has("Wave Portal") & Has("Robot Portal") & Has(level + ": Unlock"), None, True)
                elif level.startswith("Fingerdash"):
                    self.create_entrance(region, level_region, Has("UFO Portal") & Has("Wave Portal") & Has("Robot Portal") & Has("Spider Portal") & Has(level + ": Unlock"), None, True)
                elif level.startswith("Dash"):
                    self.create_entrance(region, level_region, Has("Ball Portal") & Has("Wave Portal") & Has("Robot Portal") & Has("Spider Portal") & Has("Swing Portal") & Has(level + ": Unlock"), None, True)
                elif level.startswith("The Sewers"):
                    self.create_entrance(region, level_region, Has("The Tower: Unlock") & Has(level + ": Unlock"), None, True)
                elif level.startswith("The Cellar"):
                    self.create_entrance(region, level_region, Has("Robot Portal") & Has("The Sewers: Unlock") & Has(level + ": Unlock"), None, True)
                elif level.startswith("The Secret Hollow"):
                    self.create_entrance(region, level_region, Has("Ball Portal") & Has("The Cellar: Unlock") & Has(level + ": Unlock"), None, True)
                else:
                    self.create_entrance(region, level_region, Has(level + ": Unlock"), None, True)
            region.add_locations({level: location_table[level]}, GDLocation)
            if self.options.coins.value:
                for i in range(3):
                    level_region.add_locations({level + " - Coin " + str(i + 1): coins[level + " - Coin " + str(i + 1)]}, GDLocation)
            self.multiworld.regions.append(level_region)
        #if self.options.ultimate.value:
            #  region.add_locations(ultimate_locations, GDLocation)
        # if self.options.coins.value:
        #    region.add_locations(coins, GDLocation)
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
        if self.options.check_shop.value:
            si1 =  self.multiworld.get_location("Check Shop #1", self.player).item.name
            si2 =  self.multiworld.get_location("Check Shop #2", self.player).item.name
            si3 =  self.multiworld.get_location("Check Shop #3", self.player).item.name
            si4 =  self.multiworld.get_location("Check Shop #4", self.player).item.name
            si5 =  self.multiworld.get_location("Check Shop #5", self.player).item.name
            si6 =  self.multiworld.get_location("Check Shop #6", self.player).item.name
        else:
            si1 = "None"
            si2 = "None"
            si3 = "None"
            si4 = "None"
            si5 = "None"
            si6 = "None"
        return {
            "startinglevels": startinglevels,
            "start_levels": self.options.start_levels.value,
            #"ultimate": ultimateVal,
            "death_link": self.options.death_link.value,
            "death_link_amnesty": self.options.death_link_amnesty.value,
            "speed": self.options.speed.value,
            "coins": coinsVal,
            "coin_locks": coinLocksVal,
            "check_shop": checkShopVal,
            "shop_item1": si1,
            "shop_item2": si2,
            "shop_item3": si3,
            "shop_item4": si4,
            "shop_item5": si5,
            "shop_item6": si6
                }