import os
import sys
from PIL import Image
from os.path import basename
from Tkinter import *
from ttk import *
import tkFileDialog
import tkMessageBox
import time
import re

root = Tk()
fields = ('Pilih gambar', 'Lebar', 'Tinggi')
tek = Text(root)
execute_time = 0
entries = {}

def browse(entries):
	entries['Pilih gambar'].delete(0,END)
	entries['Pilih gambar'].insert(0,tkFileDialog.askopenfilename())

def convertBitmap(entries):
	width = entries['Lebar'].get()
	height = entries['Tinggi'].get()
	if width == '' and height == '':
		start_time = time.clock()
		#tek.delete('1.0',END)	
		image_dir = entries['Pilih gambar'].get()
		image_size_before = os.path.getsize(image_dir)
		#print image_size_before
		imgname = os.path.splitext(image_dir)[0]
		#print image_dir
		img = Image.open(image_dir)
		imgformat = img.format
		img.save(imgname+'-new.bmp','bmp',quality=50,optimize=True)
		global execute_time 
		execute_time = time.clock() - start_time
		tkMessageBox.showinfo("Convert to Bitmap", imgname+'-new.bmp'+' sudah tersimpan')
		image_size_after = os.path.getsize(imgname+'-new.bmp')
		#print image_size_after
		Compressed = (float(image_size_before) - float(image_size_after))/float(image_size_before)
		Compressed *= 100
		CompleteTime = str("\n--- Convert to Bitmap : ") + str(execute_time) + str(" seconds ---\n")
		Compress = str("--- Compressed : ") + str(Compressed) + str("% ---\n")
		print("--- Convert to Bitmap : %s seconds ---" % execute_time)
		print("--- Compressed : %s ---" %Compressed )
		tek.insert(END, CompleteTime)
		tek.insert(END, Compress)
	else :
		tkMessageBox.showinfo("Convert to Bitmap", "Hanya Resize yang menggunakan Lebar dan Tinggi")

def convertJPEG(entries):
	width = entries['Lebar'].get()
	height = entries['Tinggi'].get()
	if width == '' and height == '':
		start_time = time.clock()
		#tek.delete('1.0',END)
		image_dir = entries['Pilih gambar'].get()
		image_size_before = os.path.getsize(image_dir)
		imgname = os.path.splitext(image_dir)[0]
		img = Image.open(image_dir)
		imgformat = img.format
		img.save(imgname+'-new.jpeg','jpeg',quality=50,optimize=True)
		global execute_time
		execute_time = time.clock() - start_time
		tkMessageBox.showinfo("Convert to JPEG", imgname+'-new.jpeg'+' sudah tersimpan')
		image_size_after = os.path.getsize(imgname+'-new.jpeg')
		Compressed = (float(image_size_before) - float(image_size_after))/float(image_size_before)
		Compressed *= 100
		CompleteTime = str("\n--- Convert to JPEG : ") + str(execute_time) + str(" seconds ---\n")
		Compress = str("--- Compressed : ") + str(Compressed) + str("% ---\n")
		print("--- Convert to JPEG : %s seconds ---" % execute_time)
		print("--- Compressed : %s ---" %Compressed )
		tek.insert(END, CompleteTime)
		tek.insert(END, Compress)
	else :
		tkMessageBox.showinfo("Convert to Bitmap", "Hanya Resize yang menggunakan Lebar dan Tinggi")		

def convertPNG(entries):
	width = entries['Lebar'].get()
	height = entries['Tinggi'].get()
	if width == '' and height == '':
		start_time = time.clock()
		#tek.delete('1.0',END)
		image_dir = entries['Pilih gambar'].get()
		image_size_before = os.path.getsize(image_dir)
		imgname = os.path.splitext(image_dir)[0]
		img = Image.open(image_dir)
		imgformat = img.format
		img.save(imgname+'-new.png','png',dpi=[10,10],quality=20,optimize=True)
		global execute_time
		execute_time = time.clock() - start_time
		tkMessageBox.showinfo("Convert to PNG", imgname+'-new.PNG'+' sudah tersimpan')
		image_size_after = os.path.getsize(imgname+'-new.PNG')
		Compressed = (float(image_size_before) - float(image_size_after))/float(image_size_before)
		Compressed *= 100		
		CompleteTime = str("\n--- Convert to PNG : ") + str(execute_time) + str(" seconds ---\n")
		Compress = str("--- Compressed : ") + str(Compressed) + str("% ---\n")		
		print("--- Convert to PNG : %s seconds ---" % execute_time)
		print("--- Compressed : %s ---" %Compressed )		
		tek.insert(END, CompleteTime)
		tek.insert(END, Compress)
	else :
		tkMessageBox.showinfo("Convert to Bitmap", "Hanya Resize yang menggunakan Lebar dan Tinggi")
		
