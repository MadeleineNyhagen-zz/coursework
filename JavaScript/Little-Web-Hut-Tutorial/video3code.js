$(document).ready(function() {

	$("h1").mouseenter(function() { // click function is activated on release of mouse button, mousedown activates when button is pushed, mouseenter whenever mouse pointer is moved over h1 tag
		$(this).css("background-color","red");
	});

	$("h1").mouseleave(function() { // mouseup event will happen whenever the user releases the mouse button while over an h1 element, mouseleave whenever mouse is moved away from h1 tag
		$(this).css("background-color","yellow");
		// $(this).unbind(); // unbind removes all events from the selected tag
		$("*").unbind("mouseleave"); // unbind mouseleave events from all elements
	});

}); // this function ensures that the html has fully run before running the JavaScript