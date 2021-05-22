import re
from glob import glob
import os
import pathlib
from pathlib import Path


def extractFrames(filename):
    os.system('md "%s"' % filename.stem)
    CMDsTR = 'ffmpeg -i "%s"  -vsync 0 "%s/out-%%05d.jpg"' % (filename, filename.stem)
    os.system(CMDsTR)
    os.system('xcopy "%s" .\done\ && del  "%s"' % (filename,filename))
    # 2import pdb;pdb.set_trace()
    framesdir = Path.cwd() / filename.stem
    imagefiles = [1]
    while len(imagefiles) > 0:
        os.system('cd "%s" && call ..\\frames.bat && cd .. ' % filename.stem)
        imagefiles = [x for x in framesdir.glob('*.jpg')]

def getFileCount(dpath):
    if dpath.is_file():
        return 0
    return len([x for x in dpath.parent.glob('*.jp*g')])

def startFS(dpath):
    imagefiles = [1]
    while len(imagefiles) > 0:
        # import pdb;pdb.set_trace()
        os.system('cd "%s" && call ..\\framesCsv.bat && call ..\\frames.bat && cd .. ' % str(dpath))
        imagefiles = [x for x in dpath.glob('*.jpg')]

def doPrev():
    FSvideoDirs = Path.cwd().glob('*\\yummy\\')
    FSvideoDirs = sorted(FSvideoDirs, key=getFileCount )
    for fsdir in FSvideoDirs:
        startFS(fsdir.parent)
        

if __name__ == '__main__':    
    videoFiles = glob(".\\DoThis\\*")  
    for xx in videoFiles:
        xx = Path(xx)
        if xx.is_dir():
            continue
        extractFrames(xx)
    
    