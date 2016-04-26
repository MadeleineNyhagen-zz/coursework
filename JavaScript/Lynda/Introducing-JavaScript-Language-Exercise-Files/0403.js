var animal1 = 'monkey';
var animal2 = 'bear';
var animal3 = 'tiger';

animal1 === 'monkey' && animal2 === 'bear'; // true

animal1 === 'ape' && animal2 === 'bear'; // false

animal1 === 'ape' && animal2 === 'bear' && animal3 === 'tiger'; // false

animal1 === 'monkey' && animal2 === 'bear' && animal3 === 'tiger'; // true

animal1 === 'monkey' || animal2 === 'bear'; // true

animal1 === 'ape' || animal2 === 'bear'; // true

animal1 === 'ape' || animal2 === 'ostrich'; // false

animal1 === 'monkey' || animal2 === 'bear' && animal3 === 'tiger'; // true

animal1 === 'ape' || animal2 === 'bear' && animal3 === 'tiger'; // true

(animal1 === 'ape' || animal2 === 'monkey') && animal3 === 'tiger'; // false

animal1 === 'monkey' && animal2 === 'bear'; // true

!(animal1 === 'monkey' && animal2 === 'bear'); // false

// in JavaScript, operator precedence means that && (and) will always be evaluated before || (or)
// but using parentheses can eliminate any doubts about how a statement will evaluate

// More info:
// https://developer.mozilla.org/en-US/docs/JavaScript/Guide/Expressions_and_Operators#Logical_operators