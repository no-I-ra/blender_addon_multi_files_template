# **************************************************
# Addon Common Operators
# *************************************************

import bpy
from ...utils.addon_utils import get_addon_prefs
from . import properties

class NOIRATEMPLATE_OT_common_tool1(bpy.types.Operator):
    bl_idname = "noiratemplate.common_tool1"
    bl_label = "Common - Tool 1"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, 'Common - Tool 1')
        return {'FINISHED'}


# Classes to registered/unregistered from features/__init__.py
CLASSES = (
    NOIRATEMPLATE_OT_common_tool1,
)


