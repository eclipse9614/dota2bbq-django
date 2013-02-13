$(document).ready(function(){
    $('#add_comp').click(function(){
        var cur_component_name = $('#cur_comp').val();

        var $button = $('<button/>')
        .addClass('del_comp')
        .attr('type', 'button')
        .html("Delete this component")
        .click(del);

        $('<li />')
        .html('<span class="component">' + cur_component_name + '</span>')
        .append($button)
        .appendTo($('#components'));
    });


    $('.del_comp').click(del);

    $('#input').submit(function(){
        var recipe = [];
        $('.component').each(function(){
            recipe[recipe.length] = $(this).html();
        });
        $('#recipe').val(recipe.join('/'));
    });
});


function del(){
    $(this).parent().remove();
}