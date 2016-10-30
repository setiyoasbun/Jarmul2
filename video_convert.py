from Tkinter import *
from converter import Converter
import tkFileDialog
import time
import re

root = Tk()
tek = Text(root)
execute_time = 0


class Window:	

	def __init__ (self, master):
		#updated()
		pathr = StringVar()
		path = Label(master, text="File Path:")
		self.pathe = Entry(master, textvariable=pathr, width=50)
		pathb = Button(master, text="Browse", command=lambda:pathr.set(tkFileDialog.askopenfilename()))

		formats = Label(master, text="Format Output:")
		self.formate = Entry(master) 

		audiocodec = Label(master, text="Audio Codec:")
		self.audiocodece = Entry(master)

		audiosamplerate = Label(master, text="Audio Sample Rate:")
		self.audiosampleratee = Entry(master)

		audiochannels = Label(master, text="Audio Channel:")
		self.audiochannelse = Entry(master)

		videocodec = Label(master, text="Video Codec:")
		self.videocodece = Entry(master)

		videowidth = Label(master, text="Video Width:")
		self.videowidthe = Entry(master)

		videoheight = Label(master, text="Video Height:")
		self.videoheighte = Entry(master)

		videofps = Label(master, text="Video FPS:")
		self.videofpse = Entry(master)
		
		finalbutton = Button(master, text="Convert", command=self.convert)

		path.grid(sticky=E)
		self.pathe.grid(row = 0, column = 1)
		pathb.grid(row = 0, column = 2)
		formats.grid(sticky=E)
		self.formate.grid(row = 1, column = 1, sticky = W)
		audiocodec.grid(sticky=E)
		self.audiocodece.grid(row = 2, column=1, sticky = W)
		audiosamplerate.grid(sticky=E)
		self.audiosampleratee.grid(row = 3, column=1, sticky=W)
		audiochannels.grid(sticky=E)
		self.audiochannelse.grid(row = 4, column=1, sticky=W)
		videocodec.grid(sticky=E)
		self.videocodece.grid(row=5, column=1, sticky=W)
		videowidth.grid(sticky=E)
		self.videowidthe.grid(row=6, column=1, sticky=W)
		videoheight.grid(sticky=E)
		self.videoheighte.grid(row=7, column=1, sticky=W)
		videofps.grid(sticky=E)
		self.videofpse.grid(row=8, column=1, sticky=W)
		finalbutton.grid(row=9, column=1)

	def convert(self):
		start_time = time.clock()
		c = Converter()

		info = c.probe(self.pathe.get())

		conv = c.convert(self.pathe.get(), 'output.'+self.formate.get(), {
			'format': self.formate.get(),
			'audio': {
				'codec': self.audiocodece.get(),
				'samplerate': int(self.audiosampleratee.get()),
				'channels': int(self.audiochannelse.get())
			},
			'video': {
				'codec': self.videocodece.get(),
				'width': int(self.videowidthe.get()),
				'height': int(self.videoheighte.get()),
				'fps': int(self.videofpse.get())
			}})

		for timecode in conv:
			print "Converting (%f) ...\r" % timecode
		toplevel = Toplevel()
		label1 = Label(toplevel, text="Finished", height=0, width=100)
		label1.pack()
		execute_time = time.clock() - start_time
		CompleteTime = str("\n--- Convert : ") + str(execute_time) + str(" seconds ---")
		print("--- Convert to PNG : %s seconds ---" % execute_time)
		tkMessageBox.showinfo("Convert", CompleteTime)
		tek.insert(END, CompleteTime)

window=Window(root)
root.mainloop()  
