# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_delaunay_voronoi
#

from bpy.types import PropertyGroup, WindowManager
from bpy.props import EnumProperty, BoolProperty, PointerProperty
from bpy.utils import register_class, unregister_class


class DELAUNAY_VORONOI_1D_options(PropertyGroup):
	projection = EnumProperty(
		items=[
			('Camera', 'Camera', 'Camera', '', 0),
			('View', 'View', 'View', '', 1)
		],
		default='View'
	)
	remove_geometry = BoolProperty(
		name='Remove geometry',
		default=True
	)


def register():
	register_class(DELAUNAY_VORONOI_1D_options)
	WindowManager.delaunay_voronoi_1d_opts = PointerProperty(type=DELAUNAY_VORONOI_1D_options)


def unregister():
	del WindowManager.delaunay_voronoi_1d_opts
	unregister_class(DELAUNAY_VORONOI_1D_options)
