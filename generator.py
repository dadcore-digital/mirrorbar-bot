from textblob import TextBlob

import codecs
a = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/pkd-shortstories.txt","r", "utf-8").read()
blob = TextBlob(a)

# All Noun Phrases
np = blob.noun_phrases

# Sorted list of noun phrases by frequency (most frequent first)
np = blob.np_counts
import operator
np_sorted = sorted(blob.np_counts.items(), key=operator.itemgetter(1))

for i, (a, b) in enumerate(np_sorted):
	myfile = open("/Users/ianfitzpatrick/code/dystopiabar/pkd-shortstories-np.txt", "a")
	try:
		myfile.write(a.encode('utf-8'))
		myfile.write('\n')
	except:
		pass


# Create Dystopian Session Titles
from textblob import TextBlob
import codecs
import random
sessions = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/session_titles.txt","r", "utf-8").read().split('\n')
pkd = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/dystopian-words.txt","r", "utf-8").read().split('\n')

a = sessions[0]
b = pkd[0]

hr = '\n\n-------------------------------------------------------------------------'
myfile = open("/Users/ianfitzpatrick/code/dystopiabar/dystopian-session-titles.txt", "a")
myfile.write(hr.encode('utf-8'))

blob = TextBlob(a)
for item in sessions:
	blob = TextBlob(item)
	if blob.noun_phrases:
		title = item.lower().replace(blob.noun_phrases[-1], random.choice(pkd)).title()
		print title
		myfile.write('\n'.encode('utf-8'))
		myfile.write(title.encode('utf-8'))

## Srape Minnebar Session Descriptions ##
import time
import requests
from bs4 import BeautifulSoup
domain = 'http://wiki.minnestar.org'
sessions = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/links-to-all-sessions.txt","r").read().split('\n')


# Download Session Pages
for counter, link in enumerate(sessions):
	print "Writing %s.html for URL %s" % (counter, link)
	r = requests.get(domain + link)
	t = r.text
	myfile = open("/Users/ianfitzpatrick/code/dystopiabar/pages/%s.html" %  counter, "w")
	myfile.write(t.encode('utf-8'))
	print "Sleeping..."
	time.sleep(.5)

# Parse Pages for Session Description and Save to File
for i in range(340):
	print "%s.html" % i
	f = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/pages/%s.html" % i, "r", "utf-8").read()		
	soup = BeautifulSoup(f)
	desc = ""
	try:
		desc += soup.noscript.next_sibling.next_sibling.next.next.next.next.next.next.next.next.text
		try:
			desc += soup.noscript.next_sibling.next_sibling.next.next.next.next.next.next.next.next.next_sibling.text
			try:
				desc += soup.noscript.next_sibling.next_sibling.next.next.next.next.next.next.next.next.next_sibling.next_sibling.text
			except:
				pass
		except:
			pass
	except:
		print "I found ZERO text for %s.html" % i
		pass	
	myfile = open("/Users/ianfitzpatrick/code/dystopiabar/sessioncorpus.txt", "a")
	myfile.write(desc.encode('utf-8'))

# Parse Pages for Presenter Names and Save to File
import codecs
from bs4 import BeautifulSoup
for i in range(340):
	print "%s.html" % i
	f = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/pages/%s.html" % i, "r", "utf-8").read()		
	soup = BeautifulSoup(f)
	names = ""
	try:
		names += soup.h4.next.next.next.next.text
		names += '\n'
		try:
			names += soup.h4.next.next.next.next.next_sibling.next.text
			names += '\n'
		except:
			pass
	except:
		print "I found ZERO text for %s.html" % i
		pass	
	myfile = open("/Users/ianfitzpatrick/code/dystopiabar/names-real.txt", "a")
	myfile.write(names.encode('utf-8'))

# Create dystopian names from files
import codecs, random
first_names = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/names-fantasy.txt","r", "utf-8").read().split('\n')
last_names = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/names-real.txt","r", "utf-8").read().split('\n')

for i in range(300):
	print random.choice(first_names) + " " + random.choice(last_names)

# Download Presenter Pages
import time
import requests
from bs4 import BeautifulSoup
domain = 'http://wiki.minnestar.org'
presenters = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/presenters-links.txt","r").read().split('\n')

for counter, link in enumerate(presenters):
	print "Writing %s.html for URL %s" % (counter, link)
	r = requests.get(domain + link)
	t = r.text
	myfile = open("/Users/ianfitzpatrick/code/dystopiabar/presenters/%s.html" %  counter, "w")
	myfile.write(t.encode('utf-8'))
	print "Sleeping..."
	time.sleep(.5)

