# **************************************************
# Register Feature B classes
# **************************************************


# --------------------------------------------------
# IMPORT
# --------------------------------------------------

import bpy

from . import operators
from . import panels
from . import properties



# --------------------------------------------------
# REGISTER
# --------------------------------------------------

# Classes to register. Order matters
CLASSES = (
    *properties.CLASSES, # from features/feature_b/properties.py
    *operators.CLASSES, # from features/feature_b/operators.py
    *panels.CLASSES,  # from features/feature_b/panels.py   
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls) # register each class from feature_b

    if hasattr(properties, "register_properties"):
        properties.register_properties() # register properties from feature_b

    

def unregister():

    if hasattr(properties, "unregister_properties"):
        properties.unregister_properties() # unregister properties from feature_b

    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls) # unregister each class from feature_b

    
