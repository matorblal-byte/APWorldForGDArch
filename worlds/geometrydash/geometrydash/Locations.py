from BaseClasses import Location

class GDLocation(Location):
    game: str = "Geometry Dash"

gd_base_id = 130820130

location_table = {
    "Stereo Madness": 1 + gd_base_id,
    "Back On Track": 2 + gd_base_id,
    "Polargeist": 3 + gd_base_id,
    "Dry Out": 4 + gd_base_id,
    "Base After Base": 5 + gd_base_id,
    "Cant Let Go": 6 + gd_base_id,
    "Jumper": 7 + gd_base_id,
    "Time Machine": 8 + gd_base_id,
    "Cycles": 9 + gd_base_id,
    "xStep": 10 + gd_base_id,
    "Clutterfunk": 11 + gd_base_id,
    "Theory of Everything": 12 + gd_base_id,
    "Electroman Adventures": 13 + gd_base_id,
    "Clubstep": 14 + gd_base_id,
    "Electrodynamix": 15 + gd_base_id,
    "Hexagon Force": 16 + gd_base_id,
    "Blast Processing": 17 + gd_base_id,
    "Theory of Everything 2": 18 + gd_base_id,
    "Geometrical Dominator": 19 + gd_base_id,
    "Deadlocked": 20 + gd_base_id,
    "Fingerdash": 21 + gd_base_id,
    "Dash": 22 + gd_base_id,
    "The Tower": 23 + gd_base_id,
    "The Sewers": 24 + gd_base_id,
    "The Cellar": 25 + gd_base_id,
    "The Secret Hollow": 26 + gd_base_id
}

ultimate_locations = {
    "Ultimate Clubstep": 27 + gd_base_id,
    "Ultimate Theory of Everything 2": 28 + gd_base_id,
    "Ultimate Deadlocked": 29 + gd_base_id
}

# unused until MoreGames is ported to 2.2081 (probably wont be so ill just not use this)
spinoff_locations = {
    "The Seven Seas": 30 + gd_base_id,
    "Viking Arena": 31 + gd_base_id,
    "Airborne Robots": 32 + gd_base_id,
    "Press Start": 33 + gd_base_id,
    "Nock Em": 34 + gd_base_id,
    "Power Trip": 35 + gd_base_id,

}
