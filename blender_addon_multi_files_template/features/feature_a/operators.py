# **************************************************
# Feature A Operators
# *************************************************

import bpy
from ...utils.addon_utils import get_addon_prefs
from . import properties

class NOIRATEMPLATE_OT_feature_a_tool1(bpy.types.Operator):
    bl_idname = "noiratemplate.feature_a_tool1"
    bl_label = "Feature A - Tool 1"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, 'Feature A - Tool 1')
        return {'FINISHED'}


# Classes to registered/unregistered from features/feature_a/__init__.py
CLASSES = (
    NOIRATEMPLATE_OT_feature_a_tool1,
)

