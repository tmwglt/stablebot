setInterval(function() {
  // Send an AJAX request to the server
  $.ajax({
    url: '/',
    success: function(data) {
      // Update the page with the new data
      $('#balance').html(data);
    }
  });
}, 1000); // Refresh every 1000 milliseconds (1 second)
