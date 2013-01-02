$(document).ready(function(){
    $('#close_btn').click(function(){
        window.location = '/dota2bbq/';
    });

    $('#hero_edit').click(validate);
    $('#hero_delete').click(validate);
});



function validate(){
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