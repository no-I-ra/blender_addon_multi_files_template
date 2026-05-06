# **************************************************
# Feature D Panels
# **************************************************

import bpy
from ...utils.addon_utils import get_addon_prefs
from . import properties

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


# Context menu In Object Mode (bpy.types.VIEW3D_MT_object_context_menu)
def draw_object_context_menu(self, context):
    layout = self.layout

    layout.separator()
    layout.operator("noiratemplate.feature_d_tool2", icon='TOOL_SETTINGS')

# Classes to registered/unregistered from features/feature_d/__init__.py
CLASSES = (
    NOIRATEMPLATE_PT_feature_d_panel,
)