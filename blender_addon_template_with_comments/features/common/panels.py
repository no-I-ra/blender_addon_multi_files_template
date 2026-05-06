# **************************************************
# Common Panels
# **************************************************

import bpy
from ...utils.addon_utils import get_addon_prefs
from . import properties

class NOIRATEMPLATE_PT_common_panel(bpy.types.Panel):
    bl_label = "Common Tools"
    bl_idname = "NOIRATEMPLATE_PT_common_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Studio Noira"

    @classmethod
    def poll(cls, context):
        prefs = get_addon_prefs(context)
        return prefs.enable_common

    def draw(self, context):
        layout = self.layout
        layout.operator("noiratemplate.common_tool1")

# Classes to registered/unregistered from features/feature_a/__init__.py
CLASSES = (
    NOIRATEMPLATE_PT_common_panel,
)
