import os
import pyscreenshot as ImageGrab
from datetime import datetime
from pathlib import Path
from PIL import Image
import imagehash
import cli_args

# arguments
cli_args.from_file('./schema.json')
argv = cli_args.argv


# variable
date = datetime.now()
scriptPath = str(Path.cwd())

# -- last image hash store is here
hashFile = argv['hashFile'] if argv['hashFile'] else "hash.txt"

# --day=%Y/%m/%d
dayPath = date.strftime(
    argv['day']) if argv['day'] else date.strftime("%Y/%m/%d")

# --filename=%H:%M:%S
filename = date.strftime(
    date.strftime(argv['filename'])) if argv['filename'] else date.strftime("%H:%M:%S")

# --defaultPath=/home/screensoot
argDefaultPath = argv['defaultPath'] + "/" if (
    argv['defaultPath'] and not argv['defaultPath'].endswith("/")) else ""


targetPath = argDefaultPath if argDefaultPath != "" else scriptPath+"/screenshoot/"

basePath = os.path.join(targetPath, dayPath+"/")

finalName = basePath+filename+".png"

# If the path you specified does not exist, it creates.
if not (os.path.exists(basePath)):
    os.makedirs(basePath)

if not (os.path.exists(hashFile)):
    open(hashFile, "w").write("")

    # grab and save screenshoot
im = ImageGrab.grab()
im.save(finalName)

# Retrieves hashes of recently saved and newly created images
newHashData = str(imagehash.average_hash(Image.open(finalName)))
oldHashData = open(hashFile).read()

# check hash
if(oldHashData == newHashData):
    # deletes the picture if it was previously saved
    os.remove(finalName)
else:
    # saves the hash in hash.txt if the image has not been saved before
    open(hashFile, "w").write(str(newHashData))
