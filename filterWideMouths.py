import re
from pathlib import Path

thresh = 3.0
def getWeight(filePath): return float(re.search('^[\d\.]*',filePath.name)[0])
def outFilename(filePath): 
    tfilename = re.sub('^[^@]*@','',filePath.name)
    return tfilename

resultDir = Path.cwd() / 'kharab'
# resultDir.mkdir()
# xtr = [x for x in Path.cwd().glob('*.jpg')]
for xtr in Path.cwd().glob('*.jpg'):
    
    # print(xtr)
    if getWeight(xtr) < thresh:
        continue
    outDir = Path.cwd().parent / 'yummy'
    outfilepath = outDir / outFilename(xtr)
    resultFilepath = resultDir / outFilename(xtr)
    # import pdb;pdb.set_trace()
    print(outfilepath)
    if outfilepath.is_file():
        outfilepath.rename(resultFilepath)
        
fileNames = []