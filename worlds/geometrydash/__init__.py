import os
import json
from typing import List

from .Options import GDOptions
from .Items import item_table, GDItem, portals
from .Locations import location_table, ultimate_locations, GDLocation, coins, possible_starting_levels
from .Regions import region_data_table
from .Rules import set_rules
from BaseClasses import Tutorial, ItemClassification, Region
from worlds.AutoWorld import World, WebWorld
import random
class GDWebWorld(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide for setting up Geometry Dash + Geode for the Archipelago Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["1257Plays"]
    )]
    theme = "ocean"

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

    def create_item(self, name: str, classification: ItemClassification) -> GDItem:
        if self.options.coins.value:
            item_table.update(portals)
        return GDItem(name, classification, item_table[name], self.player)
    
    def create_items(self):
        global startinglevels
        startinglevels = ""
        startinglevelslist = []
        key = ""
        all_levels = list(possible_starting_levels.items())
        for _ in range(self.options.start_levels.value):
            levelNum = random.randint(0, len(all_levels) - 1)
            startinglevels += str(levelNum) + " "
            for key, value in item_table.items():
                if value == levelNum + self.gd_base_id:
                    level = key
                    while level in startinglevelslist:
                        levelNum = random.randint(0, len(all_levels) - 1)
                        startinglevels += str(levelNum) + " "
                        for key, value in item_table.items():
                            if value == levelNum + self.gd_base_id:
                                level = key
            startinglevelslist.append(level)
            print(startinglevels)
        item_pool: List[GDItem] = []
        if self.options.coins.value:
            item_table.update(portals)
        for item in item_table:
            if item in startinglevelslist:
                item_pool.append(self.create_item("100 Mana Orbs", ItemClassification.filler)) # filler for rn
                continue
            if item == "100 Mana Orbs" or item == "5 Diamonds":
                item_pool.append(self.create_item(item, ItemClassification.filler))
            else:
                item_pool.append(self.create_item(item, ItemClassification.progression))
        unfilledlocations = len(self.multiworld.get_unfilled_locations(self.player))
        numitemstoadd = unfilledlocations - len(item_pool)
        for _ in range(numitemstoadd):
            item = random.randint(1, 2)
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
            if self.options.ultimate:
                region.add_locations(ultimate_locations, GDLocation)
            if self.options.coins:
                region.add_locations(coins, GDLocation)

            self.multiworld.regions.append(region)

#        for region_name in region_data_table.items():
#            region = self.get_region(region_name)

    def set_rules(self):
        set_rules(self)

    def fill_slot_data(self):
       return {
        "startinglevels": startinglevels,
        "start_levels": self.options.start_levels.value,
        "ultimate": self.options.ultimate.value,
        "death_link": self.options.death_link.value,
        "death_link_amnesty": self.options.death_link_amnesty.value,
        "speed": self.options.speed.value,
        "coins": self.options.coins.value
            }