# Parse Presenter Pages for Bio Descriptions and Save to File
import codecs
from bs4 import BeautifulSoup
for i in range(500):
	print "%s.html" % i
	f = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/presenters/%s.html" % i, "r", "utf-8").read()		
	soup = BeautifulSoup(f)
	desc = ""
	try:
		desc += soup.find(id='mw-content-text').text
	except:
		print "I found ZERO text for %s.html" % i
	myfile = open("/Users/ianfitzpatrick/code/dystopiabar/presentercorpus.txt", "a")
	myfile.write(desc.encode('utf-8'))

# Create dystopian session descriptions (eh this didn't really give good results)
from textblob import TextBlob
import codecs, random
sessions = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/session_corpus_descriptions.txt","r", "utf-8").read()
slist = sessions.split('.')
pkd = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/dystopian-words.txt","r", "utf-8").read().split('\n')
blob = TextBlob(sessions)
np = blob.noun_phrases

for item in slist:
	blob = TextBlob(sessions)
	np = blob.noun_phrases
	if np:
		item = item.lower().replace(blob.noun_phrases[-1], random.choice(pkd))

	title = item.lower().replace(blob.noun_phrases[-1], random.choice(pkd)).title()

sessions = sessions.replace(item, random.choice(pkd))

for i, a in enumerate(np):
    if i % 5 == 0 :

# Generate  Makrov Chains
python markov.py parse sessions 2 /Users/ianfitzpatrick/code/dystopiabar/session_corpus_descriptions.txt
python markov.py gen sessions 800

# Trim Session Markov Output (delete short sentence/one-line paragraphs)
import codecs, random
descs = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/markov_session_desc.txt","r", "utf-8").read().split('.\n')

result = []
for item in descs:
	if len(item) > 224:
		result.append(item + '.\n')

# Light Dystopianization of Session Phrases
import random, codecs
from textblob import TextBlob
pkd = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/dystopian-words.txt","r", "utf-8").read().split('\n')
sessions = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/markov_session_desc.txt","r", "utf-8").read().split('\n')

for i in xrange(len(sessions)):
    data[i] = "everything"

for i in xrange(len(sessions)):
	blob = TextBlob(sessions[i])
	np  = blob.noun_phrases
	if np:
		sessions[i] = sessions[i].replace(random.choice(np).lower(), random.choice(pkd))
		sessions[i] = sessions[i].replace(random.choice(np).lower(), random.choice(pkd))
		sessions[i] = sessions[i].replace(random.choice(np).lower(), random.choice(pkd))
		sessions[i] = sessions[i].replace(random.choice(np).lower(), random.choice(pkd))
		sessions[i] = sessions[i].replace(random.choice(np).lower(), random.choice(pkd))
		sessions[i] = sessions[i].replace(random.choice(np).lower(), random.choice(pkd))

# Trim Bio Markov Output (delete short sentence/one-line paragraphs)
import codecs, random
descs = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/markov_presenter_bios.txt","r", "utf-8").read().split('\n')

result = []
for item in descs:
	if len(item) > 50:
		result.append(item + '.\n')

# Light Dystopianization of Presenter Bios Phrases
import random, codecs
from textblob import TextBlob
pkd = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/dystopian-words.txt","r", "utf-8").read().split('\n')
presenters = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/markov_presenter_bios.txt","r", "utf-8").read().split('\n')

for i in xrange(len(presenters)):
	blob = TextBlob(presenters[i])
	np  = blob.noun_phrases
	if np:
		presenters[i] = presenters[i].replace(random.choice(np).lower(), random.choice(pkd))
		presenters[i] = presenters[i].replace(random.choice(np).lower(), random.choice(pkd))
		presenters[i] = presenters[i].replace(random.choice(np).lower(), random.choice(pkd))
		presenters[i] = presenters[i].replace(random.choice(np).lower(), random.choice(pkd))
		presenters[i] = presenters[i].replace(random.choice(np).lower(), random.choice(pkd))
		presenters[i] = presenters[i].replace(random.choice(np).lower(), random.choice(pkd))


# Generate Presenter Bio Pages
import codecs
fullnames = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/names-dystopian.txt","r", "utf-8").read().split('\n')
bios = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/markov_presenter_bios_dystop.txt","r", "utf-8").read().split('\n')

pcounter = 0
for i in xrange(0,119):
	template = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/web/bio.html", "r", "utf-8").read()
	soup = BeautifulSoup(template)
	soup.find(id='fullname').append(fullnames[i])
	new_tag = soup.new_tag('p')
	new_tag.string = bios[pcounter]
	new_tag2 = soup.new_tag('p')
	new_tag2.string = bios[pcounter+1]
	soup.find(id='bio').append(new_tag)
	soup.find(id='bio').append(new_tag2)
	filename = fullnames[i].lower().replace(' ', '-')
	myfile = open("/Users/ianfitzpatrick/code/dystopiabar/web/bios/%s.html" % filename, "w")
	myfile.write(soup.encode('utf-8'))
	pcounter += 2

