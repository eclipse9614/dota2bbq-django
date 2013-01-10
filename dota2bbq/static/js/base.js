$(document).ready(function(){
	var href = window.location.pathname;
	$(".nav").children('li').removeClass('active')
		.find('a[href="' + href.toLowerCase() + '"]').parent().addClass('active');
	$('#manage_btn').click(function(){
		window.location = '/manager';
	});
});

