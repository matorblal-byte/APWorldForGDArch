from BaseClasses import Tutorial, ItemClassification, Region
from worlds.AutoWorld import World, WebWorld

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
