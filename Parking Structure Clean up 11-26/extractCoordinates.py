import xml.etree.ElementTree as ET
import os
from exif import Image
import json

def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == "S" or ref == "W":
        decimal_degrees = -decimal_degrees
    return decimal_degrees

def get_coordinates(image_path):
        with open(image_path, 'rb') as src:
            img = Image(src)
            if img.has_exif:
                lon = decimal_coords(img.gps_longitude, img.gps_longitude_ref)
                lat = decimal_coords(img.gps_latitude, img.gps_latitude_ref)
                return {'lon':lon,'lat':lat}
            else:
                print(image_path + " has no exif")
                return {'lon':0,'lat':0}

def writeToJson(file, trash):
    with open(output_file, 'a', encoding='utf-8') as outFile:
        print("Saved in " + str(output_file))
        outFile.write(json.dumps(trash))



annotationsDir = "Annotations"
images_dir = "Images"
output_file = "TrashMap.json"

# Remove previous output file
if os.path.exists(output_file):
    print("Removing previous output file")
    os.remove(output_file)

allTrash = []

# Loop through all XML files
for xmlFileName in os.listdir(annotationsDir):
    xmlPath = os.path.join(annotationsDir, xmlFileName)
    tree = ET.parse(xmlPath)
    root = tree.getroot()

    # Loop each individual annotation
    for objectNode in root.findall('object'):
        category = objectNode.find('name').text
        image_path = os.path.join(images_dir, root.find('filename').text)
        coordinates = get_coordinates(image_path)
        trash = {
            'path': image_path, 
            'category': category, 
            'longitude': coordinates['lon'],
            'latitude': coordinates['lat']
        }
        allTrash.append(trash)

writeToJson(output_file, allTrash)

# File for loop
    # filepath path
    # get category
    # get coordinates
# export to JSON file