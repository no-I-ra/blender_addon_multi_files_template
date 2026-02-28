import bpy

from . import operators
from . import panels
from . import properties



CLASSES = (
    *properties.CLASSES,
    *operators.CLASSES,
    *panels.CLASSES,
)



def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)

    if hasattr(properties, "register_properties"):
        properties.register_properties()


def unregister():
    if hasattr(properties, "unregister_properties"):
        properties.unregister_properties()

    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)