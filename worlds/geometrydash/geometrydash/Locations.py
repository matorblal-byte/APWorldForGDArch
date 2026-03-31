from BaseClasses import Location

class GDLocation(Location):
    game: str = "Geometry Dash"

gd_base_id = 130820130

coins = {}

location_table = {
    "Stereo Madness": 0 + gd_base_id,
    "Back On Track": 1 + gd_base_id,
    "Polargeist": 2 + gd_base_id,
    "Dry Out": 3 + gd_base_id,
    "Base After Base": 4 + gd_base_id,
    "Cant Let Go": 5 + gd_base_id,
    "Jumper": 6 + gd_base_id,
    "Time Machine": 7 + gd_base_id,
    "Cycles": 8 + gd_base_id,
    "xStep": 9 + gd_base_id,
    "Clutterfunk": 10 + gd_base_id,
    "Theory of Everything": 11 + gd_base_id,
    "Electroman Adventures": 12 + gd_base_id,
    "Clubstep": 13 + gd_base_id,
    "Electrodynamix": 14 + gd_base_id,
    "Hexagon Force": 15 + gd_base_id,
    "Blast Processing": 16 + gd_base_id,
    "Theory of Everything 2": 17 + gd_base_id,
    "Geometrical Dominator": 18 + gd_base_id,
    "Deadlocked": 19 + gd_base_id,
    "Fingerdash": 20 + gd_base_id,
    "Dash": 21 + gd_base_id,
    "The Tower": 22 + gd_base_id,
    "The Sewers": 23 + gd_base_id,
    "The Cellar": 24 + gd_base_id,
    "The Secret Hollow": 25 + gd_base_id,
}

ultimate_locations = {
    "Ultimate Clubstep": 26 + gd_base_id,
    "Ultimate Theory of Everything 2": 27 + gd_base_id,
    "Ultimate Deadlocked": 28 + gd_base_id
}

# unused until MoreGames is ported to 2.2081 (probably wont be so ill just not use this)
spinoff_locations = {
    "The Seven Seas": 29 + gd_base_id,
    "Viking Arena": 30 + gd_base_id,
    "Airborne Robots": 31 + gd_base_id,
    "Press Start": 32 + gd_base_id,
    "Nock Em": 33 + gd_base_id,
    "Power Trip": 34 + gd_base_id,

}

possible_starting_levels = {
    "Stereo Madness": 0 + gd_base_id,
    "Back On Track": 1 + gd_base_id,
    "Polargeist": 2 + gd_base_id,
    "Dry Out": 3 + gd_base_id,
    "Base After Base": 4 + gd_base_id,
    "Cant Let Go": 5 + gd_base_id,
    "Jumper": 6 + gd_base_id,
    "Time Machine": 7 + gd_base_id,
}

check_shop_locations = {
    "Check Shop #1": 100 + gd_base_id,
    "Check Shop #2": 101 + gd_base_id,
    "Check Shop #3": 102 + gd_base_id,
    "Check Shop #4": 103 + gd_base_id,
    "Check Shop #5": 104 + gd_base_id,
    "Check Shop #6": 105 + gd_base_id,
}

for key in location_table:
    for i in range(3):
        name = key + " - Coin " + str(i + 1)
        value = (location_table[key] - gd_base_id) * 1000 + (i + 1) + gd_base_id
        coins[name] = value