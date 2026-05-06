# **************************************************
# Feature D Operators
# *************************************************

import bpy
from ...utils.addon_utils import get_addon_prefs
from . import properties

class NOIRATEMPLATE_OT_feature_d_tool1(bpy.types.Operator):
    bl_idname = "noiratemplate.feature_d_tool1"
    bl_label = "Feature D - Tool 1"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        active = context.active_object
        selected = [o for o in context.selected_objects if o != active]

        print(f"active: {active}")
        print(f"selected: {selected}")

        self.report({'INFO'}, 'Feature D - Tool 1')
        return {'FINISHED'}


class NOIRATEMPLATE_OT_feature_d_tool2(bpy.types.Operator):
    bl_idname = "noiratemplate.feature_d_tool2"
    bl_label = "Feature D - Tool 2"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, 'Feature D - Tool 2')
        return {'FINISHED'}


# Classes to registered/unregistered from features/feature_d/__init__.py
CLASSES = (
    NOIRATEMPLATE_OT_feature_d_tool1,
    NOIRATEMPLATE_OT_feature_d_tool2,
)

