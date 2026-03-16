import typing
from dataclasses import dataclass
from Options import Option, DeathLink, Range, Toggle, PerGameCommonOptions

class StartingLevels(Range):
    """Amount of levels unlocked by default."""
    display_name = "Starting Levels"
    range_start = 0
    range_end = 5
    default = 3

class DeathAmount(Range):
    """Amount of deaths needed before sending a DeathLink signal. Does nothing if DeathLink is disabled."""
    display_name = "DeathLink Amnesty"
    range_start = 1
    range_end = 30
    default = 10

class Ultimate(Toggle):
    """Enables Ultimate Clubstep, Theory of Everything 2 and Deadlocked as locations."""
    display_name = "Ultimate Achievements"
    default = False

class CoinLocks(Toggle):
    """Enables the vanilla coin locks for Clubstep, Theory of Everything 2 and Deadlocked."""
    display_name = "Coin Locks"
    default = False

class Modifiers(Toggle):
    """Adds modifers to when you're playing a level."""
    display_name = "Modifers"
    default = True

class Speed(Range):
    """Speed up a level in the range (Weighted based on diffculty)"""
    display_name = "Speed"
    range_start = 75
    range_end = 250
    default = 100

# spinoff disabled as it depends on MoreGames by BitZ and the mod hasn't been ported to 2.206 yet. DO NOT ENABLE

# class Spinoff(Toggle):
    # """Enables Meltdown and Subzero levels as checks. You must have MoreGames by BitZ installed!"""
    # display_name = "Meltdown and Subzero Levels"
    # default = False

@dataclass
class GDOptions(PerGameCommonOptions):
    start_levels: StartingLevels
    ultimate: Ultimate
    # spinoff: Spinoff
    death_link: DeathLink
    death_link_amnesty: DeathAmount
    modifiers: Modifiers
    speed: Speed