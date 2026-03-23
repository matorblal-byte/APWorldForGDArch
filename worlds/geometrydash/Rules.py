from typing import TYPE_CHECKING
from BaseClasses import CollectionState
from .Items import item_table
from .Locations import location_table, ultimate_locations, GDLocation, coins
from worlds.generic.Rules import set_rule
from .Options import GDOptions
if TYPE_CHECKING:
    from . import GDWorld

def set_rules(world: "GDWorld"):
    # level rules!
    if world.options.coins.value:
        set_rule(world.get_location("Stereo Madness"), lambda state: state.has("Ship Portal", world.player))
        set_rule(world.get_location("Back On Track"), lambda state: state.has("Ship Portal", world.player))
        set_rule(world.get_location("Polargeist"), lambda state: state.has("Ship Portal", world.player))
        set_rule(world.get_location("Dry Out"), lambda state: state.has("Ship Portal", world.player))
        set_rule(world.get_location("Base After Base"), lambda state: state.has("Ship Portal", world.player))
        set_rule(world.get_location("Cant Let Go"), lambda state: state.has("Ship Portal", world.player))
        set_rule(world.get_location("Jumper"), lambda state: state.has("Ship Portal", world.player))
        set_rule(world.get_location("Time Machine"), lambda state: state.has("Ship Portal", world.player))
        set_rule(world.get_location("Cycles"), lambda state: state.has_all(("Ship Portal", "Ball Portal"), world.player))
        set_rule(world.get_location("xStep"), lambda state: state.has_all(("Ship Portal", "Ball Portal"), world.player))
        set_rule(world.get_location("Clutterfunk"), lambda state: state.has_all(("Ship Portal", "Ball Portal"), world.player))
        set_rule(world.get_location("Theory of Everything"), lambda state: state.has_all(("Ship Portal", "Ball Portal", "UFO Portal"), world.player))
        set_rule(world.get_location("Electroman Adventures"), lambda state: state.has_all(("Ship Portal", "Ball Portal", "UFO Portal"), world.player))
        set_rule(world.get_location("Clubstep"), lambda state: state.has_all(("Ship Portal", "Ball Portal", "UFO Portal"), world.player))
        set_rule(world.get_location("Electrodynamix"), lambda state: state.has_all(("Ship Portal", "Ball Portal", "UFO Portal"), world.player))
        set_rule(world.get_location("Hexagon Force"), lambda state: state.has_all(("Ship Portal", "Ball Portal", "UFO Portal"), world.player))
        set_rule(world.get_location("Blast Processing"), lambda state: state.has_all(("Ship Portal", "Ball Portal", "UFO Portal", "Wave Portal"), world.player))
        set_rule(world.get_location("Theory of Everything 2"), lambda state: state.has_all(("Ship Portal", "Ball Portal", "UFO Portal", "Wave Portal"), world.player))
        set_rule(world.get_location("Geometrical Dominator"), lambda state: state.has_all(("Ship Portal", "Ball Portal", "UFO Portal", "Wave Portal", "Robot Portal"), world.player))
        set_rule(world.get_location("Deadlocked"), lambda state: state.has_all(("Ship Portal", "Ball Portal", "UFO Portal", "Wave Portal", "Robot Portal"), world.player))
        set_rule(world.get_location("Fingerdash"), lambda state: state.has_all(("Ship Portal", "UFO Portal", "Wave Portal", "Robot Portal", "Spider Portal"), world.player))
        set_rule(world.get_location("Dash"), lambda state: state.has_all(("Ship Portal", "Ball Portal", "Wave Portal", "Robot Portal", "Spider Portal", "Swing Portal"), world.player))
        set_rule(world.get_location("The Cellar", lambda state: state.has("Robot Portal", world.player)))
        set_rule(world.get_location("The Secret Hollow"), lambda state: state.has("Ball Portal", world.player)) # Reason why robot isnt included is because you spawn as it it isnt a portal
    for location in location_table:
        for item in item_table:
            if location.startswith(item):
                set_rule(world.get_location(location), lambda state: state.has(item))
    if world.options.coins.value:
        for location in coins:
            for item in item_table:
                if location.startswith(item):
                    set_rule(world.get_location(location), lambda state: state.has(item))
        
                
    