var timee_ = 0
// Dropdown
function dropFunction(id) {
  console.log(id)
  var x = document.getElementById(id);
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
} else {
    x.className = x.className.replace(" w3-show", "");
}
}

// Filter
function filterFunction() {
  var input, filter, ul, li, a, i, div;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDIV");
  a = div.getElementsByTagName("div");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
  } else {
      a[i].style.display = "none";
  }
}
}

// Accordions 
function myFunction(id) {
      var x = document.getElementById(id);
      if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else { 
        x.className = x.className.replace(" w3-show", "");
    }
}

function make_images() {
  $.ajax({
    type: 'POST',
    url: "/get_len",
    success: function(response){ 
      var json = jQuery.parseJSON(response)
        timer = json.len*2*1000;
        window.time_ = Math.round(timer/1000);

        var g = document.getElementById("Start");
        g.disabled = true;  

        function new_time(){
          $('#timer').html("Осталось " + window.time_ + " сек");
          window.time_ -= 1;
          console.log(window.time_);
        }

        var x = document.getElementById("wait");
        x.className = "w3-container w3-center";
        var timerId = setInterval(new_time, 1000);
        setTimeout(function() {
          clearInterval(timerId);
          var y = document.getElementById("timer");
          y.className = "w3-hide";
          g.className = "w3-hide";
        }, timer);

        start_make_images()
    },
    error: function(error){ 
      console.log(error);
    }
  });

  function start_make_images(){
      $.ajax({
        type: 'POST',
        url: "/iter",
        data: {"iter":1},
        success: function(response){ 
          var y = document.getElementById("OKbut");
          y.className -= "w3-hide";
          var z = document.getElementById("timer_block");
          z.className = "w3-hide";
        },
        error: function(error){ 
          console.log(error);
        }
      })
  };


};