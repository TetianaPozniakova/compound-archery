/**
 * Created with PyCharm.
 * User: noctule
 * Date: 29.12.13
 * Time: 18:46
 * To change this template use File | Settings | File Templates.
 */

$(function() {
    $( "#id_birth_date" ).datepicker({
        changeMonth: true,
        changeYear: true
    });
});

$(function() {
//    $('#participants-lists').hide(); //hide field on start

    $('#reg-tournament').change(function() {
    $('.lists').hide();
    var selected = $('#reg-tournament').val();
    document.getElementById(selected).style.display="block";
    });
});