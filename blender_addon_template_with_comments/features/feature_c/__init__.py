# **************************************************
# Register Feature C classes
# **************************************************


# --------------------------------------------------
# IMPORT
# --------------------------------------------------

import bpy

from . import operators
from . import panels
from . import properties


# Handle reload of sub-features
if "feature_d" in locals():
    import importlib
    importlib.reload(feature_d)
else:
    from . import feature_d

# --------------------------------------------------
# REGISTER
# --------------------------------------------------

# Classes to register. ORDER MATTERS!
CLASSES = (
    *properties.CLASSES, # from features/feature_c/properties.py
    *operators.CLASSES, # from features/feature_c/operators.py
    *panels.CLASSES,  # from features/feature_c/panels.py   
)

# Su-features to register
SUB_FEATURES = (
    feature_d,
)

def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls) # register each class from feature_c

    if hasattr(properties, "register_properties"):
        properties.register_properties() # register properties from feature_c

    for sub in SUB_FEATURES: # register sub-features of feature_c
        sub.register()

def unregister():

    for sub in reversed(SUB_FEATURES): # unregister sub-features of feature_c
        sub.unregister()

    if hasattr(properties, "unregister_properties"):
        properties.unregister_properties() # unregister properties from feature_c

    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls) # unregister each class from feature_c