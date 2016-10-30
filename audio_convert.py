from Tkinter import *
from ttk import *
import tkMessageBox
import os
import tkFileDialog
from pydub import AudioSegment
import time
import re

root = Tk()
fields = ('Pilih File Audio')
tek = Text(root)
execute_time = 0
entries = {}


def browse(entries):
	entries['Pilih File Audio'].delete(0,END)
	entries['Pilih File Audio'].insert(0,tkFileDialog.askopenfilename())

def convertMP3(entries):
	start_time = time.clock()
	#tek.delete('1.0',END)
	audio_dir = entries['Pilih File Audio'].get()
	audio_size_before = os.path.getsize(audio_dir)
	audioname = os.path.splitext(audio_dir)[0]
	AudioSegment.from_file(audio_dir).export(audioname+'.mp3', format='mp3')
	#img = Image.open(audio_dir)
	#imgformat = img.format
	#img.save(imgname+'-new.png','png')
	global execute_time
	execute_time = time.clock() - start_time
	tkMessageBox.showinfo("Convert to mp3", audioname+'.mp3'+' sudah tersimpan')
	audio_size_after = os.path.getsize(audioname+'.mp3')
	Compressed = (float(audio_size_before) - float(audio_size_after))/float(audio_size_before)
	Compressed *= 100
	CompleteTime = str("\n--- Convert to mp3 : ") + str(execute_time) + str(" seconds ---\n")
	Compress = str("--- Compressed : ") + str(Compressed) + str("% ---\n")
	print("--- Convert to mp3 : %s seconds ---" % execute_time)
	print("--- Compressed : %s ---" %Compressed )
	tek.insert(END, CompleteTime)
	tek.insert(END, Compress)

def convertMP4(entries):
	start_time = time.clock()
	#tek.delete('1.0',END)
	audio_dir = entries['Pilih File Audio'].get()
	audio_size_before = os.path.getsize(audio_dir)
	audioname = os.path.splitext(audio_dir)[0]
	AudioSegment.from_file(audio_dir).export(audioname+'.mp4', format='mp4')
	#img = Image.open(audio_dir)
	#imgformat = img.format
	#img.save(imgname+'-new.png','png')
	global execute_time
	execute_time = time.clock() - start_time
	tkMessageBox.showinfo("Convert to mp4", audioname+'.mp4'+' sudah tersimpan')
	audio_size_after = os.path.getsize(audioname+'.mp4')
	Compressed = (float(audio_size_before) - float(audio_size_after))/float(audio_size_before)
	Compressed *= 100
	CompleteTime = str("\n--- Convert to mp4 : ") + str(execute_time) + str(" seconds ---\n")
	Compress = str("--- Compressed : ") + str(Compressed) + str("% ---\n")
	print("--- Convert to mp4 : %s seconds ---" % execute_time)
	print("--- Compressed : %s ---" %Compressed )
	tek.insert(END, CompleteTime)
	tek.insert(END, Compress)

def convertAC3(entries):
	start_time = time.clock()
	#tek.delete('1.0',END)
	audio_dir = entries['Pilih File Audio'].get()
	audio_size_before = os.path.getsize(audio_dir)
	audioname = os.path.splitext(audio_dir)[0]
	AudioSegment.from_file(audio_dir).export(audioname+'.ac3', format='ac3')
	#img = Image.open(audio_dir)
	#imgformat = img.format
	#img.save(imgname+'-new.png','png')
	global execute_time
	execute_time = time.clock() - start_time
	tkMessageBox.showinfo("Convert to ac3", audioname+'.ac3'+' sudah tersimpan')
	audio_size_after = os.path.getsize(audioname+'.ac3')
	Compressed = (float(audio_size_before) - float(audio_size_after))/float(audio_size_before)
	Compressed *= 100
	CompleteTime = str("\n--- Convert to ac3 : ") + str(execute_time) + str(" seconds ---\n")
	Compress = str("--- Compressed : ") + str(Compressed) + str("% ---\n")
	print("--- Convert to ac3 : %s seconds ---" % execute_time)
	print("--- Compressed : %s ---" %Compressed )
	tek.insert(END, CompleteTime)
	tek.insert(END, Compress)

def updated():
	#tek = Text(root)
	tek.pack()
	#tek.insert(END, output)
	#tek.update_idletasks()

def makeform(root, fields):
	#for field in fields:
	row = Frame(root)
	lab = Label(row, width=22, text=fields+": ", anchor='w')
	ent = Entry(row)
	ent.insert(0,"")
	row.pack(side=TOP, fill=X, padx=5, pady=5)
	lab.pack(side=LEFT)
	ent.pack(side=RIGHT, expand=YES, fill=X)
	entries[fields] = ent
	return entries

if __name__ == '__main__':
	ents = makeform(root, fields)
	updated()
	root.bind('<Return>', (lambda event, e=ents: fetch(e)))
	b0 = Button(root, text='Browse', command=(lambda e=ents: browse(e)))
	b0.pack(side=LEFT, padx=5, pady=5)
	b1 = Button(root, text='Convert to mp3', command=(lambda e=ents: convertMP3(e)))
	b1.pack(side=LEFT, padx=5, pady=5)
	b2 = Button(root, text='Convert to mp4', command=(lambda e=ents: convertMP4(e)))
	b2.pack(side=LEFT, padx=5, pady=5)
	b3 = Button(root, text='Convert to ac3', command=(lambda e=ents: convertAC3(e)))
	b3.pack(side=LEFT, padx=5, pady=5)	
	b4 = Button(root, text='Quit', command=root.quit)
	b4.pack(side=LEFT, padx=5, pady=5)
	root.mainloop()
