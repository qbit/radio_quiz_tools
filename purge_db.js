'use strict';
var fs = require('fs'),
redis = require('redis'),
count = 0,

to_db = process.argv[2],

client = redis.createClient();
client.select(to_db);

if ( !to_db || to_db === 1 || to_db === '1' ) {
	throw new Error( 'Please pass in db number that is not 1' );
}

console.log('Purging data for db %d', to_db );
client.keys( '*', function( e, d ) {
	d.forEach(function( item, index) {
		client.del( item );
		count++;
		if ( count === d.length ) {
			process.exit();
		}
	});
});
