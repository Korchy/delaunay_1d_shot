# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_delaunay_voronoi
#

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class DELAUNAY_VORONOI_1D_PT_panel(Panel):
	bl_idname = 'DELAUNAY_VORONOI_1D_PT_panel'
	bl_label = 'Delaunay Shot'
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = '1D'

	def draw(self, context):
		row = self.layout.row()
		row.prop(context.window_manager.delaunay_voronoi_1d_opts, 'projection', expand=True)
		self.layout.prop(context.window_manager.delaunay_voronoi_1d_opts, 'remove_geometry')
		self.layout.separator()
		self.layout.operator('delaunay_voronoy_1d.triangulate_view')


def register():
	register_class(DELAUNAY_VORONOI_1D_PT_panel)


def unregister():
	unregister_class(DELAUNAY_VORONOI_1D_PT_panel)
