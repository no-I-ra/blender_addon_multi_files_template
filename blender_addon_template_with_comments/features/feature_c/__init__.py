# **************************************************
# Register Feature C classes
# **************************************************


# --------------------------------------------------
# IMPORT
# --------------------------------------------------

# # Handle reload
# if "feature_d" in locals():
#     import importlib
#     importlib.reload(feature_d)
# else:
#     from . import feature_d


import bpy

from . import operators
from . import panels
from . import properties







# --------------------------------------------------
# REGISTER
# --------------------------------------------------

# Classes to register. ORDER MATTERS!
CLASSES = (
    *properties.CLASSES, # from features/feature_c/properties.py
    *operators.CLASSES, # from features/feature_c/operators.py
    *panels.CLASSES,  # from features/feature_c/panels.py   
)

# # Feature C sub-features that have been defined in its sub-folders and need to be registered/unregistered
# FEATURES = (
#     feature_d,
# )


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls) # register each class from feature_c

    if hasattr(properties, "register_properties"):
        properties.register_properties() # register properties from feature_c

    # for feature in FEATURES:
    #     feature.register() # register each feature from features/feature_c/<FEATURE_NAME>/__init__.py register()

    

def unregister():

    # for feature in reversed(FEATURES): # Importtant to unregister in reverse order.
    #     feature.unregister() # unregister each feature from features/feature_c/<FEATURE_NAME>/__init__.py unregister()

    if hasattr(properties, "unregister_properties"):
        properties.unregister_properties() # unregister properties from feature_c

    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls) # unregister each class from feature_c