# **************************************************
# Feature B Operators
# *************************************************

import bpy
from ...utils.addon_utils import get_addon_prefs
from . import properties

class NOIRATEMPLATE_OT_feature_b_tool1(bpy.types.Operator):
    bl_idname = "noiratemplate.feature_b_tool1"
    bl_label = "Feature B - Tool 1"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, 'Feature B - Tool 1')
        return {'FINISHED'}


class NOIRATEMPLATE_OT_feature_b_tool2(bpy.types.Operator):
    bl_idname = "noiratemplate.feature_b_tool2"
    bl_label = "Feature B - Tool 2"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        props = context.scene.feature_b_ppties
        self.report({'INFO'}, f"Property bool_ppty is {props.bool_ppty}")

        return {'FINISHED'}

class FEATUREB_OT_add_selected_objects(bpy.types.Operator):
    bl_idname = "feature_b.add_selected_objects"
    bl_label = "Add Selected Objects"

    def execute(self, context):
        props = context.scene.feature_b_ppties
        selected_objects = context.selected_objects

        for obj in selected_objects:
            # Avoid duplicates
            if any(item.obj == obj for item in props.object_collection):
                continue
            item = props.object_collection.add()
            item.obj = obj

        props.object_index = len(props.object_collection) - 1
        return {'FINISHED'}


class FEATUREB_OT_remove_object(bpy.types.Operator):
    bl_idname = "feature_b.remove_object"
    bl_label = "Remove Object"

    def execute(self, context):
        props = context.scene.feature_b_ppties
        index = props.object_index
        if 0 <= index < len(props.object_collection):
            props.object_collection.remove(index)
            props.object_index = min(max(0, index - 1), len(props.object_collection) - 1)
        return {'FINISHED'}


# Classes to registered/unregistered from features/feature_b/__init__.py
CLASSES = (
    NOIRATEMPLATE_OT_feature_b_tool1,
    NOIRATEMPLATE_OT_feature_b_tool2,
    FEATUREB_OT_add_selected_objects,
    FEATUREB_OT_remove_object,
)

