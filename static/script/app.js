const header = document.querySelector("nav");

window.addEventListener ("scroll", function() {
  header.classList.toggle ("sticky", window.scrollY > 0);
});

$(".owl-carousel").owlCarousel({
  loop: true,
  margin: 10,
  nav: true,
  navText: [
    "<i class='fa-solid fa-chevron-left'></i>",
    "<i class='fa-solid fa-chevron-right'></i>" 
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
