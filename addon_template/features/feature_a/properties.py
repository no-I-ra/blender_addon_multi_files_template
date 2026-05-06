import bpy
from bpy.props import BoolProperty

class NOIRATEMPLATE_PG_FeatureA(bpy.types.PropertyGroup):
    bool_ppty: BoolProperty(
        name="Boolean property",
        default=True
        )



CLASSES = (
    NOIRATEMPLATE_PG_FeatureA,
)



def register_properties():
    bpy.types.Scene.feature_a_ppties = bpy.props.PointerProperty(
        type=NOIRATEMPLATE_PG_FeatureA
    )


def unregister_properties():
    del bpy.types.Scene.feature_a_ppties