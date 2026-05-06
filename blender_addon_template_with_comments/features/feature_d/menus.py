# **************************************************
# Feature D Context Menus
# **************************************************

import bpy
from ...utils.addon_utils import get_addon_prefs
from . import properties


# --------------------------------------------------
# CONTEXT MENUS
# --------------------------------------------------

def draw_object_context_menu(self, context):
    '''
    Tool in Context Menu in 'OBJECT' mode
    '''

    # Shows up only if enable_feature_d from  the addon preferences properties is True 
    prefs = get_addon_prefs(context)
    if not prefs.enable_feature_d:
        return

    layout = self.layout
    layout.separator()
    layout.operator("noiratemplate.feature_d_tool1", text="Context Menu OBJECT mode", icon='TOOL_SETTINGS')

def draw_edit_mesh_context_menu(self, context):
    '''
    Tool in Context Menu in 'OBJECT' mode
    '''

    # Shows up only if enable_feature_d from  the addon preferences properties is True 
    prefs = get_addon_prefs(context)
    if not prefs.enable_feature_d:
        return


    layout = self.layout
    layout.separator()
    layout.operator("noiratemplate.feature_d_tool2", text="Context Menu EDIT mode", icon='EDITMODE_HLT')



# --------------------------------------------------
# TOOLBAR MENUS
# --------------------------------------------------

def draw_object_header(self, context):
    prefs = get_addon_prefs(context)
    if not prefs.enable_feature_d:
        return

    layout = self.layout
    layout.separator()
    layout.operator("noiratemplate.feature_d_tool1", text="CUSTOM MENU", icon="COLLECTION_COLOR_03")

def draw_edit_mesh_header(self, context):
    prefs = get_addon_prefs(context)
    if not prefs.enable_feature_d:
        return

    layout = self.layout
    layout.separator()
    layout.operator("noiratemplate.feature_d_tool2", text="Feature D - Tool 2")




# --------------------------------------------------
# CLASSES TO REGISTER
# --------------------------------------------------

MENUS = (
    ("VIEW3D_MT_object_context_menu", draw_object_context_menu),
    ("VIEW3D_MT_edit_mesh_context_menu", draw_edit_mesh_context_menu),
)

HEADERS = (

    # Mode 'OBJECT' Toolbar menu
    ("VIEW3D_MT_editor_menus", draw_object_header), # Menu 'Object'
    
   
    # ("VIEW3D_MT_object", draw_object_header), # Menu 'Object'
    # ("VIEW3D_MT_select_object", draw_object_header), # Menu 'Select'

    # Mode 'EDIT_MESH' Toolbar menu
    # ("VIEW3D_MT_edit_mesh", draw_edit_mesh_header), # Menu 'Mesh'
)