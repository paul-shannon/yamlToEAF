import re
import sys
sys.path.append("/Users/paul/github/slexil")
from text import *
from audioExtractor import *
import importlib
import os
import pdb
#----------------------------------------------------------------------------------------------------
pd.set_option('display.width', 1000)
#----------------------------------------------------------------------------------------------------
if(len(sys.argv) != 7):
    print("usage: eafToWepabe.py <eafFile>  <soundFile>  <audioPhrasesTargetDirectory> <tierGuideFile.yaml> <grammaticalTermsFile> <projectDirectory>")
    sys.exit(0)

elanXmlFilename= sys.argv[1]
soundFile = sys.argv[2] 
audioPhrasesTargetDirectory = sys.argv[3]

tierGuideFile = sys.argv[4]
grammaticalTermsFile = sys.argv[5]
projectDirectory = sys.argv[6]

assert(os.path.isfile(soundFile))
assert(os.path.isfile(elanXmlFilename))
assert(os.path.isdir(audioPhrasesTargetDirectory))
assert(os.path.isfile(soundFile))
assert(os.path.isdir(projectDirectory))
assert(os.path.isfile(tierGuideFile))
assert(os.path.isfile(grammaticalTermsFile))

# todo (31 jul 2019): pass audioPhrasesTargetDirectory to Text, so that its toHTML method can
# todo (31 jul 2019): use it, rather than currently hard-coded "audio/".

text = Text(elanXmlFilename,
	    soundFile,
	    grammaticalTermsFile=grammaticalTermsFile,
	    tierGuideFile=tierGuideFile,
	    projectDirectory=projectDirectory)

htmlText = text.toHTML()
filename = "daylight.html"
f = open(filename, "w")
f.write(indent(htmlText))
f.close()
display = True
if(display):
    os.system("open %s" % filename)
