$(document).ready(function() {
	var orangeBackground = $(".orangeBackground"),
		pinkBackground = $(".pinkBackground"),
		palm = $(".palm"),
		pyramid = $(".pyramid"),
		sun = $(".sun"),
		title = $(".title");
	$(".map-maya").css("visibility", "hidden");
	$(".zona1").css("visibility", "hidden");
	$(".zona2").css("visibility", "hidden");
	$(document).scroll(function() {
		var scrolltop = window.pageYOffset;
		pinkBackground.css("right", -scrolltop*1 + 'px');
		orangeBackground.css("left", -scrolltop*1 + 'px');
		title.css("top", -scrolltop*2 + 'px');
		sun.css("top", -scrolltop*3 + 'px');

		
		if(scrolltop >= 745 && scrolltop <= 1000) {
			$(".map-maya").addClass("bounceInRight");
			$(".map-maya").css("visibility", "visible");
		}
		else if(scrolltop >= 2550 && scrolltop <= 2710) {
			$(".zona1").css("visibility", "visible");
			$(".zona1").addClass("bounceInRight");
			
		}
		else if (scrolltop >= 2880) {
			$(".zona2").css("visibility", "visible");
			$(".zona2").addClass("bounceInLeft");
			
		}
		console.log(scrolltop);

	});

});