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
    *menus.MENUS,
    *menus.HEADERS,
)



def register():

    for cls in CLASSES:
        bpy.utils.register_class(cls) # register each class from feature_d

    if hasattr(properties, "register_properties"):
        properties.register_properties() # register properties from feature_d

    for menu_id, func in MENUS:
        menu = getattr(bpy.types, menu_id)
        menu.remove(func) # ensure the menu appends only once
        menu.append(func)


    for menu_id, func in MENUS:
        menu = getattr(bpy.types, menu_id)

        if(not menu.remove(func)):
            menu.append(func)

def unregister():

    for menu_id, func in MENUS:
        getattr(bpy.types, menu_id).remove(func)

    if hasattr(properties, "unregister_properties"):
        properties.unregister_properties() # unregister properties from feature_d

    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls) # unregister each class from feature_d