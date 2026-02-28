# Blender python addon template
A multi-file Blender addon template designed to help organize features, operators, panels, and properties in a clean, scalable way.
Compatibility tested with Blender 4.x and 5.x.

This template demonstrates best practices for:
* Structuring addon features in separate folders
* Using PropertyGroup, PointerProperty, and CollectionProperty
* Organizing operators, panels, and properties per feature
* Reload-safe registration
* Maintaining readable and maintainable code

Files are commented for clarity, and a Visual Studio solution is included for easier development.

Two templates are available:
* blender_addon_template_with_comments: template with two features and comments. Use it to understand how it works.
* addon_template: template without any comment and only one feature. Use it as a base to build your own addon.

The current templates add panels in the View_3D side view. 
Templates to customize other Blender's UI areas will come later.


# How to customize the template
* Use addon_template as a base and rename the folder to match with your addon name.
* Change the bl_info in the main __init__.py file.
* Rename the prefixes "NOIRATEMPLATE" and "noiratemplate." that are used in classes to match with your addon name.
* Change the "bl_category" of panels to match with your addon.
* Rename "features/feature_a" folder and its file content to match with your addon features. Duplicate it to add another feature.
* Update features/__init__.py to add all the feature classes your addon implements to "FEATURES = ()". Add an import reload for each feature as well.



# Contributing & Improvements
This template was created based on my current knowledge of Blender’s Python API and multi-file addon structure.

I would be glad if others could:
 * Try it out in their projects
 * Suggest improvements for registration, property handling, or folder structure
 * Share best practices for building scalable Blender addons
 * Open pull requests, issues, or discussions to help improve the template

Your contributions and feedback are very welcome!
