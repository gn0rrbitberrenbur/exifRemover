# 📷 Remove EXIF-files from your images

this little script allows you to batch remove EXIF-data from your images. 

# how does it work?

enter a relative path to the folder containing your images. like...

```
/home/user/pictures
```

if the path is valid the script will load every file with the filetype '.jpg' or '.jpeg' in the folder and save it again.
in this process the images EXIF-date will be removed from the image.

# ⚠️ note

I do not grant that this actually deletes every bit of information inthe images. I saw it worked for information like ISO, focal length, shutter speed. so if you are really concerned about accidentally leaking your location maybe check manually or use another tool.
