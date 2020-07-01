import os
import re
import piexif

def absoluteFilePaths(directory):
	for dirpath,_,filenames in os.walk(directory):
		for f in filenames:
			fullPath = os.path.abspath(os.path.join(dirpath, f))
			if re.match(r"^IMG-\d\d\d\d\d\d\d\d-WA\d\d\d\d.jpg", f):
				print(f+" Matched")
				match = re.search("^IMG-(\d\d\d\d)(\d\d)(\d\d)-WA\d\d\d\d.jpg", f)
				year = match.group(1)
				month= match.group(2)
				day = match.group(3)
				exif_dict = piexif.load(fullPath)
				exif_dict['Exif'][36867] = year+':'+month+':'+day+' 00:00:00'
				exif_dict['Exif'][36868] = year+':'+month+':'+day+' 00:00:00'
				exif_dict['0th'][306] = '2015:07:08 12:10:10'
				exif_bytes = piexif.dump(exif_dict)
				piexif.insert(exif_bytes, fullPath)
				print("############################")


absoluteFilePaths("C:\\Users\\cicil\Downloads\\Downloads\\")
