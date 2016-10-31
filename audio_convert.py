# import os
# import glob
# import sys
# from pydub import AudioSegment

# video_dir = '/home/daniel/rnd/Jarmul2/uploads/'  # Path where the videos are located
# file_name = sys.argv[1]
# format = "." + sys.argv[2]
# os.chdir(video_dir)
# new_filename = os.path.splitext(os.path.basename(file_name))[0] + format
# AudioSegment.from_file(file_name).export(new_filename, format=sys.argv[2])


import os
import glob
from pydub import AudioSegment
import sys

video_dir = '/home/daniel/rnd/Jarmul2/uploads'  # Path where the videos are located
file_name = sys.argv[1]
format = "." + sys.argv[2]
bitrate = sys.argv[3]+"k"
os.chdir(video_dir)
if bitrate == '0k':
	mp3_filename = os.path.splitext(os.path.basename("new -"+file_name))[0] + format
	AudioSegment.from_file(file_name).export(mp3_filename, format=sys.argv[2])
else:
	mp3_filename = os.path.splitext(os.path.basename("new -"+file_name))[0] + format
	AudioSegment.from_file(file_name).export(mp3_filename, format=sys.argv[2], bitrate=bitrate)