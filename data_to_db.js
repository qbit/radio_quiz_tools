'use strict';
var fs = require('fs'),
redis = require('redis'),

to_db = process.argv[2],
from_file = process.argv[3],

client = redis.createClient();
client.select(to_db);

console.log('Importing from "%s" to "%s"', from_file, to_db );
fs.readFile(from_file, function(e, data) {
	if ( e  ) {
		throw e;
	}
	var d = JSON.parse(data), i, l, item, count = 0;
	for( i = 0, l = d.length; i < l; i++ ) {
		item = d[i];
		client.hset( item.id, 'question', item.question );
		client.hset( item.id, 'answer', item.answer );
	}

	process.exit();
});
