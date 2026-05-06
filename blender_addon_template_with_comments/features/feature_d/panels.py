# **************************************************
# Feature D Panels
# **************************************************

import bpy
from ...utils.addon_utils import get_addon_prefs
from . import properties

# --------------------------------------------------
# PANEL VIEW_3D
# --------------------------------------------------

class NOIRATEMPLATE_PT_feature_d_panel(bpy.types.Panel):
    bl_label = "Feature D Tools"
    bl_idname = "NOIRATEMPLATE_PT_feature_d_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Studio Noira"

    @classmethod
    def poll(cls, context):
        prefs = get_addon_prefs(context)
        return prefs.enable_feature_d

    def draw(self, context):
        layout = self.layout
        layout.operator("noiratemplate.feature_d_tool1")


# --------------------------------------------------
# PANEL OBJECT PROPERTIES
# --------------------------------------------------

class NOIRATEMPLATE_PT_feature_d_mesh_obj_ppties(bpy.types.Panel):
    bl_label = "Feature D - Object Properties"
    bl_idname = "NOIRATEMPLATE_PT_feature_d_mesh_obj_ppties"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'object'

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        obj = context.object

        layout.prop(obj, "name")

class NOIRATEMPLATE_PT_feature_d_mesh_data_ppties(bpy.types.Panel):
    bl_label = "Feature D - Data Properties"
    bl_idname = "NOIRATEMPLATE_PT_feature_d_mesh_data_ppties"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'data'

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        obj = context.object.data

        layout.prop(obj, "name")



# --------------------------------------------------
# CLASSES TO REGISTER
# --------------------------------------------------

# Classes to registered/unregistered from features/feature_d/__init__.py
CLASSES = (
    NOIRATEMPLATE_PT_feature_d_panel,
    NOIRATEMPLATE_PT_feature_d_mesh_obj_ppties,
    NOIRATEMPLATE_PT_feature_d_mesh_data_ppties,

)