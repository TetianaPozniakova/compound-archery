function fanPictureSet2(divid) {
    var ps2imgs = $("#"+divid+" .pictureset2 IMG.picture");
    $("#"+divid+" .pictureset2").delegate("img", "mouseenter", function() {
	ps2imgs.eq(0).addClass("rotate1");
	ps2imgs.eq(1).addClass("rotate2");
	ps2imgs.eq(0).css("left", "50px");
	ps2imgs.eq(1).css("left", "150px");
    }).delegate('img', 'mouseleave', function() {
	ps2imgs.eq(0).removeClass("rotate1");
	ps2imgs.eq(1).removeClass("rotate2");
	ps2imgs.eq(0).css("left", "");
	ps2imgs.eq(1).css("left", "");
    });
}

function fanPictureSet3(divid) {
    var ps3imgs = $("#"+divid+" .pictureset3 IMG.picture");
    $("#"+divid+" .pictureset3").delegate("img", "mouseenter", function() {
	ps3imgs.eq(0).addClass("rotate1");
	ps3imgs.eq(1).addClass("rotate2");
	ps3imgs.eq(2).addClass("rotate3");
	ps3imgs.eq(0).css("left", "50px");
	ps3imgs.eq(2).css("left", "150px");
    }).delegate('img', 'mouseleave', function() {
	ps3imgs.eq(0).removeClass("rotate1");
	ps3imgs.eq(1).removeClass("rotate2");
	ps3imgs.eq(2).removeClass("rotate3");
	ps3imgs.eq(0).css("left", "");
	ps3imgs.eq(2).css("left", "");
    });

}

var prettyparams = {
        animation_speed: 'fast',
        slideshow: 3000,
        autoplay_slideshow: false,
        opacity: 0.7,
        show_title: false,
        allow_resize: true,
        default_width: 600,
        default_height: 480,
        counter_separator_label: '/',
        overlay_gallery: true,
        changepicturecallback: function() {$pp_overlay.css({'height':$(document).height()})},
        };

$(document).ready(function() {
    $('.inline-ps3').each(function() {
	fanPictureSet3($(this).attr("id"));
    });
    $('.inline-ps2').each(function() {
	fanPictureSet2($(this).attr("id"));
    });
    $("a[rel^='pictureset']").prettyPhoto(prettyparams);
    $("a.picture").prettyPhoto({social_tools:false});
});
