const header = document.querySelector("nav");

window.addEventListener ("scroll", function() {
  header.classList.toggle ("sticky", window.scrollY > 0);
});

$(".owl-carousel").owlCarousel({
  loop: true,
  margin: 10,
  nav: true,
  navText: [
    "<box-icon name='chevron-left' type='solid'></box-icon>",
    "<box-icon name='chevron-right'></box-icon>"
  ],
  autoplay: true,
  autoplayHoverPause: true,
  responsive: {
    
    0: {
      items: 1
    },
    480: {
      items: 2
    },
    767: {
      items: 3
    },
    1000: {
      items: 5
    }
  }
});
