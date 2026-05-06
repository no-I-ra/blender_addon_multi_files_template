# **************************************************
# Feature C > Sub-Feature A Properties
# **************************************************

import bpy
from bpy.props import BoolProperty

class NOIRATEMPLATE_PG_FeatureD(bpy.types.PropertyGroup):
    bool_ppty_d: BoolProperty(
        name="Boolean property D",
        default=True
        ) # type: ignore




# Classes to registered/unregistered from features/feature_a/__init__.py
CLASSES = (
    NOIRATEMPLATE_PG_FeatureD,
)


# functions to registered/unregistered the proeprties from features/feature_c/sub_a/__init__.py
def register_properties():
    bpy.types.Scene.sub_a_ppties = bpy.props.PointerProperty(
        type=NOIRATEMPLATE_PG_FeatureD
    )


def unregister_properties():
    del bpy.types.Scene.sub_a_ppties