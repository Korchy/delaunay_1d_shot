# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/delaunay_1d_shot
#

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


def ui(layout, context):
	# ui panel
	layout.label(text='Projection to')
	row = layout.row()
	row.prop(context.window_manager.delaunay_voronoi_1d_opts, 'projection', expand=True)
	layout.prop(context.window_manager.delaunay_voronoi_1d_opts, 'remove_geometry')
	layout.separator()
	layout.operator('delaunay_voronoy_1d.triangulate_view')


class DELAUNAY_VORONOI_1D_PT_panel(Panel):
	bl_idname = 'DELAUNAY_VORONOI_1D_PT_panel'
	bl_label = 'Delaunay Shot 1.0.2'
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = '1D'

	def draw(self, context):
		ui(
			layout=self.layout,
			context=context
		)


def register():
	register_class(DELAUNAY_VORONOI_1D_PT_panel)


def unregister():
	unregister_class(DELAUNAY_VORONOI_1D_PT_panel)
