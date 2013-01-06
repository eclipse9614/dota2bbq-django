$(document).ready(function(){
    $('#close_btn').click(function(){
        window.location = '/dota2bbq/';
    });

    $('#hero_edit').click(validateHero);
    $('#hero_delete').click(validateHero);
    $('#skill_edit').click(validateHero);
    $('#skill_build').click(validateHero);

    $('#item_edit').click(validateItem);
    $('#item_delete').click(validateItem);

});



function validateHero(){
    var hero_name = $('#hero_name').val();
    if(hero_name == '-1')
    {
        alert('Pick a hero first');
        return false;
    }
    else
    {
        var href = $(this).attr('href');
        href += (hero_name + '/');
        $(this).attr('href', href);
        return true;
    }
}


function validateItem(){
    var item_name = $('#item_name').val();
    if(item_name == '-1')
    {
        alert('Pick an item first');
        return false;
    }
    else
    {
        var href = $(this).attr('href');
        href += (item_name + '/');
        $(this).attr('href', href);
        return true;
    }
}