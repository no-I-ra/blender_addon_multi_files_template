import bpy

def get_addon_prefs(context=None):
    '''
    Get the addon preferences
    '''
    if context is None:
        context = bpy.context

    addon_name = __package__.split(".")[0]
    return context.preferences.addons[addon_name].preferences