# Pull noun phrases from corpus
from textblob import TextBlob
import codecs, os

corp_dir = '%s/corpus/dystopia' % os.getcwd()
corp_filename = 'pkd-scanner.txt'
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

for i, (a, b) in enumerate(np_sorted):
	myfile = open(file_out, "a")
	try:
		if len(a.split(" ")) > 1:
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

# Create dystopian names from files
import codecs, random
first_names = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/names-fantasy.txt","r", "utf-8").read().split('\n')
last_names = codecs.open("/Users/ianfitzpatrick/code/dystopiabar/names-real.txt","r", "utf-8").read().split('\n')

for i in range(300):
	print random.choice(first_names) + " " + random.choice(last_names)


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

