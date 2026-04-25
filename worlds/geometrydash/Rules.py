from typing import TYPE_CHECKING
from BaseClasses import CollectionState
from .Items import item_table
from .Locations import location_table, ultimate_locations, GDLocation, coins
from worlds.generic.Rules import set_rule, add_rule
from rule_builder.rules import Rule, Has, HasAll
from .Options import GDOptions
if TYPE_CHECKING:
    from . import GDWorld

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
        set_rule(world.get_location("Cycles"), Has("Ball Portal"))
        set_rule(world.get_location("xStep"), Has("Ball Portal"))
        set_rule(world.get_location("Clutterfunk"), Has("Ball Portal"))
        set_rule(world.get_location("Theory of Everything"), HasAll("Ball Portal", "UFO Portal"))
        set_rule(world.get_location("Electroman Adventures"), HasAll("Ball Portal", "UFO Portal"))
        set_rule(world.get_location("Clubstep"), HasAll("Ball Portal", "UFO Portal"))
        set_rule(world.get_location("Electrodynamix"), HasAll("Ball Portal", "UFO Portal"))
        set_rule(world.get_location("Hexagon Force"), HasAll("Ball Portal", "UFO Portal"))
        set_rule(world.get_location("Blast Processing"), HasAll("Ball Portal", "UFO Portal", "Wave Portal"))
        set_rule(world.get_location("Theory of Everything 2"), HasAll("Ball Portal", "UFO Portal", "Wave Portal"))
        set_rule(world.get_location("Geometrical Dominator"), HasAll("Ball Portal", "UFO Portal", "Wave Portal", "Robot Portal"))
        set_rule(world.get_location("Deadlocked"), HasAll("Ball Portal", "UFO Portal", "Wave Portal", "Robot Portal"))
        set_rule(world.get_location("Fingerdash"), HasAll("UFO Portal", "Wave Portal", "Robot Portal", "Spider Portal"))
        set_rule(world.get_location("Dash"), HasAll("Ball Portal", "Wave Portal", "Robot Portal", "Spider Portal", "Swing Portal"))
        set_rule(world.get_location("The Sewers"), Has("The Tower: Unlock"))
        set_rule(world.get_location("The Cellar"), HasAll("Robot Portal", "The Sewers: Unlock"))
        set_rule(world.get_location("The Secret Hollow"), HasAll("Ball Portal", "The Cellar: Unlock")) # Reason why robot isnt included is because you spawn as it it isnt a portal
#    else:
#        set_rule(world.get_location("The Sewers"), Has("The Tower: Unlock"))
#        set_rule(world.get_location("The Cellar"), Has("The Sewers: Unlock"))
#        set_rule(world.get_location("The Secret Hollow"), Has("The Cellar: Unlock"))
    for location in location_table:
        for item in item_table:
            level = item.removesuffix(": Unlock")
            if location == level:
                print(location + " " + item + " " + level)
                add_rule(world.get_location(location), Has(item))
    if world.options.coins.value:
        for location in coins:
            for item in item_table:
                level = item.removesuffix(": Unlock")
                if location.startswith(level):
                    print(location + " " + item + " " + level)
                    set_rule(world.get_location(location), Has(item))
                    if location.startswith(("Cycles", "xStep", "Clutterfunk")):
                        add_rule(world.get_location(location), Has("Ball Portal"))
                    elif location.startswith(("Theory of Everything", "Electroman Adventures", "Clubstep", "Electrodynamix", "Hexagon Force")):
                        add_rule(world.get_location(location), HasAll("Ball Portal", "UFO Portal"))
                    elif location.startswith(("Blast Processing", "Theory of Everything 2")):
                        add_rule(world.get_location(location), HasAll("Ball Portal", "UFO Portal", "Wave Portal"))
                    elif location.startswith(("Geometrical Dominator", "Deadlocked")):
                        add_rule(world.get_location(location), HasAll("Ball Portal", "UFO Portal", "Wave Portal", "Robot Portal"))
                    elif location.startswith("Fingerdash"):
                        add_rule(world.get_location(location), HasAll("UFO Portal", "Wave Portal", "Robot Portal", "Spider Portal"))
                    elif location.startswith("Dash"):
                        add_rule(world.get_location(location), HasAll("Ball Portal", "Wave Portal", "Robot Portal", "Spider Portal", "Swing Portal"))
                    elif location.startswith("The Cellar"):
                        add_rule(world.get_location(location), Has("Robot Portal"))
                    elif location.startswith("The Secret Hollow"):
                        add_rule(world.get_location(location), Has("Ball Portal"))