import re
import codecs
from json import JSONEncoder
# import redis

# r = redis.StrictRedis(host='localhost', port=6379, db=0)

class MyEncoder(JSONEncoder):
	def default(self, o):
		return o.__dict__  

class test_question:
	id = ''
	question = ''
	answer = ''

test = []

radio_test_file = codecs.open('general.txt', 'r', 'utf-8')

radio_test = radio_test_file.read()

regex = re.compile(r"(?P<id>T[0-9][A-C][0-9][0-9]) \((?P<answer>[A-G])\)\s*(?P<question>[^~]*)")

match = regex.findall(radio_test)

#print(match.groups())
#print(len(match))

for question in match:
	item = test_question()
	item.id = question[0]
	item.answer = question[1]
	item.question = question[2]

	# r.hset("ham:"+item.id, 'question', item.question)
	# r.hset("ham:"+item.id, 'answer', item.answer)

	test.append(item)

# for thing in test:
# 	print(thing.id)
# 	print(thing.question)
# 	print(thing.answer)

print MyEncoder().encode(test)
