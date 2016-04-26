var thing = 12;
thing = 'twelve';
typeof thing;

thing = 12;
typeof thing;

thing = false;
typeof thing;

thing = {};
typeof thing;

thing = [];
typeof thing; // since an array in JavaScript is an object this isn't helpful in distinguishing between an array and an object, but this is:
typeof thing === 'object' && thing.hasOwnProperty('length'); // true

thing = {};
typeof thing === 'object' && thing.hasOwnProperty('length'); // false

NaN;
typeof NaN; // this will, confusingly, return number

typeof null; // also confusingly, this will return object
thing === null;
thing = null;
thing;
thing === null;

// More info:
// https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Operators/typeof