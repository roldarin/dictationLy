#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
##########################################################################
#                       * * *  PySynth  * * *
#       A very basic audio synthesizer in Python (www.python.org)
#
#          Martin C. Doege, 2009-04-07 (mdoege@compuserve.com)
##########################################################################
# Based on a program by Tyler Eaves (tyler at tylereaves.com) found at
#   http://mail.python.org/pipermail/python-list/2000-August/049968.html
##########################################################################

# 'song' is a Python list (or tuple) in which the song is defined,
#   the format is [['note', value]]

# Notes are 'a' through 'g' of course,
# optionally with '#' or 'b' appended for sharps or flats.
# Finally the octave number (defaults to octave 4 if not given).
# An asterisk at the end makes the note a little louder (useful for the beat).
# 'r' is a rest.

# Note value is a number:
# 1=Whole Note; 2=Half Note; 4=Quarter Note, etc.
# Dotted notes can be written in two ways:
# 1.33 = -2 = dotted half
# 2.66 = -4 = dotted quarter
# 5.33 = -8 = dotted eighth
"""

# Example 1: The C major scale
song1 = [
['c',4],['d',4],['e',4],['f',4],['g',4],['a',4],['b',4],['c5',2],['r',1],
['c3',4],['d3',4],['e3',4],['f3',4],['g3',4],['a3',4],['b3',4],['c4',2],['r',1],
['c1*', 1], ['c2*', 1], ['c3*', 1], ['c4*', 1], ['c5*', 1], ['c6*', 1], ['c7*', 1], ['c8*', 1],
]

# Example 2: Something a little more patriotic
song2 = (
  ('g', -8), ('e', 16),
  ('c*', 4), ('e', 4), ('g', 4),
  ('c5*', 2), ('e5', -8), ('d5', 16),
  ('c5*', 4), ('e', 4), ('f#', 4),
  ('g*', 2), ('g', 8), ('g', 8),
  ('e5*', -4), ('d5', 8), ('c5', 4),
  ('b*', 2), ('a', -8), ('b', 16),
  ('c5*', 4), ('c5', 4), ('g', 4),
  ('e*', 4), ('c', 4),
)

# Example 3: Beginning of Nocturne Op. 9 #2 by F. Chopin
song3 = (
  ('bb', 8),
  ('g5*', 2), ('f5', 8), ('g5', 8), ('f5', -4), ('eb5', 4), ('bb', 8),
  ('g5*', 4), ('c5', 8), ('c6', 4), ('g5', 8), ('bb5', -4), ('ab5', 4), ('g5', 8),
  ('f5*', -4), ('g5', 4), ('d5', 8), ('eb5', -4), ('c5', -4),
  ('bb*', 8), ('d6', 8), ('c6', 8), ('bb5', 16), ('ab5', 16), ('g5', 16), ('ab5', 16), ('c5', 16), ('d5', 16), ('eb5', -4),
)

# Example 4: J.S. Bach: Bourrée (from BWV 996)
song4_rh = (
  ('e', 8), ('f#', 8),
  ('g*', 4), ('f#', 8), ('e', 8), ('d#*', 4), ('e', 8), ('f#', 8),
  ('b3*', 4), ('c#', 8), ('d#', 8), ('e*', 4), ('d', 8), ('c', 8),
  ('b3*', 4), ('a3', 8), ('g3', 8), ('f#3*', 4), ('g3', 8), ('a3', 8),
  ('b3*', 8), ('a3', 8), ('g3', 8), ('f#3', 8), ('e3*', 4), ('e', 8), ('f#', 8),
  ('g*', 4), ('f#', 8), ('e', 8), ('d#*', 4), ('e', 8), ('f#', 8),
  ('b3*', 4), ('c#', 8), ('d#', 8), ('e*', 4), ('d', 8), ('c', 8),
  ('b3*', 4), ('a3', 8), ('g3', 8), ('g3*', 32), ('f#3*', 32), ('g3*', 32), ('f#3*', 32), ('g3*', 32), ('f#3*', 32), ('g3*', 32), ('f#3*', 6.4), ('g3', 8), ('g3*', -2),
)
# version without the trill:
#  ('b3*', 4), ('a3', 8), ('g3', 8), ('f#3*', -4), ('g3', 8), ('g3*', -2),

song4_lh = (
  ('g2', 8), ('f#2', 8),
  ('e2*', 4), ('a2', 4), ('b2', 4), ('a2', 4),
  ('g2*', 4), ('f#2', 4), ('e2', 4), ('f#2', 4),
  ('g2*', 4), ('a2', 4), ('b2', 4), ('a2', 4),
  ('g2*', 4), ('b2', 4), ('e2', 8), ('f#2', 8), ('g2', 8), ('f#2', 8),
  ('e2*', 4), ('a2', 4), ('b2', 4), ('a2', 4),
  ('g2*', 4), ('f#2', 4), ('e2', 4), ('f#2', 4),
  ('g2*', 4), ('c3', 4), ('d3', 4), ('d3', 4),
  ('b2*', -2),
)

##########################################################################
# Compute and print piano key frequency table
##########################################################################
pitchhz = {}
keys_s = ('a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#')
keys_f = ('a', 'bb', 'b', 'c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab')

if __name__ == '__main__':
    print "Piano key frequencies (for equal temperament):"
    print "Key number\tScientific name\tFrequency (Hz)"
for k in range(88):
    freq = 27.5 * 2.**(k/12.)
    oct = (k+9) // 12
    note = '%s%u' % (keys_s[k%12], oct)
    if __name__ == '__main__':
        print "%10u\t%15s\t%14.2f" % (k+1, note.upper(), freq)
    pitchhz[note] = freq
    note = '%s%u' % (keys_f[k%12], oct)
    pitchhz[note] = freq

##########################################################################
#### Main program starts below
##########################################################################
# Some parameters:

# Beats (quarters) per minute
# e.g. bpm = 95

# Octave shift (neg. integer -> lower; pos. integer -> higher)
# e.g. transpose = 0

# Pause between notes as a fraction (0. = legato and e.g., 0.5 = staccato)
# e.g. pause = 0.05

# Volume boost for asterisk notes (1. = no boost)
# e.g. boost = 1.2

# Output file name
#fn = 'pysynth_output.wav'

# Other parameters:

# Influences the decay of harmonics over frequency. Lowering the
# value eliminates even more harmonics at high frequencies.
# Suggested range: between 3. and 5., depending on the frequency response
#  of speakers/headphones used
harm_max = 4.
##########################################################################

import wave, math, struct

def make_wav(song,bpm=120,transpose=0,pause=.05,boost=1.1,repeat=0,fn="out.wav", silent=False):
	f=wave.open(fn,'w')

	f.setnchannels(1)
	f.setsampwidth(2)
	f.setframerate(44100)
	f.setcomptype('NONE','Not Compressed')

	bpmfac = 120./bpm

	def length(l):
	    return 88200./l*bpmfac

	def waves2(hz,l):
	    a=44100./hz
	    b=float(l)/44100.*hz
	    return [a,round(b)]

	def sixteenbit(x):
	    return struct.pack('h', round(32000*x))

	def asin(x):
	    return math.sin(2.*math.pi*x)

	def render2(a,b,vol):
	    b2 = (1.-pause)*b
	    l=waves2(a,b2)
	    ow=""
	    q=int(l[0]*l[1])

	    # harmonics are frequency-dependent:
	    lf = math.log(a)
	    lf_fac = (lf-3.) / harm_max
	    if lf_fac > 1: harm = 0
	    else: harm = 2. * (1-lf_fac)
	    decay = 2. / lf
	    t = (lf-3.) / (8.5-3.)
	    volfac = 1. + .8 * t * math.cos(math.pi/5.3*(lf-3.))

	    for x in range(q):
	         fac=1.
	         if x<100: fac=x/80.
	         if 100<=x<300: fac=1.25-(x-100)/800.
	         if x>q-400: fac=1.-((x-q+400)/400.)
	         s = float(x)/float(q)
	         dfac =  1. - s + s * decay
	         ow=ow+sixteenbit((asin(float(x)/l[0])
	              +harm*asin(float(x)/(l[0]/2.))
	              +.5*harm*asin(float(x)/(l[0]/4.)))/4.*fac*vol*dfac*volfac)
	    fill = max(int(ex_pos - curpos - q), 0)
	    f.writeframesraw((ow)+(sixteenbit(0)*fill))
	    return q + fill

	##########################################################################
	# Write to output file (in WAV format)
	##########################################################################

	if silent == False:
		print "Writing to file", fn
	curpos = 0
	ex_pos = 0.
	for rp in range(repeat+1):
		for nn, x in enumerate(song):
		    if not nn % 4 and silent == False:
		        print "[%u/%u]\t" % (nn+1,len(song))
		    if x[0]!='r':
		        if x[0][-1] == '*':
		            vol = boost
		            note = x[0][:-1]
		        else:
		            vol = 1.
		            note = x[0]
			try:
		            a=pitchhz[note]
			except:
		            a=pitchhz[note + '4']	# default to fourth octave
		        a = a * 2**transpose
		        if x[1] < 0:
		            b=length(-2.*x[1]/3.)
		        else:
		            b=length(x[1])
			ex_pos = ex_pos + b
		        curpos = curpos + render2(a,b,vol)

		    if x[0]=='r':
		        b=length(x[1])
			ex_pos = ex_pos + b
		        f.writeframesraw(sixteenbit(0)*int(b))
			curpos = curpos + int(b)

	f.writeframes('')
	f.close()
	print

def mix_files(a, b, c, chann = 2, phase = -1.):
	f1 = wave.open(a,'r')
	f2 = wave.open(b,'r')
	f3 = wave.open(c,'w')
	f3.setnchannels(chann)
	f3.setsampwidth(2)
	f3.setframerate(44100)
	f3.setcomptype('NONE','Not Compressed')
	frames = min(f1.getnframes(), f2.getnframes())

	print "Mixing files, total length %.2f s..." % (frames / 44100.)
	d1 = f1.readframes(frames)
	d2 = f2.readframes(frames)
	for n in range(frames):
		if not n%(5*44100): print n // 44100, 's'
		if chann < 2:
			d3 = struct.pack('h',
				.5 * (struct.unpack('h', d1[2*n:2*n+2])[0] +
				struct.unpack('h', d2[2*n:2*n+2])[0]))
		else:
			d3 = ( struct.pack('h',
				phase * .3 * struct.unpack('h', d1[2*n:2*n+2])[0] +
				.7 * struct.unpack('h', d2[2*n:2*n+2])[0]) +
				struct.pack('h',
				.7 * struct.unpack('h', d1[2*n:2*n+2])[0] +
				phase * .3 * struct.unpack('h', d2[2*n:2*n+2])[0]) )
		f3.writeframesraw(d3)
	f3.close()

import random, os

def make_song_upper(notes, song_length, notes_length):
# Notes are 'a' through 'g' of course,
# optionally with '#' or 'b' appended for sharps or flats.
# Finally the octave number (defaults to octave 4 if not given).
# An asterisk at the end makes the note a little louder (useful for the beat).
# 'r' is a rest.
    song_upper = []
    for i in range(length):
	new_song_note = []
	new_song_note.append(random.choice(notes))
	new_song_note.append(random.choice(notes_length))
	song_upper.append(new_song_note)
    return song_upper

def make_song_lower(notes, song_length, notes_length):
# Notes are 'a' through 'g' of course,
# optionally with '#' or 'b' appended for sharps or flats.
# Finally the octave number (defaults to octave 4 if not given).
# An asterisk at the end makes the note a little louder (useful for the beat).
# 'r' is a rest.
    song_lower = []
    for i in range(length):
	new_song_note = []
	new_song_note.append(random.choice(notes))
	new_song_note.append(random.choice(notes_length))
	song_lower.append(new_song_note)
    return song_lower

def translate(song_pysynth):
    song_lylipond = ""
    for n in song_pysynth:
	song_lylipond += dictionaryLY[n[0]]+str(n[1])+" "
    return song_lylipond

def correct(song):
#arrelgar los silencios
    corrected_song = ""
    time = 0
    #n = ["Name",0]
    print song
    for n in song.split():
        note_time = 32 / int(n[-1])  
        time += note_time       
        #print "name length time",n[0:-1], n[-1],time      
        if time == 32:
		corrected_song += n+" "
		time = 0
	elif time > 32:
		excess_time = time - 32
		first_time = note_time - excess_time
		second_time = excess_time
		#print "HAY QUE ROMPER ", n[0:-1], "ENTRE ", first_time, " Y ", excess_time 
		#buscamos la nota mas grande que cabe 
		#1 redonda 2 blanca 4 negra 8 corchea 16 semicorchea
                while first_time != 0:
                    value = 32
		    div = first_time
		    while div !=1: 
			div /= 2
			value /= 2
                        #print "div, value", div, value
	                #raw_input()
                    first_time = first_time - 32 / value
                    #tiempo que queda a rellenar
		    if (first_time % 2) == 0 and (first_time != 0):
			#lo solucionamos con un puntillo	
                        corrected_song += n[0:-1]+str(value)+".~ "
			first_time = 0
                        #print "a PRIMER VALOR ",str(value), ".~ EXCESO",  first_time
                    else: 
                        corrected_song += n[0:-1]+str(value)+"~ "
                        #print "b PRIMER VALOR ",str(value), "~ EXCESO",  first_time
		while excess_time != 0:
                    value = 32
		    div = excess_time
		    while div != 1: 
			div /= 2
			value /= 2
                        #print "div, value", div, value, 32 / value
		    excess_time = excess_time - 32 / value
                    if (excess_time % 2) == 0 and (excess_time != 0):
			#lo solucionamos con un puntillo	
                        corrected_song += n[0:-1]+str(value)+". "
			excess_time = 0
                        #print "a SEGUNDO VALOR ",str(value), ". EXCESO", excess_time
                    elif (excess_time == 0): 
                        corrected_song += n[0:-1]+str(value)+" "
		    	excess_time = 0
                        #print "b SEGUNDO VALOR ",str(value), " EXCESO", excess_time	
                    else:  
                        corrected_song += n[0:-1]+str(value)+" "
		    	excess_time = excess_time - 32 / value
                        #print "c SEGUNDO VALOR ",str(value), " EXCESO", excess_time
		time = second_time
        else:
		corrected_song += n+" "
       

    return corrected_song

def fill_song(upper, lower):
    #make upper and lower from the same time length, fill with silences
    length_upper = 0
    length_lower = 0
    for n in upper:
	length_upper += 32 / n[1]
    for n in lower:
	length_lower += 32 / n[1] 
    if length_upper > length_lower:
	#fill song lower with silences
        fill_time = length_upper - length_lower
	while fill_time != 0:
	   if fill_time >= 32:
               lower.append(['r', 1])
               fill_time -= 32
	   elif fill_time >= 16:
               lower.append(['r', 2])
               fill_time -= 16
	   elif fill_time >= 8:
               lower.append(['r', 4])
               fill_time -= 8
	   elif fill_time >= 4:
               lower.append(['r', 8])
               fill_time -= 4
	   elif fill_time >= 2:
               lower.append(['r', 16])
               fill_time -= 2
	   elif fill_time >= 1:
               lower.append(['r', 32])
               fill_time = 0
    else: 
       	#fill song uppe with silences
        fill_time = length_lower - length_upper
	while fill_time != 0:
	   print "fill_time ", fill_time
	   if fill_time >= 32:
               upper.append(['r', 1])
               fill_time -= 32
               print "red "
	   elif fill_time >= 16:
               upper.append(['r', 2])
               fill_time -= 16
	   elif fill_time >= 8:
               upper.append(['r', 4])
               fill_time -= 8
	   elif fill_time >= 4:
               upper.append(['r', 8])
               fill_time -= 4
	   elif fill_time >= 2:
               upper.append(['r', 16])
               fill_time -= 2
	   elif fill_time >= 1:
               upper.append(['r', 32])
               fill_time = 0
    return length_lower, length_upper

if __name__ == '__main__':

	dictionaryLY = {
    		"r" : "r",
		
		"a0" : "a,,,",
    		"ab0" : "aes,,,",
    		"b0" : "b,,,",

   		"c1" : "c,,",
   		"c#1" : "cis,,",
   		"db1" : "des,,",
    		"d1" : "c,,",
    		"d#1" : "dis,,",
    		"eb1" : "ees,,",
    		"e1" : "e,,",
   		"f1" : "f,,",
    		"f#1" : "fis,,",
    		"gb1" : "ges,,",
    		"g1" : "g,,",
    		"g#1" : "gis,,",
    		"ab1" : "aes,,",
    		"a1" : "a,,",
    		"a#1" : "ais,,",
    		"bb1" : "bes,,",
    		"b1" : "b,,",

   		"c2" : "c,",
   		"c#2" : "cis,",
   		"db2" : "des,",
    		"d2" : "c,",
    		"d#2" : "dis,",
    		"eb2" : "ees,",
    		"e2" : "e,",
   		"f2" : "f,",
    		"f#2" : "fis,",
    		"gb2" : "ges,",
    		"g2" : "g,",
    		"g#2" : "gis,",
    		"ab2" : "aes,",
    		"a2" : "a,",
    		"a#2" : "ais,",
    		"bb2" : "bes,",
    		"b2" : "b,",

   		"c3" : "c",
   		"c#3" : "cis",
   		"db3" : "des",
    		"d3" : "c",
    		"d#3" : "dis",
    		"eb3" : "ees",
    		"e3" : "e",
   		"f3" : "f",
    		"f#3" : "fis",
    		"gb3" : "ge'",
    		"g3" : "g",
    		"g#3" : "gis",
    		"ab3" : "aes",
    		"a3" : "a",
    		"a#3" : "ais",
    		"bb3" : "bes",
    		"b3" : "b",

   		"c4" : "c'",
   		"c#4" : "cis'",
   		"db4" : "des'",
    		"d4" : "c'",
    		"d#4" : "dis'",
    		"eb4" : "ees'",
    		"e4" : "e'",
   		"f4" : "f'",
    		"f#4" : "fis'",
    		"gb4" : "ges'",
    		"g4" : "g'",
    		"g#4" : "gis'",
    		"ab4" : "aes'",
    		"a4" : "a'",
    		"a#4" : "ais'",
    		"bb4" : "bes'",
    		"b4" : "b'",

   		"c5" : "c''",
   		"c#5" : "cis''",
   		"db5" : "des''",
    		"d5" : "c''",
    		"d#5" : "dis''",
    		"eb5" : "ees''",
    		"e5" : "e''",
   		"f5" : "f''",
    		"f#5" : "fis''",
    		"gb5" : "ges''",
    		"g5" : "g''",
    		"g#5" : "gis''",
    		"ab5" : "aes''",
    		"a5" : "a''",
    		"a#5" : "ais''",
    		"bb5" : "bes''",
    		"b5" : "b''",

   		"c6" : "c'''",
   		"c#6" : "cis'''",
   		"db6" : "des'''",
    		"d6" : "c'''",
    		"d#6" : "dis'''",
    		"eb6" : "ees'''",
    		"e6" : "e'''",
   		"f6" : "f'''",
    		"f#6" : "fis'''",
    		"gb6" : "ges'''",
    		"g6" : "g'''",
    		"g#6" : "gis'''",
    		"ab6" : "aes'''",
    		"a6" : "a'''",
    		"a#6" : "ais'''",
    		"bb6" : "bes'''",
    		"b6" : "b'''",

   		"c7" : "c''''",
   		"c#7" : "cis''''",
   		"db7" : "des''''",
    		"d7" : "c''''",
    		"d#7" : "dis''''",
    		"eb7" : "ees''''",
    		"e7" : "e''''",
   		"f7" : "f''''",
    		"f#7" : "fis''''",
    		"gb7" : "ges''''",
    		"g7" : "g''''",
    		"g#7" : "gis''''",
    		"ab7" : "aes''''",
    		"a7" : "a''''",
    		"a#7" : "ais''''",
    		"bb7" : "bes''''",
    		"b7" : "b''''",

   		"c8" : "c'''''",
	


	}
	print
	print "Creating Dictation..."
	print

	fout = open("dictation.ly", 'w')
	header = """\\version "2.16.2"

