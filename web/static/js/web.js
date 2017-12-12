// AUTO HIDE NAVBAR TOGGLE

// $(".navbar-nav li a").click(function(event) {
//     if (!$(this).parent().hasClass('dropdown'))
//         $(".navbar-collapse").collapse('hide');
// });

// SCROLL INTO VIEW

// Animations 
// NAVBAR
window.sr = ScrollReveal({ reset: false, viewFactor: 0.15, easing: 'cubic-bezier(0.6, 0.2, 0.1, 1)', });
sr.reveal('.navbar', {
    duration: 600,
    origin: 'top'
})
// CAROUSEL

sr.reveal('.reveal-left', {
    duration: 500,
    delay: 500,
    origin: 'left'
    // distance: '300px',

})
sr.reveal('#reveal-bottom', {
    duration: 1500,
    // delay: 500,
    origin: 'bottom',
    distance: '150px',
})


// SCROLL TOP
// function() {

//     var href = $(this).attr("href");

//     if ($(href).length == 0) {

//         var nameSelector = "[name=" + href.replace("#", "") + "]";

//         if (href == "#") {
//             scrollBodyTo(0, href);
//         } else if ($(nameSelector).length != 0) {
//             scrollBodyTo($(nameSelector).offset().top, href);
//         } else {
//             window.location = href;
//         }
//     } else {
//         scrollBodyTo($(href).offset().top, href);
//     }
//     return false;
// }