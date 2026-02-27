# **************************************************
# Register All Features of the addons
# **************************************************



# --------------------------------------------------
# IMPORT
# --------------------------------------------------

# Handle reload
if "feature_a" in locals():
    import importlib
    importlib.reload(feature_a)
else:
    from . import feature_a

if "feature_b" in locals():
    import importlib
    importlib.reload(feature_b)
else:
    from . import feature_b



# --------------------------------------------------
# REGISTER
# --------------------------------------------------

# All addon features that have been defined in sub-folders and need to be registered/unregistered
FEATURES = (
    feature_a,
    feature_b,
)


def register():
    for feature in FEATURES:
        feature.register() # register each feature from features/<FEATURE_NAME>/__init__.py register()


def unregister():
    for feature in reversed(FEATURES): # Importtant to unregister in reverse order.
        feature.unregister() # unregister each feature from features/<FEATURE_NAME>/__init__.py unregister()