import re
import codecs
from json import JSONEncoder
# import redis

# r = redis.StrictRedis(host='localhost', port=6379, db=0)

class TestFile:
	def __init__(self, char, filename):
		self.char = char
		self.filename = filename


class MyEncoder(JSONEncoder):
	def default(self, o):
		return o.__dict__  

class test_question:
	id = ''
	question = ''
	answer = ''

test_files = [TestFile('T', 'tech.txt'), TestFile('G', 'general.txt')]

for test_file in test_files:

	test_questions = []

	radio_test_file = codecs.open(test_file.filename, 'r', 'utf-8')

	radio_test_txt = radio_test_file.read()

	regex_string = r"(?P<id>%c[0-9][A-C][0-9][0-9]) \((?P<answer>[A-G])\)\s*(?P<question>[^~]*)" % test_file.char
	regex = re.compile(regex_string)

	match = regex.findall(radio_test_txt)

	for question in match:
		item = test_question()
		item.id = question[0]
		item.answer = question[1]
		item.question = question[2]

		# r.hset("ham:"+item.id, 'question', item.question)
		# r.hset("ham:"+item.id, 'answer', item.answer)

		test_questions.append(item)

	json_db = codecs.open(test_file.filename + ".json", 'w', 'utf-8')
	json_db.write(MyEncoder().encode(test_questions))
	#print(MyEncoder().encode(test_questions))

#for thing in test_questions:
	#print(thing.id)
	#print(thing.question)
	#print(thing.answer)

