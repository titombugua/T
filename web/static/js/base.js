// NAVBAR REVEAL ON SCROLL

$(function() {
  //caches a jQuery object containing the header element
  var header = $('.navbar');
  $(window).scroll(function() {
    var scroll = $(window).scrollTop();

    if (scroll >= 600) {
      header.removeClass('.navbar').addClass('navbar-visible').fadeIn();
    }
    else {
      header.removeClass('navbar-visible').addClass('.navbar').fadeIn();
    }
  });
});
// AUTO HIDE NAVBAR TOGGLE

$(".navbar-nav li a").click(function(event) {
    if (!$(this).parent().hasClass('dropdown'))
        $(".navbar-collapse").collapse('hide');
});