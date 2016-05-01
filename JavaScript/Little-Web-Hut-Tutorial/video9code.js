$(document).ready(function() {
	//var hText = "This is just some text.";
	//var hText = $("#head1").text(); // using the text method here with no argument says that we want to read the text, which will return a text string
	//var text1 = "The heading text is ";
	//var text2 = text1 + hText;

	//var hText = "The heading text is " + $("#head1").text();
	
	//var lineNum = 0;
	//var aNumber = 5;
	//lineNum = aNumber - 4;

	//$("h1").click(function() {
		//$("p").text(hText);
	//	$("p").css("background-color", "yellow");
	//	$("p").eq(lineNum).css("background-color", "red");
	//	lineNum++; // increment the lineNum variable each time h1 is clicked
	//	if (lineNum > 2) {lineNum = 0;}
	//});

	var imageName = ["maru2.gif", "maru3.gif", "maru.gif"];
	var indexNum = 0;

	$("#picture").click(function() {
		// to cycle through pictures when the image is clicked:
		//$("#picture").attr("src", imageName[indexNum]);
		//indexNum++
		//if (indexNum > 2) {indexNum = 0;}

		// instead of just swapping out images abruptly, we can fade them like this:
		$("#picture").fadeOut(300, function() {
			$("#picture").attr("src", imageName[indexNum]);
			indexNum++;
			if (indexNum > 2) {indexNum = 0;}
			$("#picture").fadeIn(500);
		});
	});
}); // this function ensures that the html has fully run before running the JavaScript