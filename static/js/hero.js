$(document).ready(function() {

	//lore expanding
	$('#hero_lore_btn').click(function() {
		var $lore = $('.hero_lore > p');
		$lore.toggleClass('hero_lore_height');
		if($(this).html() == 'expand')
		{
			$(this).html('shrink');
		}
		else
		{
			$(this).html('expand');
		}
	});

	//tabs
	var hero_name = $("#hero_name").html();

	$("#skill_tabs").tabs();
	$('#skillbuild_tabs').tabs();

	//skill tooltip based on ajax
	$(".skill")
	.each(function(){
		$('<img>')
		.attr('src', "/static/images/skills/" +
			($(this).data("hero") + '_' + $(this).data('skill'))
			.toLowerCase().replace(/ /g, '_').replace(/'/g, '').replace(/\?/g, '') +
			'.png')
		.width('128px')
		.height('128px')
		.attr('title', '')
		.prependTo($(this));
	});
	$(".skill").tooltip({
		position: {
			my: "right center",
			at: "left center",
			offset: "-20"
		},
		content: function() {
			var $parent = $(this).parent();

			var display = "";
			if($parent.data('type') == 'True')
			{
				display += "Type: Active";
			}
			else
			{
				display += "Type: Passive";
			}


			if($parent.data('manacost') != 'None')
			{
				display += ("<br>Manacost: " + $parent.data('manacost'));
			}

			if($parent.data('cooldown') != 'None')
			{
				display += ("<br>Cooldown: " + $parent.data('cooldown'));
			}

			return display;
		}
	});

	$('#skillbuild_tabs')
	.tooltip({
		position: {
			my: "center bottom",
			at: "center top",
		},
		content: function(){
			return $(this).data('skill')
		}
	})
	.find('img').hover(function(){
		var skill_name = $(this).data('skill');

		if(skill_name != 'Stats')
		{
			var tab = $('.skill[data-skill="' + skill_name + '"]');
			var index = $('.skill').index(tab);
			$('#skill_tabs').tabs('option', 'active', index);
		}
		else
		{
			$(this).data('skill', 'Stats: Increase all attributes by 2')
		}
	});




});
