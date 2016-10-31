import os
import glob
from pydub import AudioSegment

video_dir = '/home/daniel/kuliah/jarmul/'  # Path where the videos are located
extension = ('*.au')
print ("1. ogg  2. aiff  3. ac3")
type = input("Jenis Kompresi (1/2/3): ")
os.chdir(video_dir)
for video in glob.glob(extension):
	if type == 1:
		ogg_filename = os.path.splitext(os.path.basename(video))[0] + '.ogg'
		AudioSegment.from_file(video).export(ogg_filename, format='ogg')
	elif type == 2:
		aiff_filename = os.path.splitext(os.path.basename(video))[0] + '.aiff'
		AudioSegment.from_file(video).export(aiff_filename, format='aiff')
	else:
		ac3_filename = os.path.splitext(os.path.basename(video))[0] + '.ac3'
		AudioSegment.from_file(video).export(ac3_filename, format='ac3')
