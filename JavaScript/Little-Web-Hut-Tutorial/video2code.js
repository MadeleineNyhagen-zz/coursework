$(document).ready(function() {
	$("#testbutton, strong").click(function() {
		// this line specifies that the div element's css background-color property will be changed to red:
		// $("div, strong, #testbutton").css("background-color","red"); // the $("") is used to specify a selector, which can be an element, an id, etc.
		// $("div > p").css("background-color","red"); // in this case, we're selecting the paragraphs that are children of div elements
		// $("div > p:first-child").css("background-color","red"); // to select only the paragraph that's the first child of a div element
		// can also specify p:last-child
		// $("div strong").css("background-color","red"); // this selects all strong elements that are descendants of a div
		// $("p:even").css("background-color","red"); // to select every other element of a type, follow it with 'even' or 'odd'
		// $("#third, strong.multiple").css("background-color","red"); // selects elements with id third and strong tags with class multiple
		$(this).css("background-color","red"); // selects whatever triggered this function

	});
}); // this function ensures that the html has fully run before running the JavaScript