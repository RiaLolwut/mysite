$(document).ready(function() {
      $(".pulse-this").mouseenter(function(event) {
          $(this).addClass("animate__animated animate__pulse");
      });

      $(".pulse-this").on("webkitAnimationEnd mozAnimationEnd oAnimationEnd animationEnd", function(event) {
          $(this).removeClass("animate__animated animate__pulse");
      });

  var  nb = $("#navbar");
    mnb = $("#mini-navbar");
    nbs = "navbar-scrolled";
    ssb = "sticky-sidebar";
    bsb = $("#blog-sidebar-content");
    hdr = $('header').height();
    bsbo = bsb.offset();

$(window).scroll(function() {
  if( $(this).scrollTop() > hdr ) {
    nb.addClass(nbs);
    mnb.addClass(nbs);
    $(".about-nav").insertAfter("#navbar li:nth-child(7)");
    $(".blog-nav").insertAfter("#navbar li:nth-child(2)");
  } else {
    nb.removeClass(nbs);
    mnb.removeClass(nbs);
    $(".about-nav").insertAfter("#navbar li:nth-child(2)");
    $(".blog-nav").insertAfter("#navbar li:nth-child(7)");
  }

});

$(window).scroll(function() {
  if( $(this).scrollTop() > bsbo.top ) {
    bsb.addClass(ssb + " animate__animated animate__fadeInDown");
  } else {
    bsb.removeClass(ssb + " animate__animated animate__fadeInDown");
  }

});

  $(".hamburger").on("click", function(){
    $(".menu-displayed").toggleClass("open");
    $(".hamburger").toggleClass("fa-bars fa-times");
  });

  $("a[href^='#']").click(function() {
    $("html, body").animate({ scrollTop: 0 }, 700);
    return false;
  });

  $(".scroll").click(function(e) {
    e.preventDefault();
    $("html, body").animate({scrollTop:$(this.hash).offset().top},700);
  });

});
