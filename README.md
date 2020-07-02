# Scripts
Just Scripts that i find useful

# Change_Photo_Taken_Time.py
Whatsapp photos issue where all the photos got uploaded to a single day in Google photos since the Whatsapp photos were missing the required metadata to be added to the required dates.
This script makes use of piexif library to update the DateTimeOriginal, DateTimeDigitized, DateTime  of all the whatsapp images in a directory __DIRECTORY_WITH_PHOTOS__. It makes use of the filename to update the above timestamps
Eg:  IMG-20160117-WA0001.jpg

20160117 = 2016 (Year) - 01 (Month) - 17 (Day)
The Timestamp is hardcoded to 04:00 (GMT +00:00) to allow the photos to be added to the correct day.


This script was specificatlly done to fix an issue i was facing where whatsapp images uploaded to google photos would get shown current date when the photo was uploaded