def convertTIFF(entries):
	width = entries['Lebar'].get()
	height = entries['Tinggi'].get()
	if width == '' and height == '':
		start_time = time.clock()
		#tek.delete('1.0',END)
		image_dir = entries['Pilih gambar'].get()
		image_size_before = os.path.getsize(image_dir)
		imgname = os.path.splitext(image_dir)[0]
		img = Image.open(image_dir)
		imgformat = img.format
		img.save(imgname+'-new.tiff','tiff')
		global execute_time
		execute_time = time.clock() - start_time
		tkMessageBox.showinfo("Convert to TIFF", imgname+'-new.tiff'+' sudah tersimpan')
		image_size_after = os.path.getsize(imgname+'-new.tiff')
		Compressed = (float(image_size_before) - float(image_size_after))/float(image_size_before)
		Compressed *= 100		
		CompleteTime = str("\n--- Convert to TIFF : ") + str(execute_time) + str(" seconds ---\n")
		Compress = str("--- Compressed : ") + str(Compressed) + str("% ---\n")		
		print("--- Convert to TIFF : %s seconds ---" % execute_time)
		print("--- Compressed : %s ---" %Compressed )		
		tek.insert(END, CompleteTime)
		tek.insert(END, Compress)		
	else :
		tkMessageBox.showinfo("Convert to Bitmap", "Hanya Resize yang menggunakan Lebar dan Tinggi")		

def convertResize(entries):
	width = entries['Lebar'].get()
	height = entries['Tinggi'].get()
	if width == '' and height == '':
		tkMessageBox.showinfo("Resize", "Isikan terlebih dahulu Lebar dan Tinggi")
	else :
		start_time = time.clock()
		#tek.delete('1.0',END)
		image_dir = entries['Pilih gambar'].get()
		image_size_before = os.path.getsize(image_dir)		
		imgname = os.path.splitext(image_dir)[0]
		img = Image.open(image_dir)
		imgformat = img.format
		x = entries['Lebar'].get()
		y = entries['Tinggi'].get()
		x = int(x)
		y = int(y)
		nilaix = str(x)
		nilaiy = str(y)
		new_img = img.resize((x,y))
		new_img.save(imgname+'-'+nilaix+'x'+nilaiy+'.'+imgformat,imgformat)
		global execute_time
		execute_time = time.clock() - start_time
		tkMessageBox.showinfo("Resize", imgname+'-'+nilaix+'x'+nilaiy+'.'+imgformat+' sudah tersimpan')
		image_size_after = os.path.getsize(imgname+'-'+nilaix+'x'+nilaiy+'.'+imgformat)
		Compressed = (float(image_size_before) - float(image_size_after))/float(image_size_before)
		Compressed *= 100		
		CompleteTime = str("\n--- Resize : ") + str(execute_time) + str(" seconds ---\n")
		Compress = str("--- Compressed : ") + str(Compressed) + str("% ---\n")			
		print("--- Resize : %s seconds ---" % execute_time)
		print("--- Compressed : %s ---" %Compressed )		
		tek.insert(END, CompleteTime)
		tek.insert(END, Compress)			
	
def makeform(root, fields):
	#pathr = StringVar()
	#path = Label(master, text="File Path:")
	#self.pathe = Entry(master, textvariable=pathr, width=50)
	#pathb = Button(master, text="Browse", command=lambda:pathr.set(tkFileDialog.askopenfilename()))	
	for field in fields:
		row = Frame(root)
		lab = Label(row, width=22, text=field+": ", anchor='w')
		ent = Entry(row)
		ent.insert(0,"")
		row.pack(side=TOP, fill=X, padx=5, pady=5)
		lab.pack(side=LEFT)
		ent.pack(side=RIGHT, expand=YES, fill=X)
		entries[field] = ent
	return entries
	
def updated():
	#tek = Text(root)
	tek.pack()
	#tek.insert(END, output)
	#tek.update_idletasks()		

if __name__ == '__main__':
	from PIL import Image
	ents = makeform(root, fields)
	updated()
	#global entries
	root.bind('<Return>', (lambda event, e=ents: fetch(e)))
	b1 = Button(root, text='Browse', command=(lambda e=ents: browse(e)))
	b1.pack(side=LEFT, padx=5, pady=5)	
	b1 = Button(root, text='Convert to Bitmap', command=(lambda e=ents: convertBitmap(e)))
	b1.pack(side=LEFT, padx=5, pady=5)
	b2 = Button(root, text='Convert to JPEG', command=(lambda e=ents: convertJPEG(e)))
	b2.pack(side=LEFT, padx=5, pady=5)
	b3 = Button(root, text='Convert to PNG', command=(lambda e=ents: convertPNG(e)))
	b3.pack(side=LEFT, padx=5, pady=5)
	b4 = Button(root, text='Convert to TIFF', command=(lambda e=ents: convertTIFF(e)))
	b4.pack(side=LEFT, padx=5, pady=5)
	b5 = Button(root, text='Resize', command=(lambda e=ents: convertResize(e)))
	b5.pack(side=LEFT, padx=5, pady=5)	
	b6 = Button(root, text='Quit', command=root.quit)
	b6.pack(side=LEFT, padx=5, pady=5)
	root.mainloop()
