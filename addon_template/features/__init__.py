if "feature_a" in locals():
    import importlib
    importlib.reload(feature_a)
else:
    from . import feature_a



FEATURES = (
    feature_a,
)



def register():
    for feature in FEATURES:
        feature.register()

def unregister():
    for feature in reversed(FEATURES):
        feature.unregister()