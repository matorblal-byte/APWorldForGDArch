from typing import TYPE_CHECKING
from .Locations import location_table, coins
from .Items import item_table
from worlds.generic.Rules import set_rule, add_rule
from rule_builder.rules import Has, HasAll

#if TYPE_CHECKING:
#    from . import GDWorld

def set_all_rules(world, startinglevelslist):
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
        world.set_rule(world.get_location("Cycles"), Has("Ball Portal"))
        world.set_rule(world.get_location("xStep"), Has("Ball Portal"))
        world.set_rule(world.get_location("Clutterfunk"), Has("Ball Portal"))
        world.set_rule(world.get_location("Theory of Everything"), Has("Ball Portal") & Has("UFO Portal"))
        world.set_rule(world.get_location("Electroman Adventures"), Has("Ball Portal") & Has("UFO Portal"))
        world.set_rule(world.get_location("Clubstep"), Has("Ball Portal") & Has("UFO Portal"))
        world.set_rule(world.get_location("Electrodynamix"), Has("Ball Portal") & Has("UFO Portal"))
        world.set_rule(world.get_location("Hexagon Force"), Has("Ball Portal") & Has("UFO Portal"))
        world.set_rule(world.get_location("Blast Processing"), Has("Ball Portal") & Has("UFO Portal") & Has("Wave Portal"))
        world.set_rule(world.get_location("Theory of Everything 2"), Has("Ball Portal") & Has("UFO Portal") & Has("Wave Portal"))
        world.set_rule(world.get_location("Geometrical Dominator"), Has("Ball Portal") & Has("UFO Portal") & Has("Wave Portal") & Has("Robot Portal"))
        world.set_rule(world.get_location("Deadlocked"), Has("Ball Portal") & Has("UFO Portal") & Has("Wave Portal") & Has("Robot Portal"))
        world.set_rule(world.get_location("Fingerdash"), Has("UFO Portal") & Has("Wave Portal") & Has("Robot Portal") & Has("Spider Portal"))
        world.set_rule(world.get_location("Dash"), Has("Ball Portal") & Has("Wave Portal") & Has("Robot Portal") & Has("Spider Portal") & Has("Swing Portal"))
        world.set_rule(world.get_location("The Sewers"), Has("The Tower: Unlock"))
        world.set_rule(world.get_location("The Cellar"), Has("Robot Portal") & Has("The Sewers: Unlock"))
        world.set_rule(world.get_location("The Secret Hollow"), Has("Ball Portal") & Has("The Cellar: Unlock")) # Reason why robot isnt included is because you spawn as it it isnt a portal
        world.set_rule(world.get_location("The Sewers"), Has("The Tower: Unlock"))
        world.set_rule(world.get_location("The Cellar"), Has("The Sewers: Unlock"))
        world.set_rule(world.get_location("The Secret Hollow"), Has("The Cellar: Unlock"))
    for location in location_table:
        for item in item_table:
            level = item.removesuffix(": Unlock")
            if location == level:
                if level in world.startinglevelslist:
                    pass
                else:
                    print(location + " " + item + " " + level)
                    world.set_rule(world.get_location(location), Has(item))
    if world.options.coins.value:
        for location in coins.keys():
            for item in item_table:
                level = item.removesuffix(": Unlock")
                if location.startswith(level):
                    if level in world.startinglevelslist:
                        pass
                    else:
                        print(location + " " + item + " " + level)
                        world.set_rule(world.get_location(location), Has(item))
                        if location.startswith(("Cycles", "xStep", "Clutterfunk")):
                            world.set_rule(world.get_location(location), Has("Ball Portal"))
                        elif location.startswith(("Theory of Everything", "Electroman Adventures", "Clubstep", "Electrodynamix", "Hexagon Force")):
                            world.set_rule(world.get_location(location), HasAll("Ball Portal", "UFO Portal"))
                        elif location.startswith(("Blast Processing", "Theory of Everything 2")):
                            world.set_rule(world.get_location(location), HasAll("Ball Portal", "UFO Portal", "Wave Portal"))
                        elif location.startswith(("Geometrical Dominator", "Deadlocked")):
                            world.set_rule(world.get_location(location), HasAll("Ball Portal", "UFO Portal", "Wave Portal", "Robot Portal"))
                        elif location.startswith("Fingerdash"):
                            world.set_rule(world.get_location(location), HasAll("UFO Portal", "Wave Portal", "Robot Portal", "Spider Portal"))
                        elif location.startswith("Dash"):
                            world.set_rule(world.get_location(location), HasAll("Ball Portal", "Wave Portal", "Robot Portal", "Spider Portal", "Swing Portal"))
                        elif location.startswith("The Sewers"):
                            world.set_rule(world.get_location(location), Has("The Tower: Unlock"))
                        elif location.startswith("The Cellar"):
                            world.set_rule(world.get_location(location), HasAll("Robot Portal", "The Sewers: Unlock"))
                        elif location.startswith("The Secret Hollow"):
                            world.set_rule(world.get_location(location), HasAll("Ball Portal", "The Cellar: Unlock"))