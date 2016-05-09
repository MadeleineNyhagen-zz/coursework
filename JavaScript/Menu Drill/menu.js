$(document).ready(function() {
    // hide the p tags
    $("li").hide();
    $("ul").mouseover(function() {
    	$("li").show();
    });
    $("ul").mouseout(function() {
    	$("li").hide();
    });
    $("li").mouseover(function() {
    	$(this).css("background-color", "yellow");
    });
    $("li").mouseout(function() {
    	$(this).css("background-color", "white");
    });

});