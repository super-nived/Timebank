$(document).ready(function(){
    $('#open-edit-page').click(function(){
        $('.form-box').css('display','flex')
        $('.middle').css('display','none')
    })
})





// timer

// Set the target date and time for the countdown in India's time zone
const targetDate = new Date("2028-07-01T00:00:00+05:30");

// Update the countdown every second
const countdownTimer = setInterval(updateCountdown, 1000);

function updateCountdown() {

  // Get the current date and time in India's time zone
  const currentDate = new Date().toLocaleString("en-US", { timeZone: "Asia/Kolkata" });

  // Calculate the remaining time in milliseconds
  const remainingTime = targetDate - new Date(currentDate);

  // Exit the countdown if the target date has passed
  if (remainingTime <= 0) {
    clearInterval(countdownTimer);
    console.log("Countdown has ended.");
    return;
  }

  // Calculate the remaining hours, minutes, and seconds
  const hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

  $('#hours').text(`${hours} h`);
  $('#minutes').text(`${minutes} m`);
  $('#seconds').text(`${seconds} s`);
  // Display the countdown in the console or update your webpage with the values
  console.log(`Hours: ${hours}, Minutes: ${minutes}, Seconds: ${seconds}`);
}




/////////////redeem time to money///////
$(document).ready(function () {

  // Function to calculate currency
  function calculateCurrency() {
    var time = parseInt($("#time").val());
    if (!isNaN(time)) {
      var currency = time * 700;
      $("#currency").val(currency);
    }
  }

  // Call the calculateCurrency function initially to set the default value
  calculateCurrency();

  // Set up onchange event for the time input
  $("#time").on("change", function () {
    calculateCurrency();
  });
});




$(document).ready(function(){
  $('#redeem-close-btn').click(function(){
    $('.redeem-container').css('display','none')
  });
})

$(document).ready(function(){
  $('#redeem-btn').click(function(){

    $('.redeem-container').css('display','flex')
  });
})

$(document).ready(function(){
  $('.btn-primary').click(function(){
    $('.redeem-container').css('display','none')
  });
})


