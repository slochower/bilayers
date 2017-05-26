import chimera
from chimera import runCommand as rc
from chimera import replyobj
import os
file_names = [fn for fn in os.listdir(".") if fn.endswith(".pdb")]
for fn in file_names:
    print "Opening... " + fn
    rc("open " + fn)

# rc("del ~:.A")
rc("del :I3P@=.B")
rc("~display")
rc("display :I3P")
rc("~ribbon")
rc("color grey")
rc("color red #0:I3P")

models = chimera.openModels.list()
for m in models:
    print "Aligning... " + str(m) + " to... #0"
    try:
        rc("match " + str(m) + ":I3P.A@C= #0:I3P@C=") # Align chain A of target
    except:
        try:
            rc("match " + str(m) + ":I3P.B@C= #0:I3P@C=") # Align chain B of target
        except:
            rc("match " + str(m) + ":I3P@C=.A #0:I3P@C=") # Align primary position of target

# Get rid of the excess IP3 that are in other chains...
rc("sel #0:I3P zr>5 & :I3P")
# Maybe this will work. "sel up" doesn't.
rc("del sel")

# for m in models:
#     rc("write " + str(m) + " aligned/" + str(m) + ".pdb")


for m in models:
    name = m.name
    rc("write " + str(m) + " aligned/" + str(name) + ".pdb")