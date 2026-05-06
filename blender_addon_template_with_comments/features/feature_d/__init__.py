# **************************************************
# Register Feature D classes
# **************************************************


# --------------------------------------------------
# IMPORT
# --------------------------------------------------

import bpy

from . import operators
from . import panels
from . import properties
from . import menus

# --------------------------------------------------
# REGISTER
# --------------------------------------------------

# Classes to register. ORDER MATTERS!
CLASSES = (
    *properties.CLASSES, # from features/feature_d/properties.py
    *operators.CLASSES, # from features/feature_d/operators.py
    *panels.CLASSES,  # from features/feature_d/panels.py
)

MENUS = (
    menus,
)


def register():

    for cls in CLASSES:
        bpy.utils.register_class(cls) # register each class from feature_d

    if hasattr(properties, "register_properties"):
        properties.register_properties() # register properties from feature_d

    # register menus
    for menu in MENUS:
        if hasattr(menu, "register"):
            menu.register()

    

def unregister():

    # unregister menus first (important)
    for menu in reversed(MENUS):
        if hasattr(menu, "unregister"):
            menu.unregister()

    if hasattr(properties, "unregister_properties"):
        properties.unregister_properties() # unregister properties from feature_d

    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls) # unregister each class from feature_d