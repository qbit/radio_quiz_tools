'use strict';
function testSelect($scope) {
	$scope.loadTech = function() {
		console.log('tech');
	};
	$scope.loadGen = function() {
		console.log('gen');
	};
	$scope.loadExt = function() {
		console.log('ext');
	};
}
