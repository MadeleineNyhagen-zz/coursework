$(document).ready(function() {
	$("h1").click(function() {
		//$(this).add("p").css("background-color", "red"); // the add method adds elements with the p tag to the affected elements
		//$("p").not("p.second").css("background-color", "red"); // use the not method to exclude an element from those affected, in this case the p element with class 'second'
		//$("div").next().css("background-color", "red"); // the next method affects the next element that's a sibling of the selected element
		//$("h1").next().css("background-color", "red"); // in this case, it affects the next siblings of both h1 elements
		//$("h1").next("div").css("background-color", "red"); // here it only affects the next sibling of the h1 if it's a div element
		//$(this).next().css("background-color", "red"); // can also use the next method with a this selector
		//$("p").prev().css("background-color", "red"); // use prev to affect the previous sibling of the selected element
		//$(this).parent().css("background-color", "red"); // use parent to select the parent of the selected element
		//$("div").find("p").css("background-color", "red"); // use find to select the descendants of an element, in this case all p elements descended from a div
		//$("p").first().css("background-color", "red"); // first allows us to select the first of the selected element
		//$("p").last().css("background-color", "red"); // last allows us to select the last of the selected element
		$("p").eq(1).css("background-color", "red"); // use eq to select a specific element with an index number, in this case the second p element
	});
}); // this function ensures that the html has fully run before running the JavaScript