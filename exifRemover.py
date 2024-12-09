from PIL import Image
import os

def getPath():
    folderPath = input("Enter the path of the folder containing the images: ")
    return folderPath

def removeExifData(imagePath):
    with Image.open(imagePath) as img:
        img.save(imagePath, "JPEG", quality=100)

def batchRemoveExif(folderPath):
    for filename in os.listdir(folderPath):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            imagePath = os.path.join(folderPath, filename)
            print(f"Removed EXIF data from: {imagePath}")
            removeExifData(imagePath)

while True:
    folderPath = getPath()

    try:
        if os.path.isdir(folderPath):
            batchRemoveExif(folderPath)
            print("EXIF data was removed.")
        else:
            print("The path you entered is not a valid directory.")
    except Exception as error:
        print(f"An error occurred: {error}. Please try again!")
