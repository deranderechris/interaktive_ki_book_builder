[app]

# (str) Title of your application
name = Interactive Book Builder

# (str) Package name
package.name = interactivebookbuilder

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (str) The entrypoint to your application
entrypoint = kivy_app.py

# (list) Source files to include (let's include all py)
source.include_exts = py,png,jpg,jpeg,gif,webp

# (list) Requirements
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (str) Android permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (str) Python for android (p4a) branching
p4a.branch = master

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
