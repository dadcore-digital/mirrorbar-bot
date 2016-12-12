
<<<<<<< HEAD
def extract_noun_phrases(filename):
	# Pull noun phrases from corpus
	from textblob import TextBlob
	import codecs, os, re

	corp_dir = '%s/corpus/dystopia' % os.getcwd()
	corp_filename = filename
=======
def extract_noun_phrases():
	# Pull noun phrases from corpus
	from textblob import TextBlob
	import codecs, os

	corp_dir = '%s/corpus/dystopia' % os.getcwd()
	corp_filename = 'pkd-scanner.txt'
>>>>>>> 57ff84a26514b30640a6d487422ea685d1692039
	file_in = '%s/raw/%s' % (corp_dir, corp_filename)
	file_out = '%s/parsed/%s' % (corp_dir, corp_filename)

	a = codecs.open(file_in,"r", "utf-8").read()
	blob = TextBlob(a)

	# All Noun Phrases
	np = blob.noun_phrases

	# Sorted list of noun phrases by frequency (most frequent first)
	np = blob.np_counts
	import operator
	np_sorted = sorted(blob.np_counts.items(), key=operator.itemgetter(1))
<<<<<<< HEAD
	
=======

>>>>>>> 57ff84a26514b30640a6d487422ea685d1692039
	# Don't include words with this in them
	pattern = "^('|\")"

	for i, (a, b) in enumerate(np_sorted):
		myfile = open(file_out, "a")
<<<<<<< HEAD
		if len(a.split(" ")) > 2 and not re.search(pattern, a):
			myfile.write(a.encode('utf-8'))
			myfile.write('\n')
=======
		try:
			if len(a.split(" ")) > 1 and not re.search(pattern, a):
				myfile.write(a.encode('utf-8'))
				myfile.write('\n')
		except:
			pass
>>>>>>> 57ff84a26514b30640a6d487422ea685d1692039


#####################################
# Create Dystopian Session Titles   #
#####################################

def create_session_titles():
	from textblob import TextBlob
	import codecs, os
	from random import randint, shuffle

	session_filename	= 'session_titles.txt'
	dys_filename 		= 'dystopian-words.txt'

	session_dir 		= '%s/corpus/sessions' % os.getcwd()
	dys_dir 			= '%s/generated/phrases' % os.getcwd()

	f_session 			= '%s/%s' % (session_dir, session_filename)
	f_dys 				= '%s/%s' % (dys_dir, dys_filename)

	sessions = codecs.open(f_session,"r", "utf-8").read().split('\n')
	dyswords = codecs.open(f_dys,"r", "utf-8").read().split('\n')

	out_filename = 'test-session-titles.txt'
	myfile = open("%s/generated/%s" % (os.getcwd(), out_filename), "a")

	session_copy = sessions[:]
	dyswords_copy = dyswords[:]

	shuffle(session_copy)
	output = ''

	for item in session_copy:
		blob = TextBlob(item)


		if len(blob.noun_phrases) > 1:

			rand_pos = randint(0, len(dyswords_copy)-1)
			d = dyswords_copy[rand_pos] 
			session_title = item.lower().replace(blob.noun_phrases[-1], d)
			session_title = session_title.title()

			output += session_title + '\n'

			# Remove used dystopian word as an option
			del dyswords_copy[rand_pos]

			# Reset dystopian word list if depleted
			if not dyswords_copy:
				dyswords_copy = dyswords[:]

	# Write out file
	myfile.write(output.encode('utf-8'))


<<<<<<< HEAD
create_session_titles()
=======
>>>>>>> 57ff84a26514b30640a6d487422ea685d1692039
