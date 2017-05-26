# import chimera
# from chimera import runCommand as rc
# from chimera import replyobj
# import os
# file_names = [fn for fn in os.listdir(".") if fn.endswith(".pdb")]
# for fn in file_names:
#        rc("open template.pdb")
#        rc("open " + fn)
#        rc("del ~:.A")
#        # rc("match #1:I3P@C= #0:I3P@C=")
#        rc("close #0")
#        rc("~display")
#        rc("display :I3P")
#        rc("color purple :I3P")
#        rc("color byhet :I3P")
#        rc("color grey ~:I3P")
#        rc("align :I3P ~:I3P")
#        rc("~ribbon")
#        rc("surf protein")
#        rc("set bg_color white")
#        rc("set silhouette")
#        rc("transparency 80,s")
#        rc("lighting key specular_intensity 0.0")
#        # rc("matrixset matrixget")
#        # rc("scale 0.5")
#        png_name = fn[:-3] + "png"
#        rc("copy file " + png_name + " supersample 3")
#        rc("close all")
# #rc("stop now")

import chimera
from chimera import runCommand as rc
from chimera import replyobj
import os
os.chdir('aligned/')
rc("scale 1.5")
file_names = [fn for fn in os.listdir(".") if fn.endswith(".pdb")]
for fn in file_names:
    print "Opening... " + fn
    rc("open " + fn)
    if fn == file_names[0]:
        rc("scale 1.5")

    rc("~display")
    rc("display :I3P")
    rc("~ribbon")
    rc("color grey")
    rc("color green :I3P")
    rc("color byhet :I3P")
    rc("cofr :I3P")
    rc("sel :I3P zr<5")
    rc("display sel")
    rc("~display @=.B")
    rc("color byhet sel")
    # rc("transparency 80")
    rc("~sel")
    rc("transparency 0 :I3P")
    rc("matrixset matrixget")
    png_name = fn[:-3] + "png"
    rc("copy file " + png_name + " supersample 3")
    rc("close all")
# rc("surface protein")
# rc("align :I3P protein")