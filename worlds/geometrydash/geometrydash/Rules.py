from typing import TYPE_CHECKING
from BaseClasses import CollectionState
from .Items import item_table
from .Locations import location_table, ultimate_locations, GDLocation, coins
from worlds.generic.Rules import set_rule, add_rule
from .Options import GDOptions
if TYPE_CHECKING:
    from . import GDWorld

# 100% unoptimized
def set_rules(world: "GDWorld"):
    # level rules!
    if world.options.coins.value:
#        set_rule(world.get_location("Stereo Madness"), lambda state: state.has("Ship Portal", world.player))
#        set_rule(world.get_location("Back On Track"), lambda state: state.has("Ship Portal", world.player))
#        set_rule(world.get_location("Polargeist"), lambda state: state.has("Ship Portal", world.player))
#        set_rule(world.get_location("Dry Out"), lambda state: state.has("Ship Portal", world.player))
#        set_rule(world.get_location("Base After Base"), lambda state: state.has("Ship Portal", world.player))
#        set_rule(world.get_location("Cant Let Go"), lambda state: state.has("Ship Portal", world.player))
#        set_rule(world.get_location("Jumper"), lambda state: state.has("Ship Portal", world.player))
#        set_rule(world.get_location("Time Machine"), lambda state: state.has("Ship Portal", world.player))
        set_rule(world.get_location("Cycles"), lambda state: state.has("Ball Portal", world.player))
        set_rule(world.get_location("xStep"), lambda state: state.has("Ball Portal", world.player))
        set_rule(world.get_location("Clutterfunk"), lambda state: state.has("Ball Portal", world.player))
        set_rule(world.get_location("Theory of Everything"), lambda state: state.has_all(("Ball Portal", "UFO Portal"), world.player))
        set_rule(world.get_location("Electroman Adventures"), lambda state: state.has_all(("Ball Portal", "UFO Portal"), world.player))
        set_rule(world.get_location("Clubstep"), lambda state: state.has_all(("Ball Portal", "UFO Portal"), world.player))
        set_rule(world.get_location("Electrodynamix"), lambda state: state.has_all(("Ball Portal", "UFO Portal"), world.player))
        set_rule(world.get_location("Hexagon Force"), lambda state: state.has_all(("Ball Portal", "UFO Portal"), world.player))
        set_rule(world.get_location("Blast Processing"), lambda state: state.has_all(("Ball Portal", "UFO Portal", "Wave Portal"), world.player))
        set_rule(world.get_location("Theory of Everything 2"), lambda state: state.has_all(("Ball Portal", "UFO Portal", "Wave Portal"), world.player))
        set_rule(world.get_location("Geometrical Dominator"), lambda state: state.has_all(("Ball Portal", "UFO Portal", "Wave Portal", "Robot Portal"), world.player))
        set_rule(world.get_location("Deadlocked"), lambda state: state.has_all(("Ball Portal", "UFO Portal", "Wave Portal", "Robot Portal"), world.player))
        set_rule(world.get_location("Fingerdash"), lambda state: state.has_all(("UFO Portal", "Wave Portal", "Robot Portal", "Spider Portal"), world.player))
        set_rule(world.get_location("Dash"), lambda state: state.has_all(("Ball Portal", "Wave Portal", "Robot Portal", "Spider Portal", "Swing Portal"), world.player))
        set_rule(world.get_location("The Sewers"), lambda state: state.has("The Tower: Unlock", world.player))
        set_rule(world.get_location("The Cellar"), lambda state: state.has_all(("Robot Portal", "The Sewers: Unlock"), world.player))
        set_rule(world.get_location("The Secret Hollow"), lambda state: state.has_all(("Ball Portal", "The Cellar: Unlock"), world.player)) # Reason why robot isnt included is because you spawn as it it isnt a portal
#    else:
#        set_rule(world.get_location("The Sewers"), lambda state: state.has("The Tower: Unlock", world.player))
#        set_rule(world.get_location("The Cellar"), lambda state: state.has("The Sewers: Unlock", world.player))
#        set_rule(world.get_location("The Secret Hollow"), lambda state: state.has("The Cellar: Unlock", world.player))
    for location in location_table:
        for item in item_table:
            level = item.removesuffix(": Unlock")
            if location == level:
                print(location + " " + item + " " + level)
                add_rule(world.get_location(location), lambda state, item = item: state.has(item, world.player))
    if world.options.coins.value:
        for location in coins:
            for item in item_table:
                level = item.removesuffix(": Unlock")
                if location.startswith(level):
                    print(location + " " + item + " " + level)
                    set_rule(world.get_location(location), lambda state, item = item: state.has(item, world.player))
                    if location.startswith(("Cycles", "xStep", "Clutterfunk")):
                        add_rule(world.get_location(location), lambda state: state.has("Ball Portal", world.player))
                    elif location.startswith(("Theory of Everything", "Electroman Adventures", "Clubstep", "Electrodynamix", "Hexagon Force")):
                        add_rule(world.get_location(location), lambda state: state.has_all(("Ball Portal", "UFO Portal"), world.player))
                    elif location.startswith(("Blast Processing", "Theory of Everything 2")):
                        add_rule(world.get_location(location), lambda state: state.has_all(("Ball Portal", "UFO Portal", "Wave Portal"), world.player))
                    elif location.startswith(("Geometrical Dominator", "Deadlocked")):
                        add_rule(world.get_location(location), lambda state: state.has_all(("Ball Portal", "UFO Portal", "Wave Portal", "Robot Portal"), world.player))
                    elif location.startswith("Fingerdash"):
                        add_rule(world.get_location(location), lambda state: state.has_all(("UFO Portal", "Wave Portal", "Robot Portal", "Spider Portal"), world.player))
                    elif location.startswith("Dash"):
                        add_rule(world.get_location(location), lambda state: state.has_all(("Ball Portal", "Wave Portal", "Robot Portal", "Spider Portal", "Swing Portal"), world.player))
                    elif location.startswith("The Cellar"):
                        add_rule(world.get_location(location), lambda state: state.has("Robot Portal", world.player))
                    elif location.startswith("The Secret Hollow"):
                        add_rule(world.get_location(location), lambda state: state.has("Ball Portal", world.player))