# # **************************************************
# # Feature D Context Menus
# # **************************************************

# import bpy
# from ...utils.addon_utils import get_addon_prefs
# from . import properties


# def draw_object_context_menu(self, context):
#     layout = self.layout
#     layout.operator("noiratemplate.feature_d_tool2")

# def draw_edit_mesh_context_menu(self, context):
#     layout = self.layout

#     layout.separator()
#     layout.operator(
#         "noiratemplate.feature_d_tool1",
#         text="Feature D - Edit Tool",
#         icon='EDITMODE_HLT'
#     )

# def register():
#     bpy.types.VIEW3D_MT_object_context_menu.append(draw_object_context_menu) # register Blender's context menu available in 'OBJECT' Mode
#     bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(draw_edit_mesh_context_menu)  # register Blender's context menu available in 'EDIT_MESH' Mode

# def unregister():

#     bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(draw_edit_mesh_context_menu)  # unregister Blender's context menu available in 'EDIT' Mode
#     bpy.types.VIEW3D_MT_object_context_menu.remove(draw_object_context_menu) # unregister Blender's context menu available in 'OBJECT' Mode



import bpy


def draw_object_context_menu(self, context):
    layout = self.layout
    layout.separator()
    layout.operator("noiratemplate.feature_d_tool2", icon='TOOL_SETTINGS')

def draw_edit_mesh_context_menu(self, context):
    layout = self.layout

    layout.separator()
    layout.operator(
        "noiratemplate.feature_d_tool1",
        text="Feature D - Edit Tool",
        icon='EDITMODE_HLT'
    )

MENUS = (
    ("VIEW3D_MT_object_context_menu", draw_object_context_menu),
    ("VIEW3D_MT_edit_mesh_context_menu", draw_edit_mesh_context_menu),
)


def register():
    for menu_id, func in MENUS:
        getattr(bpy.types, menu_id).append(func)


def unregister():
    for menu_id, func in MENUS:
        getattr(bpy.types, menu_id).remove(func)
