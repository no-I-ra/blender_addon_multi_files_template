# **************************************************
# Feature B Panels
# **************************************************



import bpy
from ...utils.addon_utils import get_addon_prefs
from . import properties


class FEATUREB_UL_object_list(bpy.types.UIList):
    """UIList for Feature B objects"""
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        obj = item.obj
        if obj:
            layout.label(text=obj.name, icon='OBJECT_DATA')
        else:
            layout.label(text="None", icon='ERROR')


class NOIRATEMPLATE_PT_feature_b_panel(bpy.types.Panel):
    bl_label = "Feature B Tools"
    bl_idname = "NOIRATEMPLATE_PT_feature_b_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Studio Noira"

    @classmethod
    def poll(cls, context):
        prefs = get_addon_prefs(context)
        return prefs.enable_feature_b

    def draw(self, context):
        layout = self.layout
        props = context.scene.feature_b_ppties

        # Boolean
        layout.prop(props, "bool_ppty")
        layout.operator("noiratemplate.feature_b_tool1")

        layout.separator()        

        # String
        layout.prop(props, "str_ppty")

        # Integer
        layout.prop(props, "int_ppty")

        # Float
        layout.prop(props, "float_ppty")


        layout.separator()
        # Enum
        layout.prop(props, "enum_ppty")
        layout.label(text=f"Selected Enum: {props.enum_ppty}")

        layout.separator()

        # CollectionProperty
        # Display collection with active index
        layout.template_list(
            "FEATUREB_UL_object_list",
            "object_collection_list",
            props,
            "object_collection",
            props,
            "object_index",
            rows=4
        )

        # Buttons
        row = layout.row()
        row.operator("feature_b.add_selected_objects", text="Add Selected")
        row.operator("feature_b.remove_object", text="Remove")

        layout.separator()

        # Nested PointerProperty
        if props.nested_ppty is not None:
            box = layout.box()
            box.label(text=f"Nested Bool: {props.nested_ppty.nested_bool}")



# Classes to registered/unregistered from features/feature_b/__init__.py
CLASSES = (
    FEATUREB_UL_object_list,
    NOIRATEMPLATE_PT_feature_b_panel,
)