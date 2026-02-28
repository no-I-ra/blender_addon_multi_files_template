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



bl_info = {
    "name": "Addon template",
    "author": "Author Name",
    "version": (1, 0, 0),
    "blender": (5, 0, 0),
    "location": "Template > View3D > Sidebar",
    "category": "",
}



import bpy
from bpy.types import AddonPreferences
from bpy.props import BoolProperty



if "features" in locals():
    import importlib
    importlib.reload(features)
else:
    from . import features



class NOIRATEMPLATE_Preferences(AddonPreferences):
    bl_idname = __name__

    enable_feature_a: BoolProperty(
        name="Enable Feature A Tools",
        default=True,
        description="Enable or disable the Feature A panel and operators"
    )

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Template addon Preferences")        
        col.prop(self, "enable_feature_a")



def register():
    bpy.utils.register_class(NOIRATEMPLATE_Preferences)
    features.register()

def unregister():
    features.unregister()
    bpy.utils.unregister_class(NOIRATEMPLATE_Preferences)