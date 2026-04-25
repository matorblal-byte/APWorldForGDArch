from typing import Dict, List, NamedTuple
from BaseClasses import Region
from .Locations import location_table, ultimate_locations, GDLocation, coins, possible_starting_levels, check_shop_locations
class GDRegionData(NamedTuple):
    connecting_regions: List[str] = []

# you can access everything from the menu so like
# pretty much copied from clique ngl
region_data_table: Dict[str, GDRegionData] = {
    "Menu": GDRegionData(),
}