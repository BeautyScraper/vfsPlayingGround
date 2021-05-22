import re
from glob import glob
import os
import pathlib
from pathlib import Path
import shutil

def createVideoFromImageDir(imageDir, outputFiledirPath):
    if Path("video.mp4").is_file():
        Path("video.mp4").unlink()
    oldcwd = Path.cwd()
    if not imageDir.is_dir():
        return
    os.system('cd %s' % str(imageDir.parent))
    if not createImagelistfile(imageDir, Path('list.tmp')):
        os.system('rd /s/q "%s" ' % imageDir.parent)
        return
    os.system("D:\Developed\VFS\RandyVideo\makeVideo.bat")
    outputFilePath = outputFiledirPath / (imageDir.parent.name + '.mp4')
    shutil.copy("video.mp4", str(outputFilePath))
    Path("video.mp4").unlink()
    os.system('cd %s' % str(oldcwd))
    # import pdb;pdb.set_trace()
    os.system('rd /s/q "%s" ' % imageDir.parent)
    # imageDir.parent.rmdir()

def createImagelistfile(srcVideoimgDirPath, imageFile):
    imageList = []
    for imgFP in srcVideoimgDirPath.glob('*.jpg'):
        fileLine = "file 'file:%s'\n" % imgFP.as_posix() 
        imageList.append(fileLine)
        # import pdb;pdb.set_trace()
    if imageList == []:
        return False
    with open(imageFile,'w') as fp:
        fp.writelines(imageList)
    return True

def main():
    FSvideoDirs = Path.cwd().glob('*\\yummy\\')
    outputFiledirPath = Path.cwd() / 'xdivision'
    for fsdir in FSvideoDirs:
        print(str(fsdir))
        unfswapped = [x for x in fsdir.parent.glob('*.jpg')]
        if unfswapped != []:
            continue
        # import pdb;pdb.set_trace()
        createVideoFromImageDir(fsdir,outputFiledirPath)
main()
        
        
    