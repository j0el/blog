# Write EXIF metadata to text file for pelican.photos plugin.
from fraction import Fraction
import os
from os import listdir
from os.path import isfile, join

import PIL
from PIL import Image
from PIL.ExifTags import GPSTAGS
from PIL.ExifTags import TAGS

# The first two functions are borrowed from github user @jpstroop
# https://gist.github.com/jpstroop/58a21d02370c8ba34dc8f0fdd4206d70


def _map_key(k):
    try:
        return TAGS[k]
    except KeyError:
        return GPSTAGS.get(k, k)

# Creates a dictionary of image EXIF meta data from an image, borrowed from a github gist
def get_exif(image_path):
    metadata = {}
    with Image.open(image_path) as i:
        info = i._getexif()
    try:
        [ metadata.__setitem__(_map_key(k), v) for k, v in info.items() ]
        return metadata
    except AttributeError:
        return None


def exposure(ExposureTime):
    try:
        return(str(Fraction(str(ExposureTime))))
    
    except:
        return('None')


#Creates a text file with some exif meta data.
def write_exif_file(directory):
    # Open the exif.txt file, create if it doesn't exist, in the current folder.
    txt = open(directory+'/exif.txt', 'w')

    for file in os.listdir(directory):

        # check the files which are end with specific extension
        # Everything that I want to have EXIF information for is a jpg, but you can add others too.
        if file.endswith(".jpg"):
            # Need to iterate through the files in the list and pass each to the 
            image = get_exif(directory +'/'+os.path.join(file))
            txt.write(
                os.path.join(file) + ': ' + 
                str(image.get('Model')) + 
                ' with a ' + str(image.get('LensModel')) + 
                ' - ' + exposure(image.get('ExposureTime')) + ' s, ' + # I want to change this to fractions, but it works for now.
                'f/' + str(image.get('FNumber')) + 
                ' at ISO-' +  str(image.get('ISOSpeedRatings')) + 
                '\n'
                )

    # Close the text file now that we are done with it.
    txt.close()
    return None

# The directory of the source photos, the same as PHOTO_LIBRARY in pelicanconf.py
# I run this in a WSL instance, but pelican is run on the host windows machine, hence the sample directory
dir = '/home/jberman/blog/content/galleries' 

# This walks through the directories and for each it calls the write exif file function
for root, subdirectories, files in os.walk(dir):
    for subdirectory in subdirectories:
       print(os.path.join(root, subdirectory))
       write_exif_file(os.path.join(root, subdirectory))

