import os
import re
import piexif

def absoluteFilePaths(directory):
	for dirpath,_,filenames in os.walk(directory):
		for f in filenames:
			fullPath = os.path.abspath(os.path.join(dirpath, f))
			if re.match(r"^IMG-\d\d\d\d\d\d\d\d-WA\d\d\d\d.*", f) and not re.match(r"^IMG-\d\d\d\d\d\d\d\d-WA\d\d\d\d-ANIMATION.gif", f):
				print(f+" Matched")
				match = re.search("^IMG-(\d\d\d\d)(\d\d)(\d\d)-WA\d\d\d\d.*", f)
				year = match.group(1)
				month= match.group(2)
				day = match.group(3)
				exif_dict = piexif.load(fullPath)
				#Update DateTimeOriginal
				exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = datetime(int(year), int(month), int(day), 4, 0, 0).strftime("%Y:%m:%d %H:%M:%S")
				#Update DateTimeDigitized				
				exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = datetime(int(year), int(month), int(day), 4, 0, 0).strftime("%Y:%m:%d %H:%M:%S")
				#Update DateTime
				exif_dict['0th'][piexif.ImageIFD.DateTime] = datetime(int(year), int(month), int(day), 4, 0, 0).strftime("%Y:%m:%d %H:%M:%S")
				exif_bytes = piexif.dump(exif_dict)
				piexif.insert(exif_bytes, fullPath)
				print("############################")


absoluteFilePaths("__DIRECTORY_WITH_PHOTOS__")
