# **************************************************
# Feature C Properties
# **************************************************

import bpy
from bpy.props import BoolProperty

class NOIRATEMPLATE_PG_FeatureC(bpy.types.PropertyGroup):
    bool_ppty_c: BoolProperty(
        name="Boolean property C",
        default=True
        ) # type: ignore



# Classes to registered/unregistered from features/feature_c/__init__.py
CLASSES = (
    NOIRATEMPLATE_PG_FeatureC,
)


# functions to registered/unregistered the proeprties from features/feature_c/__init__.py
def register_properties():
    bpy.types.Scene.feature_c_ppties = bpy.props.PointerProperty(
        type=NOIRATEMPLATE_PG_FeatureC
    )


def unregister_properties():
    del bpy.types.Scene.feature_c_ppties