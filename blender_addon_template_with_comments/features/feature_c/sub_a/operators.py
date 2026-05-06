# **************************************************
# Feature C > Sub-Feature A Operators
# *************************************************

import bpy
from ....utils.addon_utils import get_addon_prefs
from . import properties

class NOIRATEMPLATE_OT_sub_a_tool1(bpy.types.Operator):
    bl_idname = "noiratemplate.sub_a_tool1"
    bl_label = "Sub-Feature A - Tool 1"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        

        ppties_c = context.scene.feature_c_ppties # Get feature C properties
        print(f"bool_ppty_c (from feature C properties) value is: {ppties_c.bool_ppty_c}")


        self.report({'INFO'}, f"C > Sub-Feature A - Tool 1 | bool_ppty_c (from feature C properties) value is: {ppties_c.bool_ppty_c}")
        return {'FINISHED'}


# Classes to registered/unregistered from features/feature_c/sub_a/__init__.py
CLASSES = (
    NOIRATEMPLATE_OT_sub_a_tool1,
)

