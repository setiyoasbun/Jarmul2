import os
import sys
from converter import Converter
from os.path import basename

c = Converter()

os.chdir('/home/daniel/rnd/Jarmul2/uploads/')
info = c.probe(sys.argv[1])
#print sys.arg[1]
#print info
conv = c.convert(sys.argv[1], 'output.'+sys.argv[2], {
	'format': sys.argv[2],
	'audio': {
		'codec': sys.argv[3],
		'samplerate': int(sys.argv[4]),
		'channels': int(sys.argv[5])
	},
	'video': {
		'codec': sys.argv[6],
		'width': int(sys.argv[7]),
		'height': int(sys.argv[8]),
		'fps': int(sys.argv[9])
	}})
for timecode in conv:
	print "Converting (%f) ...\r" % timecode
