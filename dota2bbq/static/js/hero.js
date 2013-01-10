$(document).ready(function() {

	$hero_lore_para = $('#hero_lore_para');
	var hero_lore_content = $hero_lore_para.html();
	if(hero_lore_content.length > 1000) {

		$('#hero_full_story')
		.find('p')
		.html(hero_lore_content);
		$hero_lore_para
		.html(hero_lore_content.substr(0, 1000) + '......')
		.tooltip(
			{
				position: { my: "left center", at: "right center" }
			}
		)
		.attr('title', 'Click lore to open full hero story')
		.tooltip('open')
		.click(function() {
			//window.location = window.location + '#hero_full_story';
			$('#hero_full_story').modal('show');
		});
	}


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
	});




});
