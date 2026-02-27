# **************************************************
# Feature A Properties
# **************************************************

import bpy
from bpy.props import BoolProperty

class NOIRATEMPLATE_FeatureAProperties(bpy.types.PropertyGroup):
    use_grid_snap: BoolProperty(
        name="Use Grid Snap", default=True
        ) # type: ignore



# Classes to registered/unregistered from features/feature_a/__init__.py
CLASSES = (
    NOIRATEMPLATE_FeatureAProperties,
)


# functions to registered/unregistered the proeprties from features/feature_a/__init__.py
def register_properties():
    bpy.types.Scene.feature_a_ppties = bpy.props.PointerProperty(
        type=NOIRATEMPLATE_FeatureAProperties
    )


def unregister_properties():
    del bpy.types.Scene.feature_a_ppties