\header {
	composer = "Random"
	crossRefNumber = "1"
	footnotes = ""
	title = "Dictado"
}"""
	fout.write(header)
	translateLYlength = {
    		1 : "4",
    		2 : "2",
    		4 : "1",
    		8 : "1/2",
   		16 : "1/4",
   		32 : "1/8",
	}	
	length = 4
        upper_notes = ["c3","c#3","db3","d#3","e3","g3","c4","c5","c6","c7","c8"]
	notes_length = [1, 2, 4, 8]
	song_upper = make_song_upper(upper_notes, length, notes_length)
	song_upper = [['c7', 1], ['c8', 8], ['db3', 2], ['c6', 2]]
	lower_notes = ["r"]
	notes_length = [1]
	song_lower = make_song_upper(lower_notes, length, notes_length)
        print song_upper
        print song_lower
	#hay que igularlas primero
        print str(fill_song(song_upper, song_lower))
	#cambiamos a formato lilypond
	song_upper_translated = translate(song_upper)	
	song_lower_translated = translate(song_lower)
	#corregimos las partituras
        upper = correct(song_upper_translated)
	lower = correct(song_lower_translated)


	fout.write("\n\nupper = {\n")
	fout.write("  \\clef treble\n")
	fout.write("  \\key c \major\n")
	fout.write("  \\time 4/4\n  ")
	fout.write(upper)
	fout.write("\n}\n\n")

	fout.write("\n\nlower = {\n")
	fout.write("  \\clef bass\n")
	fout.write("  \\key c \major\n")
	fout.write("  \\time 4/4\n  ")
	fout.write(lower)
	fout.write("\n}\n\n")

	fout.write("\\score {\n")
	fout.write("  <<\n")
	fout.write("    \\new PianoStaff <<\n")
	fout.write("      \\new Staff = \"upper\" \\upper\n")
	fout.write("      \\new Staff = \"lower\" \\lower\n")
	fout.write("    >>\n")
 	fout.write(" >>\n")
	fout.write("  \\layout {\n")
	fout.write("    \\context { \Staff \RemoveEmptyStaves }\n")
	fout.write("  }\n")
	fout.write(" \\midi { }\n")
	fout.write("}\n\n")
	fout.close()

	os.system("lilypond dictation.ly")

	#print dictation in pdf
	#os.system("abcm2ps dictation.abc")
	#os.system("ps2pdf Out.ps")

	#play dictation
	#os.system("abc2midi dictation.abc")
	#os.system("timidity dictation1.mid")

	song2 = [['g', -8], ['e', 16]]
	make_wav(song2, fn = "dictation.wav")



"""
	# SONG 1
	make_wav(song1, fn = "pysynth_scale.wav")

	# SONG 2
	make_wav(song2, bpm = 95, boost = 1.2, fn = "pysynth_anthem.wav")

	# SONG 3
	make_wav(song3, bpm = 132/2, pause = 0., boost = 1.1, fn = "pysynth_chopin.wav")

	# SONG 4
	#   right hand part
	make_wav(song4_rh, bpm = 130, transpose = 1, pause = .1, boost = 1.15, repeat = 1, fn = "pysynth_bach_rh.wav")
	#   left hand part
	make_wav(song4_lh, bpm = 130, transpose = 1, pause = .1, boost = 1.15, repeat = 1, fn = "pysynth_bach_lh.wav")
	#   mix both files together
	mix_files("pysynth_bach_rh.wav", "pysynth_bach_lh.wav", "pysynth_bach.wav")

