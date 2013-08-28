'use strict';
var fs = require('fs'),
redis = require('redis'),

client = redis.createClient();
client.select(2);

fs.readFile('data.json', function(e, data) {
	var d = JSON.parse(data), i, l, item, count = 0;
	for( i = 0, l = d.length; i < l; i++ ) {
		item = d[i];
		client.hset( item.id, 'question', item.question );
		client.hset( item.id, 'answer', item.answer );
	}

	process.exit();
});
