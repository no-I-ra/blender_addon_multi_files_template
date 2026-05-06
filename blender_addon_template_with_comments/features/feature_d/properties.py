# **************************************************
# Feature D Properties
# **************************************************

import bpy
from bpy.props import BoolProperty

class NOIRATEMPLATE_PG_FeatureD(bpy.types.PropertyGroup):
    bool_ppty_d: BoolProperty(
        name="Boolean property",
        default=True
        ) # type: ignore



# Classes to registered/unregistered from features/feature_d/__init__.py
CLASSES = (
    NOIRATEMPLATE_PG_FeatureD,
)


# functions to registered/unregistered the proeprties from features/feature_d/__init__.py
def register_properties():
    bpy.types.Scene.feature_d_ppties = bpy.props.PointerProperty(
        type=NOIRATEMPLATE_PG_FeatureD
    )


def unregister_properties():
    del bpy.types.Scene.feature_d_ppties