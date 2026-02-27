# **************************************************
# Main file of the addon
# **************************************************

'''
Copyright (C) 2026 Studio Noira
studionoira@gmail.com

Created by Studio Noira

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''





# --------------------------------------------------
# ADDON INFO
# --------------------------------------------------
bl_info = {
    "name": "Multi files addon Template", # Name of the addon
    "author": "Studio Noira", # Addon's author name
    "version": (1, 0, 0), # Version of the addon
    "blender": (5, 0, 0), # Blender's version the addon is compatible with.
    "location": "Studio Noira > View3D > Sidebar", # Info - where to find the addon in Blender UI
    "category": "Studio Noira", # Category of the addon - filter in Blender > Preferences > Addon
}




# --------------------------------------------------
# IMPORT
# --------------------------------------------------
import bpy
from bpy.types import AddonPreferences
from bpy.props import BoolProperty

# # Use this if many submodules to load
# def reload_submodules(module_dict):
#     import importlib
#     for module in module_dict.values():
#         if hasattr(module, "__file__"):
#             importlib.reload(module)


# Handle reload
if "features" in locals():
    import importlib
    importlib.reload(features)
else:
    from . import features




# --------------------------------------------------
# ADDON PREFERENCES
# with a panel to set its options
# --------------------------------------------------
class NOIRATEMPLATE_Preferences(AddonPreferences):
    bl_idname = __name__

    enable_feature_a: BoolProperty(
        name="Enable Feature A Tools",
        default=True,
        description="Enable or disable the Feature A panel and operators"
    ) # type: ignore

    enable_feature_b: BoolProperty(
        name="Enable Feature B Tools",
        default=True,
        description="Enable or disable the Feature B panel and operators"
    ) # type: ignore

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Template addon Preferences")        
        col.prop(self, "enable_feature_a")
        col.prop(self, "enable_feature_b")




# --------------------------------------------------
# REGISTER
# --------------------------------------------------
def register():
    bpy.utils.register_class(NOIRATEMPLATE_Preferences) # Register preferences first.
    features.register() # register all features from features/__init__.py register()

def unregister():
    features.unregister() # unregister all features from features/__init__.py unregister()
    bpy.utils.unregister_class(NOIRATEMPLATE_Preferences)