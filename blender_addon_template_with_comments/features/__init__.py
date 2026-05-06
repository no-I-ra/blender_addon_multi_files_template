# **************************************************
# Register All Features of the addons
# **************************************************



# --------------------------------------------------
# IMPORT
# --------------------------------------------------

# Handle reload
if "common" in locals(): # register common features first as it can be used by other features, like sub-panels for example
    import importlib
    importlib.reload(common)
else:
    from . import common

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

if "feature_c" in locals():
    import importlib
    importlib.reload(feature_c)
else:
    from . import feature_c

if "feature_d" in locals():
    import importlib
    importlib.reload(feature_d)
else:
    from . import feature_d




# --------------------------------------------------
# REGISTER
# --------------------------------------------------

# All addon features that have been defined in sub-folders and need to be registered/unregistered
FEATURES = (
    common, 
    feature_a,
    feature_b,
    feature_c,
    feature_d,
)


def register():
    for feature in FEATURES:
        feature.register() # register each feature from features/<FEATURE_NAME>/__init__.py register()


def unregister():
    for feature in reversed(FEATURES): # Importtant to unregister in reverse order.
        feature.unregister() # unregister each feature from features/<FEATURE_NAME>/__init__.py unregister()