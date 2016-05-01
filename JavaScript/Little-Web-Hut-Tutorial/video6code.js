$(document).ready(function() {
	$("h1").mouseenter(function(){
		//$(this).css("margin-left", "+=50px"); // increment the margin-left property by 50px
		// to target multiple css properties, the format looks slightly different:
		/*$(this).css({
			"margin-left": "+=50px",
			"background-color": "red"
		});
		*/
		//$(this).addClass("emphasis shrink"); // adding classes to an element
		//$(this).removeClass("emphasis"); // removing classes from an element: leave parentheses empty to remove all classes
		//$(this).removeClass("emphasis").addClass("shrink"); // combining removeClass and addClass to swap classes
		$(this).toggleClass(); // if no classes are specified in the toggleClass method, any class that's already been specified for an element will be toggled
	});
}); // this function ensures that the html has fully run before running the JavaScript