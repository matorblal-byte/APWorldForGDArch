from typing import Dict, List, NamedTuple

class GDRegionData(NamedTuple):
    connecting_regions: List[str] = []

# you can access everything from the menu so like
# pretty much copied from clique ngl
region_data_table: Dict[str, GDRegionData] = {
    "Menu": GDRegionData(),
}