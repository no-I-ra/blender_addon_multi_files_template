# **************************************************
# Feature B Properties
# *************************************************

import bpy
from bpy.props import BoolProperty, StringProperty, IntProperty, FloatProperty, EnumProperty, PointerProperty, CollectionProperty


class NOIRATEMPLATE_PG_NestedProperties(bpy.types.PropertyGroup):
    nested_bool: BoolProperty(
        name="Nested Bool",
        default=True
        )  # type: ignore

class NOIRATEMPLATE_PG_FeatureB_ObjectItem(bpy.types.PropertyGroup):
    obj: PointerProperty(
        name="Object",
        type=bpy.types.Object
    ) # type: ignore

class NOIRATEMPLATE_PG_FeatureBProperties(bpy.types.PropertyGroup):
    # Boolean
    bool_ppty: BoolProperty(
        name="Boolean property",
        description="A simple on/off boolean",
        default=True
    ) # type: ignore

    # String
    str_ppty: StringProperty(
        name="String property",
        description="A simple text string",
        default="This is a string property",
        maxlen=1024
    ) # type: ignore

    # Integer
    int_ppty: IntProperty(
        name="Integer property",
        description="A simple integer",
        default=10,
        min=0,
        max=100
    ) # type: ignore

    # Float
    float_ppty: FloatProperty(
        name="Float property",
        description="A simple floating-point number",
        default=1.0,
        min=0.0,
        max=10.0,
        precision=3
    ) # type: ignore

    # Enum
    enum_ppty: EnumProperty(
        name="Enum property",
        description="Choose an option",
        items=[
            ('OPT_A', "Option A", "Description of Option A"),
            ('OPT_B', "Option B", "Description of Option B"),
            ('OPT_C', "Option C", "Description of Option C"),
        ],
        default='OPT_A'
    ) # type: ignore


    # Collection of objects
    object_collection: CollectionProperty(
        name="Object Collection",
        type=NOIRATEMPLATE_PG_FeatureB_ObjectItem
    ) # type: ignore
    object_index: IntProperty(
        name="Active Object Index",
        default=0
    ) # type: ignore


    # Pointer to another PropertyGroup (example: nested properties)
    nested_ppty: PointerProperty(type=NOIRATEMPLATE_PG_NestedProperties) # type: ignore

    
    
# Classes to registered/unregistered from features/feature_b/__init__.py
CLASSES = (
    NOIRATEMPLATE_PG_NestedProperties,
    NOIRATEMPLATE_PG_FeatureB_ObjectItem,
    NOIRATEMPLATE_PG_FeatureBProperties,
)



# functions to registered/unregistered the proeprties from features/feature_b/__init__.py
def register_properties():
    bpy.types.Scene.feature_b_nested_ppties = bpy.props.PointerProperty(
        type=NOIRATEMPLATE_PG_NestedProperties
    )

    bpy.types.Scene.feature_b_ppties = bpy.props.PointerProperty(
        type=NOIRATEMPLATE_PG_FeatureBProperties
    )


def unregister_properties():
    del bpy.types.Scene.feature_b_ppties
    del bpy.types.Scene.feature_b_nested_ppties