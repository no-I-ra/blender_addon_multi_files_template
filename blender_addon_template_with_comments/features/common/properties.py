# **************************************************
# Commonn Properties
# **************************************************

import bpy
from bpy.props import BoolProperty

class NOIRATEMPLATE_CommonProperties(bpy.types.PropertyGroup):
    bool_ppty: BoolProperty(
        name="Boolean property",
        default=True
        ) # type: ignore



# Classes to registered/unregistered from features/feature_a/__init__.py
CLASSES = (
    NOIRATEMPLATE_CommonProperties,
)


# functions to registered/unregistered the proeprties from features/feature_a/__init__.py
def register_properties():

    bpy.types.Scene.feature_a_ppties = bpy.props.PointerProperty(
        type=NOIRATEMPLATE_CommonProperties
    )


def unregister_properties():
    del bpy.types.Scene.feature_a_ppties
