// iterate over an array
var pageNames = ['Home', 'About Us', 'Contact Us', 'JavaScript Playground', 'News', 'Blog'];
for (var p in pageNames) { // generally not recommended to use a for in loop with arrays, because it doesn't always return the items from the array in order
	console.log(p + ' is ' + pageNames[p]);
}

// iterate over an object
var pages = {
	'first' : 'Home',
	'second' : 'About Us',
	'third' : 'Contact Us',
	'fourth' : 'JavaScript Playground',
	'fifth' : 'Blog',
};
for (var p in pages) {
	if (pages.hasOwnProperty(p)) { // hasOwnProperty prevents you from accidentally enumerating over an inherited property
		console.log(p + ' is ' + pages[p]);
	}
}

// More info:
// https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Statements/for...in