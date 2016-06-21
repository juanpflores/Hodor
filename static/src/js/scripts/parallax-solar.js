
$(document).ready(function() {
	var mercurio = $(".planet-mercurio"),
		venus = $(".planet-venus"),
		tierra = $(".planet-tierra"),
		marte = $(".planet-marte"),
		jupiter = $(".planet-jupiter"),
		saturno = $(".planet-saturno"),
		urano = $(".planet-urano"),
		neptuno = $(".planet-neptuno");
	var pos_mercurio = mercurio.offset().top,
		pos_venus = venus.offset().top,
		pos_tierra = tierra.offset().top,
		pos_marte = marte.offset().top,
		pos_jupiter = jupiter.offset().top,
		pos_saturno = saturno.offset().top,
		pos_urano = urano.offset().top,
		pos_neptuno = neptuno.offset().top;

	$(document).scroll(function() {
		var scrolltop = window.pageYOffset;

		mercurio.css("left", (scrolltop*1.6 - pos_mercurio) + 'px');
		venus.css("left", (scrolltop*1.4 - pos_venus) + 'px');
		tierra.css("left", (scrolltop*1.3 - pos_tierra) + 'px');
		marte.css("left", (scrolltop*1.2 - pos_marte) + 'px');
		jupiter.css("left", (scrolltop*1.1 - pos_marte) + 'px');
		saturno.css("left", (scrolltop*.9 - pos_marte) + 'px');
		urano.css("left", (scrolltop*.8 - pos_marte) + 'px');
		neptuno.css("left", (scrolltop*.7 - pos_marte) + 'px');				
	});
});