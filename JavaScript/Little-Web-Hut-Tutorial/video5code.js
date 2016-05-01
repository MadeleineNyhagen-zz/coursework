$(document).ready(function() {
	$("h1").click(function(){
		$("h2").animate({
			//"font-size": "3em", // changes font-size
			"font-size": "toggle", // can also use hide, show, or toggle as value
			"width": "50%",
			"left": "+=100px" // left property will only have an effect on an element with a position property of relative, absolute, or fixed
			// adding += to the value of the left property means that every time this function happens, the left property will be incremented by 100px
		}, 1000, function() {
			$("h3").fadeOut(1000); // fadeOut h3 element after animation effects on h2 have resolved
		}); // first argument in animate function is the css properties to be animated,
		//second argument in animate function is length of time in milliseconds
	});
}); // this function ensures that the html has fully run before running the JavaScript