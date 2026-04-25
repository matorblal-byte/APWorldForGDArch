from test.bases import WorldTestBase

from ..Worlds import GDWorld

class GDTestBase(WorldTestBase):
    game = "Geometry Dash"
    world: GDWorld