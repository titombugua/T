// NAVBAR REVEAL ON SCROLL

$(function() {
    //caches a jQuery object containing the header element
    var header = $('.navbar');
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();

        if (scroll >= 40) {
            header.removeClass('bg-transparent').addClass('bg-white', 'sticky-top').fadeIn();
        } else {
            header.removeClass('bg-white').addClass('bg-transparent').fadeIn();
        }
    });
});

// COLOR SPECIFC WORDS
$('p').html(
    function(i, h) {
        return h.replace(/(Mbugua)/g, '<span class="g-red">$1</span>');
    });