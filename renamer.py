import re
from glob import glob
import os


def renameByThis(f):
    t = glob('*%s*' % f)
    for x in t:
        newName = x.replace(f,"")
        # import pdb;pdb.set_trace()
        if os.path.exists(newName):
            os.remove(newName)
        os.rename(x,newName)

renameByThis('Yummy @hudengi Frames4 W1t81N ')
renameByThis('BurDevi @hudengi Frames4 W1t81N ')
renameByThis('ChuchiDevi @hudengi Frames4 W1t81N ')