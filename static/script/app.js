const header = document.querySelector("nav");

window.addEventListener("scroll", function () {
  header.classList.toggle("sticky", window.scrollY > 0);
});



$(".related-product-carousel").owlCarousel({
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
      items: 4
    },
    480: {
      items: 4
    },
    767: {
      items: 4
    },
    1000: {
      items: 5
    }
  }
});
$(".home-product").owlCarousel({
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
      items: 4
    },
    480: {
      items: 4
    },
    767: {
      items: 4
    },
    1000: {
      items: 5
    }
  }
});
$(".popular-product-carousel").owlCarousel({
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
      items: 2
    },
    480: {
      items: 2
    },
    767: {
      items: 4
    },
    1000: {
      items: 5
    }
  }
});

$(".bf-carousel").owlCarousel({
  loop: true,
  margin: 10,
  nav: true,
  navText: [
    "<i class='fa-solid fa-arrow-left'></i>",
    "<i class='fa-solid fa-arrow-right'></i>",
  ],
  autoplay: true,
  autoplayHoverPause: true,
  responsive: {
    0: {
      items: 1
    },
    480: {
      items: 1
    },
    767: {
      items: 1
    },
    1000: {
      items: 1
    }
  }
});
$(".floating-carousel").owlCarousel({
  loop: true,
  margin: 10,
  nav: true,
  navText: [
    "<i class='fa-solid fa-chevron-left'></i>",
    "<i class='fa-solid fa-chevron-right'></i>",
  ],
  autoplay: true,
  autoplayHoverPause: true,
  responsive: {
    0: {
      items: 1
    },
    480: {
      items: 1
    },
    767: {
      items: 2
    },
    1000: {
      items: 5
    }
  }
});
$(".category-carousel").owlCarousel({
  loop: true,
  margin: 10,
  nav: true,
  navText: [
    "<i class='fa-solid fa-chevron-left'></i>",
    "<i class='fa-solid fa-chevron-right'></i>",
  ],
  autoplay: true,
  autoplayHoverPause: true,
  responsive: {
    0: {
      items: 1
    },
    480: {
      items: 1
    },
    767: {
      items: 2
    },
    1000: {
      items: 5
    }
  }
});

$(document).ready(function () {
  $('.tab-menu li:first-child').addClass('active');
  $('.tab-content .tab-pane:first-child').addClass('active');

  $('.tab-menu li').click(function () {
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
  var productAmount = "#cart-price-" + cartId
  var subTotal = $(".subtotal")
  
  $.ajax({
    url: 'https://zade.vercel.app/cart/addcart/' + cartId,
    type: 'GET',
    success: function (response) {
      var quantity = response.cart;
      var price = response.product.price;
      var subtotal = response.subtotal
      $(testDivId).html(`<li>${quantity}</li>`);
      var amount = quantity * price;
      $(productAmount).html(`$${amount}`);
      $(subTotal).html(`$${subtotal}`);
    }
  })
});

var minusId = "[id^='minus_']";
$(minusId).click(function () {
  var cartId = $(this).data("cart-id");
  var testDivId = "#testdiv_" + cartId;
  var productAmount = "#cart-price-" + cartId
  var subTotal = $(".subtotal")
  $.ajax({
    url: 'https://zade.vercel.app/cart/minuscart/' + cartId,
    type: 'GET',
    success: function (response) {
      var quantity = response.cart;
      var price = response.product.price;
      var subtotal = response.subtotal
      $(testDivId).html(`<li>${quantity}</li>`);
      var amount = quantity * price;
      $(productAmount).html(`$${amount}`);
      $(subTotal).html(`$${subtotal}`);
    }
  })
});

$(".cart-delete-button").click(function () {
  var cartId = $(this).closest('tr').data("z-cart-id");
  console.log(cartId)
});


const passwordInput = $("#login-password");
const showHideButton = $("#show-hide-password");

showHideButton.on("click", function() {
  if (passwordInput.attr("type") === "password") {
    passwordInput.attr("type", "text");
    showHideButton.html("<i class='fa-regular fa-eye'></i>");
  } else {
    passwordInput.attr("type", "password");
    showHideButton.html("<i class='fa-regular fa-eye-slash'></i>");
  }
});

$('#searchbar').on('input', function() {
  var query = $(this).val();

  var test1DivId = "#search-results"
  if (query != '') {
    $.ajax({
      url: 'https://zade.vercel.app/product/searchproducts/',
      data: { 'query': query },
      success: function (data) {
        if (data.products.length > 0) {
          var productsHtml = data.products.map(function(p) {
            return `
            <a href="http://zade.vercel.app/product/product-details/${p.id}">
              <div class="z--search-result" data-aos="fade-up" data-aos-duration="200">
                  <img class="z-ajax-search-image" src="${p.image}">
                  <div>${p.title} - ${p.price}</div>
                </div>
            </a>
            `;
          }).join('');
        $(test1DivId).html(productsHtml);
          
          
        }
        else {
          $("#search-results").html('<div class="nothing-found-ajax">No Product Found</div>');
        }
        
      }
    });
  }
  else {
    $("#search-results").html('<div class="discover-product-ajax">Discover</div>')
    $(".z--search-result").addClass("d-none")
  }
  
});

