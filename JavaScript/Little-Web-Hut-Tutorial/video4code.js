$(document).ready(function() {
	//$("h2").hide();
	$("h1").click(function() {
		//$("h2").toggle(1000); // the number passed into the hide, show or toggle functions is the length of time the event should last, in milliseconds
		//$("h2").slideToggle(1000); // the slideUp event hides elements by changing their height, the slideDown event reveals items by changing their height
		// slideToggle switches between slideDown and slideUp as appropriate
		//$("h2").fadeToggle(1000); // fadeOut hides an element by changing its opacity, fadeIn reveals an element, and fadeToggle toggles
		//$("h2").fadeTo(1000, 0.3); //changes opacity to level specified, first argument is length of time event lasts and second argument is ending opacity
		//$("h2").delay(2000).fadeToggle(1000); // fadeToggle with a delay of two seconds
		$("h2").hide(1000, function() { // adding a callback function so that after h2 is hidden, h3 is hidden as well
			$("h3").fadeOut(1000);
		});
	});

}); // this function ensures that the html has fully run before running the JavaScript