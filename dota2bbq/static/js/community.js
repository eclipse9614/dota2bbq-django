$(document).ready(function(){

	$('#site_picker').change(function() {
		if($(this).val() != '0') {
			$.ajax('/feed/feed',
			{
				dataType: 'json',
				data: {
					'url': $(this).val()
				},
				beforeSend: function(){
					$('#feed_display')
					.html('')
					.append('<h3>Loading</h3>')
					.append($('<div/>')
						.addClass('progress progress-striped active')
						.append($('<div/>')
							.addClass('bar')
							.attr('id', 'feed_progress')
							.css('width', '100%')));
				},
				success: function(json) {
					if(json.Result == 'SUCCESS') {
						var feed = $($.parseXML(json.Content));
						var channel = feed.find('channel');
						$('#feed_display').html('').append("<h1 id='feed_title'></h1>");
						$('#feed_title')
						.html('Channel: ' + channel.children('title').text());
						$('<a/>')
						.attr('href', channel.children('link').text())
						.html('Link: ' + channel.children('link').text())
						.addClass('label')
						.insertAfter($('#feed_title'));
						feed.find('item').each(function(){
							var title = $(this).children('title');
							var link = $(this).children('link');
							var pubData = $(this).children('pubDate');
							var description = $(this).children('description')

							var $item_section = $('<div/>').addClass('feed_item');
							$("<h4/>").html('Title: ' + title.text())
							.appendTo($item_section);
							var preset = $('<p>');
							$('<a/>').addClass('label')
							.html('Link: ' + link.text().substr(0, 50))
							.attr('href', link.text())
							.appendTo(preset);
							$('<br/>').appendTo(preset);
							$('<span/>').html('Publish Date: ' + pubData.text())
							.addClass('label label-info')
							.appendTo(preset);
							$('<br/>').appendTo(preset);
							$('<span/>').html('Description: ')
							.addClass('label label-success').appendTo(preset);
							preset.appendTo($item_section);

							$('<p/>').html(description.text())
							.appendTo($item_section);
							$item_section.appendTo($('#feed_title'));


						});
					} else {
						alert(json.Content)
					}
				}
			});
			
		}
	});
});