"""


"""ANTIGUO CODIGO
    	for n in dictation:
		note_time = 32 / n[1]  
		time += note_time       
		print "n time", n ,time       
		#check if bar is full, if excess we need correction
		if time == 32:
			fout.write(dictionaryABC[n[0]]+translateABClength[n[1]])
			fout.write("|")
			time = 0
		elif time > 32:
			excess_time = time - 32
			first_time = note_time - excess_time
			second_time = excess_time
			print "HAY QUE ROMPER ", dictionaryABC[n[0]], "ENTRE ", first_time, " Y ", excess_time 
			if first_time > excess_time:
				new_time_value = excess_time
			else: 
				new_time_value = first_time
			fill_time = 0
			while (fill_time < first_time):
				print "primera ", dictionaryABC[n[0]], 32 / new_time_value
				fout.write(dictionaryABC[n[0]]+translateABClength[32 / new_time_value])
				fout.write("-")
				fill_time += new_time_value
			print "segunda ", dictionaryABC[n[0]], 32 / new_time_value
			fout.write("|")
			fout.write(dictionaryABC[n[0]]+translateABClength[32 / new_time_value])
			time = new_time_value
        	else:
			fout.write(dictionaryABC[n[0]]+translateABClength[n[1]])

	if time == 32:
		fout.write("||\n")
	else:
		print "time ", time
		fill_time = 32 / (32 - time)
		fout.write("z"+translateABClength[fill_time]+"||\n")
		
	#fill with silence


VIEJA
		while remain !=0: 
		    first_part_time = 32 / first_time
		    remain = 32 % first_time
		    print "PRIMERA VALOR ",first_part_time, " EXCESO", remain
		    corrected_song += n[0:-1]+str(first_part_time)+"~ "
		    first_time -= 32 / first_part_time
		remain=1

"""
