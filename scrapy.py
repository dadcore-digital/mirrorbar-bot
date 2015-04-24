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