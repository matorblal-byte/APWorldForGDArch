from .Items import item_table
from .Locations import location_table, coins
from worlds.generic.Rules import set_rule, add_rule
from rule_builder.rules import Has, HasAll
from . import GDWorld

def set_rules(world: GDWorld):
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
        world.set_rule(world.get_location("Theory of Everything"), HasAll("Ball Portal", "UFO Portal"))
        world.set_rule(world.get_location("Electroman Adventures"), HasAll("Ball Portal", "UFO Portal"))
        world.set_rule(world.get_location("Clubstep"), HasAll("Ball Portal", "UFO Portal"))
        world.set_rule(world.get_location("Electrodynamix"), HasAll("Ball Portal", "UFO Portal"))
        world.set_rule(world.get_location("Hexagon Force"), HasAll("Ball Portal", "UFO Portal"))
        world.set_rule(world.get_location("Blast Processing"), HasAll("Ball Portal", "UFO Portal", "Wave Portal"))
        world.set_rule(world.get_location("Theory of Everything 2"), HasAll("Ball Portal", "UFO Portal", "Wave Portal"))
        world.set_rule(world.get_location("Geometrical Dominator"), HasAll("Ball Portal", "UFO Portal", "Wave Portal", "Robot Portal"))
        world.set_rule(world.get_location("Deadlocked"), HasAll("Ball Portal", "UFO Portal", "Wave Portal", "Robot Portal"))
        world.set_rule(world.get_location("Fingerdash"), HasAll("UFO Portal", "Wave Portal", "Robot Portal", "Spider Portal"))
        world.set_rule(world.get_location("Dash"), HasAll("Ball Portal", "Wave Portal", "Robot Portal", "Spider Portal", "Swing Portal"))
        world.set_rule(world.get_location("The Sewers"), Has("The Tower: Unlock"))
        world.set_rule(world.get_location("The Cellar"), HasAll("Robot Portal", "The Sewers: Unlock"))
        world.set_rule(world.get_location("The Secret Hollow"), HasAll("Ball Portal", "The Cellar: Unlock")) # Reason why robot isnt included is because you spawn as it it isnt a portal
        world.set_rule(world.get_location("The Sewers"), Has("The Tower: Unlock"))
        world.set_rule(world.get_location("The Cellar"), Has("The Sewers: Unlock"))
        world.set_rule(world.get_location("The Secret Hollow"), Has("The Cellar: Unlock"))
    for location in location_table:
        for item in item_table:
            level = item.removesuffix(": Unlock")
            if location == level:
                print(location + " " + item + " " + level)
                world.add_rule(world.get_location(location), Has(item))
    if world.options.coins.value:
        for location in coins.keys():
            for item in item_table:
                level = item.removesuffix(": Unlock")
                if location.startswith(level):
                    print(location + " " + item + " " + level)
                    world.set_rule(world.get_location(location), Has(item))
                    if location.startswith(("Cycles", "xStep", "Clutterfunk")):
                        world.add_rule(world.get_location(location), Has("Ball Portal"))
                    elif location.startswith(("Theory of Everything", "Electroman Adventures", "Clubstep", "Electrodynamix", "Hexagon Force")):
                        world.add_rule(world.get_location(location), HasAll("Ball Portal", "UFO Portal"))
                    elif location.startswith(("Blast Processing", "Theory of Everything 2")):
                        world.add_rule(world.get_location(location), HasAll("Ball Portal", "UFO Portal", "Wave Portal"))
                    elif location.startswith(("Geometrical Dominator", "Deadlocked")):
                        world.add_rule(world.get_location(location), HasAll("Ball Portal", "UFO Portal", "Wave Portal", "Robot Portal"))
                    elif location.startswith("Fingerdash"):
                        world.add_rule(world.get_location(location), HasAll("UFO Portal", "Wave Portal", "Robot Portal", "Spider Portal"))
                    elif location.startswith("Dash"):
                        world.add_rule(world.get_location(location), HasAll("Ball Portal", "Wave Portal", "Robot Portal", "Spider Portal", "Swing Portal"))
                    elif location.startswith("The Sewers"):
                        world.add_rule(world.get_location(location), Has("The Tower: Unlock"))
                    elif location.startswith("The Cellar"):
                        world.add_rule(world.get_location(location), HasAll("Robot Portal", "The Sewers: Unlock"))
                    elif location.startswith("The Secret Hollow"):
                        world.add_rule(world.get_location(location), HasAll("Ball Portal", "The Cellar: Unlock"))
set_rules(GDWorld)