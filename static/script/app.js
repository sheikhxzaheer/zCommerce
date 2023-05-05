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

$(document).ready(function() {
  $('.tab-menu li:first-child').addClass('active');
  $('.tab-content .tab-pane:first-child').addClass('active');
  
  // $('.tab-menu li').removeAttr('href');
  
  $('.tab-menu li').click(function() {
    var tab_id = $(this).index();
    
    $('.tab-menu li').removeClass('active');
    $('.tab-content .tab-pane').removeClass('active');
    
    $(this).addClass('active');
    $('.tab-content .tab-pane').eq(tab_id).addClass('active');
  });
});

var addId = "[id^='add_']";
$(addId).click(function () {
  var cartId = $(this).data("cart-id");
  var testDivId = "#testdiv_" + cartId;
  $.ajax({
      url: 'http://127.0.0.1:8000/cart/addcart/' + cartId,
      type: 'GET',
      success: function (response) {
        $(testDivId).html(`<li>${response.cart}</li>`);
      }
     })
});

var minusId = "[id^='minus_']";
$(minusId).click(function () {
  var cartId = $(this).data("cart-id");
  var testDivId = "#testdiv_" + cartId;
  $.ajax({
      url: 'http://127.0.0.1:8000/cart/minuscart/' + cartId,
      type: 'GET',
      success: function (response) {
        $(testDivId).html(`<li>${response.cart}</li>`);
      }
     })
});

