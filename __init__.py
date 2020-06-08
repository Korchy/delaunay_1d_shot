# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_delaunay_voronoi
#
# Version history:
#   1.0.0 - Release
#       improve - projection from view
#       improve - working in edit mode
#       improve - only for selection
#       improve - deleting geometry (faces and edges) if exists
#       improve - add active material for building polygons

from . import delaunay_voronoi_1d_panel
from . import delaunay_voronoi_1d
from . import delaunay_voronoi_1d_options

bl_info = {
    'name': 'Delaunay 1D Shooter',
    'description': 'Points cloud Delaunay triangulation by projection from view',
    'author': 'Nikita Akimov',
    'version': (1, 0, 0),
    'blender': (2, 79, 0),
    'location': '3DView window - T-panel - 1D',
    'wiki_url': 'https://github.com/Korchy/1d_delaunay_voronoi',
    'tracker_url': 'https://github.com/Korchy/1d_delaunay_voronoi',
    'category': 'Mesh'
}


def register():
    delaunay_voronoi_1d_options.register()
    delaunay_voronoi_1d.register()
    delaunay_voronoi_1d_panel.register()


def unregister():
    delaunay_voronoi_1d_panel.unregister()
    delaunay_voronoi_1d.unregister()
    delaunay_voronoi_1d_options.unregister()
