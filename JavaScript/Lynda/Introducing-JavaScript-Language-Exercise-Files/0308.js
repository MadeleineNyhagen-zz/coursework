var string1 = 'This is the longest string ever.';
var string2 = 'This is the shortest string ever.';
var string3 = 'Is this the thing called Mount Everest?';
var string4 = 'This is the Sherman on the Mount.';

var regex = /this/;

console.log( regex.test(string1) );
console.log( regex.test(string2) );
console.log( regex.test(string3) );
console.log( regex.test(string4) );

regex = /this/i; // the added 'i' serves to make this regex case insensitive

regex = /^this/i; // the ^ indicates that we're looking for strings that begin with 'this'

regex = /this$/i; // the $ indicates that we're looking for strings that end with 'this'

regex = /ever.$/i; // the . stands for any character

regex = /ever\.$/i; // to look for an actual . you can escape it with a backslash

regex = /Moun.$/i;

// More info:
// https://developer.mozilla.org/en-US/docs/JavaScript/Guide/Regular_Expressions
// http://www.regular-expressions.info