# Generate Session Pages
import codecs, random
from bs4 import BeautifulSoup
fullnames = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/names-dystopian.txt","r", "utf-8").read().split('\n')
session_titles = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/dystopian-sessions-full-list-no-times.txt","r", "utf-8").read().split('\n')
session_desc = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/markov_session_desc_dystop.txt","r", "utf-8").read().split('\n')
room_names = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/room-names.txt","r", "utf-8").read().split('\n')
bios = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/markov_presenter_bios_dystop.txt","r", "utf-8").read().split('\n')

bio_pcounter = 0
desc_pcounter = 0
for i in xrange(0,118):
	template = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/templates/session.html", "r", "utf-8").read()
	soup = BeautifulSoup(template)
	
	slugify_name = fullnames[i].lower().replace(' ', '-')
	
	# Presenter Link
	a_tag = soup.new_tag('a', href='/bios/%s.html' % slugify_name)
	a_tag.string = fullnames[i]
	soup.find(id='presenterlink').append(a_tag)
	
	# Prestern Name
	soup.find(id='presentername').append(fullnames[i])
	
	# Room Name
	soup.find(id='room').append('Room: ' + room_names[i])
	
	# Bio
	new_tag = soup.new_tag('p')
	new_tag.string = bios[bio_pcounter]
	new_tag2 = soup.new_tag('p')
	new_tag2.string = bios[bio_pcounter+1]
	soup.find(id='bio').append(new_tag)
	soup.find(id='bio').append(new_tag2)
	bio_pcounter += 2

	# Session Title
	soup.find(id='sessiontitle').append(session_titles[i])

	# Session Description
	session_length = random.randrange(2,4)

	for n in range(session_length):
		desc_tag = soup.new_tag('p')
		desc_tag.string = session_desc[desc_pcounter + n]
		soup.find(id='session_description').append(desc_tag)		

	desc_pcounter += session_length

	# Save Results
	myfile = open("/Users/ianfitzpatrick/code/dystopiabar/web/%s/index.html" % str(i + 100), "w")
	myfile.write(soup.encode('utf-8'))

# Generate Home Page
import codecs, random
fullnames = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/names-dystopian.txt","r", "utf-8").read().split('\n')
session_titles = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/dystopian-sessions-full-list-no-times.txt","r", "utf-8").read().split('\n')

template = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/web/home.html", "r", "utf-8").read()
soup = BeautifulSoup(template)

i = 0
for i in range(0,119):
	# Time Slot
	if i % 15 == 0:	
		
		# Figure out time
		if i == 0:
			session_time = '9AM'
		elif i == 15:
			session_time = '10AM'
		elif i == 30:
			session_time = '11AM'			
		elif i == 45:
			session_time = '1PM'
		elif i == 60:
			session_time = '2PM'
		elif i == 75:
			session_time = '3PM'
		elif i == 90:
			session_time = '4PM'									

		# Add time List Item
		new_li_time = soup.new_tag('li')
		new_h3_time = soup.new_tag('h3')
		new_h3_time['class'] = 'time'
		new_h3_time.string = session_time
		new_li_time.append(new_h3_time)
		soup.find(id='sessionlist').append(new_li_time)

	# Session Title
	new_li_tag1 = soup.new_tag('li')	
	new_h4_tag = soup.new_tag('h4')	
	new_a_tag1 = soup.new_tag('a', href='/%s/' % str(i + 100))
	new_a_tag1.string = session_titles[i]
	new_h4_tag.append(new_a_tag1)
	new_li_tag1.append(new_h4_tag)

	# Session Presenter
	new_div_tag = soup.new_tag('div')
	new_div_tag.string = 'by '
	new_div_tag['class'] = 'presenter'

	slugify_name = fullnames[i].lower().replace(' ', '-')
	new_a_tag2 = soup.new_tag('a', href='/bios/%s.html' % slugify_name)
	new_a_tag2.string = fullnames[i]
	new_div_tag.append(new_a_tag2)
	new_li_tag1.append(new_div_tag)

	# Finally, append list item
	soup.find(id='sessionlist').append(new_li_tag1)	

# Save Results
myfile = open("/Users/ianfitzpatrick/code/dystopiabar/web/index.html", "w")
myfile.write(soup.encode('utf-8'))










