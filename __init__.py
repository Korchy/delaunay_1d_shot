# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/delaunay_1d_shot
#
# Version history:
#   1.0.0 - Release
#       improve - projection from view
#       improve - working in edit mode
#       improve - only for selection
#       improve - deleting geometry (faces and edges) if exists
#       improve - add active material for building polygons
#   1.0.1 - Fixing bugs

from . import delaunay_voronoi_1d_panel
from . import delaunay_voronoi_1d
from . import delaunay_voronoi_1d_options

bl_info = {
    'name': 'Delaunay 1D Shot',
    'description': 'Points cloud Delaunay triangulation by projection from view',
    'author': 'Nikita Akimov',
    'version': (1, 0, 2),   # change in panel header too
    'blender': (2, 79, 0),
    'location': '3DView window - T-panel - 1D',
    'wiki_url': 'https://github.com/Korchy/1d_delaunay_voronoi',
    'tracker_url': 'https://github.com/Korchy/1d_delaunay_voronoi',
    'category': 'Mesh'
}


def register(ui=True):
    delaunay_voronoi_1d_options.register()
    delaunay_voronoi_1d.register()
    if ui:
        delaunay_voronoi_1d_panel.register()


def unregister(ui=True):
    if ui:
        delaunay_voronoi_1d_panel.unregister()
    delaunay_voronoi_1d.unregister()
    delaunay_voronoi_1d_options.unregister()
