from typing import List

from .Options import GDOptions
from .Items import item_table, GDItem
from .Locations import location_table, ultimate_locations, GDLocation
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

    def create_item(self, name: str, classification: ItemClassification) -> GDItem:
        return GDItem(name, classification, item_table[name], self.player)
    
    def create_items(self):
        item_pool: List[GDItem] = []
        for item in item_table:
            if item == "100 Mana Orbs" or item == "Secret Coin":
                item_pool.append(self.create_item(item, ItemClassification.useful))
            else:
                item_pool.append(self.create_item(item, ItemClassification.progression))

        self.multiworld.itempool += item_pool

    def create_regions(self):
        # shoutouts to clique once again
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            region.add_locations(location_table, GDLocation)
            if self.options.ultimate:
                region.add_locations(ultimate_locations, GDLocation)

            self.multiworld.regions.append(region)

#        for region_name in region_data_table.items():
#            region = self.get_region(region_name)

    def set_rules(self):
        set_rules(self)

    def fill_slot_data(self):
        startinglevels = []
        for i in range(self.options.start_levels.value):
            levelid = random.randint(1, len(location_table))
            level = location_table[location_table.keys()[levelid]]
            if self.options.ultimate:
                levelid = random.randint(1, len(location_table) + len(ultimate_locations))
            if level in startinglevels:
                while level in startinglevels:
                    levelid = random.randint(1, len(location_table))
                    level = location_table[location_table.keys()[levelid]]
                    if self.options.ultimate:
                        levelid = random.randint(1, len(location_table) + len(ultimate_locations))
            startinglevels.append(location_table[levelid])
            print(f"Filled level: {level}")
        return {
            "startinglevels": startinglevels,
            "start_levels": self.options.start_levels.value,
            "ultimate": self.options.ultimate.value,
            # "spinoff": self.options.spinoff.value,
            "death_link": self.options.death_link.value,
            "death_link_amnesty": self.options.death_link_amnesty.value
        }
