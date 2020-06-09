# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_delaunay_voronoi
#

import bpy
from bpy.types import Operator
from bpy_extras.view3d_utils import location_3d_to_region_2d
from bpy_extras.object_utils import world_to_camera_view
import bmesh
from .DelaunayVoronoi import computeDelaunayTriangulation


class Point:
	def __init__(self, x, y):
		self.x, self.y = x, y


class DELAUNAY_VORONOI_1D_OT_triangulate(Operator):
	bl_idname = 'delaunay_voronoy_1d.triangulate_view'
	bl_label = 'Delaunay Shot'
	bl_description = 'Triangulate by Delaunay Voronoi (project from view)'
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		obj = bpy.context.active_object
		mesh = obj.data
		if obj.mode == 'EDIT':
			bpy.ops.object.mode_set(mode='OBJECT')
		selected_vertices = [vertex for vertex in mesh.vertices if vertex.select]
		selected_vertices_id = [vertex.index for vertex in mesh.vertices if vertex.select]
		bpy.ops.object.mode_set(mode='EDIT')
		if len(selected_vertices) < 3:
			print('Less 3 vertices selected')
			return {'FINISHED'}
		if context.window_manager.delaunay_voronoi_1d_opts.remove_geometry:
			# remove existed geometry (only edges and faces)
			bpy.ops.mesh.delete(type='EDGE_FACE')
			bpy.ops.object.mode_set(mode='OBJECT')
			for vertex_id in selected_vertices_id:
				mesh.vertices[vertex_id].select = True
			# refresh selected vertices list - need to prevent crash, selected vertices before bpy.ops.mesh.delete breaks because this operator doesn't save selection
			selected_vertices = [vertex for vertex in mesh.vertices if vertex.select]
			bpy.ops.object.mode_set(mode='EDIT')
		if context.window_manager.delaunay_voronoi_1d_opts.projection == 'Camera':
			# projection to active camera
			vertices_viewport_projecton = [world_to_camera_view(context.scene, context.scene.camera, vertex.co) for vertex in selected_vertices]
		else:
			# projection to viewport
			vertices_viewport_projecton = [location_3d_to_region_2d(context.region, context.space_data.region_3d, obj.matrix_world * vertex.co) for vertex in selected_vertices]
		verts_points = [Point(vertex.x, vertex.y) for vertex in vertices_viewport_projecton]
		triangles=computeDelaunayTriangulation(verts_points)
		triangles=[tuple(reversed(tri)) for tri in triangles]    # reverse for normals consistence
		# build new faces
		bm = bmesh.from_edit_mesh(mesh)
		bm.verts.ensure_lookup_table()
		for triangle in triangles:
			v0 = bm.verts[selected_vertices_id[triangle[0]]]
			v1 = bm.verts[selected_vertices_id[triangle[1]]]
			v2 = bm.verts[selected_vertices_id[triangle[2]]]
			face = bm.faces.new([v0, v1, v2])
			face.select = True
			# set active material to new face
			face.material_index = context.object.active_material_index
		bmesh.update_edit_mesh(mesh)
		bm.free()
		# recalculate normals
		bpy.ops.mesh.normals_make_consistent(inside=False)
		return {'FINISHED'}

	@classmethod
	def poll(cls, context):
		if context.active_object and context.active_object.type == 'MESH' and context.active_object.mode == 'EDIT':
			return True
		return False


def register():
	bpy.utils.register_class(DELAUNAY_VORONOI_1D_OT_triangulate)


def unregister():
	bpy.utils.unregister_class(DELAUNAY_VORONOI_1D_OT_triangulate)
