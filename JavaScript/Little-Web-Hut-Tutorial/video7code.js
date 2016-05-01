$(document).ready(function() {
	$("h1").click(function() {
		//$("p").text("new <b>text</b>"); // if you try and use html tags in the text method, they will be displayed insead of having their normal effect
		//$("div").html('new <b style="color: red";>text</b>'); // if you use html tags in the html method however, they will work as intended
		//$("div").empty(); // to remove all elements from div
		//$("p").append(" More text") // to append text
		//$("div").append("<p> New text</p>") // to append html
		//$("div").after("<p> New text </p>") // to add html after div
		//$("p").after("<p> New text </p>") // to add html after each paragraph
		//$("div").prepend("<p> New text </p>") // to add html at the beginning of the div
		//$("div").before("<p> New text </p>") // to add html before the div
		//$("p").replaceWith("<h2> New text </h2>") // change an element
		$("#picture").attr("src", "maru2.gif");
	});
}); // this function ensures that the html has fully run before running the JavaScript