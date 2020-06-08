
from . import delaunayVoronoiBlender

bl_info = {
	"name": "Delaunay Voronoi ",
	"description": "Points cloud Delaunay triangulation in 2.5D (suitable for terrain modelling) or Voronoi diagram in 2D",
	"author": "Domlysz",
	'license': 'GPL',
	'deps': '',
	"version": (1, 4),
	"blender": (2, 7, 0),
	"location": "View3D > Tools > GIS",
	"warning": "",
	'wiki_url': 'https://github.com/domlysz/BlenderGIS/wiki',
	'tracker_url': '',
	'link': '',
	"category": "Mesh"}


def register():
	delaunayVoronoiBlender.register()

def unregister():
	delaunayVoronoiBlender.unregister()
