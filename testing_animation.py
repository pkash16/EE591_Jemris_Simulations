# The following is a BLENDER script used on a 3D head object with an animation to export for JEMRIS.
# import the necessary modules we need
# in our case, blender's python API and python's os module

import bpy, os
from math import degrees

# get the current selection
selection = bpy.context.selected_objects
scene = bpy.context.scene
startFrame = scene.frame_start
endFrame = scene.frame_end
currentFrame = scene.frame_current

# get path to render output (usually /tmp\)
tempFolder = os.path.abspath (bpy.context.scene.render.filepath)
# make a filename
filename = os.path.join (tempFolder, "headrotation_fast.dat")
# open a file to write to
file = open(filename, "w")

FRAME_RATE = 1/60
SPEED_MULTIPLIER = 1000

# iterate through the selected objects
for sel in selection:
    #cycle trough all the animated frames
    for i in range(endFrame-startFrame+1):
        #get true frame number
        frame = i + startFrame
        #set frame and get the object's rotation
        scene.frame_set(frame)
        rot = sel.rotation_euler
        #file.write("%s - frame %d - X:%f Y:%f Z:%f \n" % (sel.name, frame, degrees(rot.x), degrees(rot.y), degrees(rot.z)))
        file.write("%f   %f   %f   %f   %f   %f   %f\n" % ((frame*SPEED_MULTIPLIER*FRAME_RATE), 0, 0, 0, degrees(rot.x), degrees(rot.y), degrees(rot.z)))
# close the file
file.close()

#restore original frame (not necessary)
scene.frame_set(currentFrame)