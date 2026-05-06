# **************************************************
# Feature C > Sub-Feature A Panels
# **************************************************

import bpy
from ....utils.addon_utils import get_addon_prefs
from . import properties

class NOIRATEMPLATE_PT_sub_a_panel(bpy.types.Panel):
    bl_label = "Sub-Feature A Tools"
    bl_idname = "NOIRATEMPLATE_PT_sub_a_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = "NOIRATEMPLATE_PT_feature_c_panel" # parent panel from feature c
    bl_category = "Studio Noira"

    def draw(self, context):
        layout = self.layout
        layout.operator("noiratemplate.sub_a_tool1")

# Classes to registered/unregistered from features/feature_c/sub_a/__init__.py
CLASSES = (
    NOIRATEMPLATE_PT_sub_a_panel,
)