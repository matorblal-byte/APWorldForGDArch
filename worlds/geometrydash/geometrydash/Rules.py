from typing import TYPE_CHECKING
from BaseClasses import CollectionState
from .Items import item_table
from .Locations import location_table, ultimate_locations, GDLocation
from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from . import GDWorld

def set_rules(world: "GDWorld"):
    for location in location_table:
        for item in item_table:
            if location.startswith(item):
                set_rule(world.get_location(location), lambda state: state.has(item))

            break
        break




        
        
                
    