//side bar//
const menuItems = document.querySelectorAll('.menu-item');
//messages//
const messageNotification = document.querySelector('#message-notifications');

const messages = document.querySelector('.messages');
const message = messages.querySelectorAll('.message');
const messageSearch = document.querySelector('#message-search');
const theme = document.querySelector('#theme')
const themeModel = document.querySelector('.custumise-theme')
const fontsize = document.querySelectorAll('.choose-size span')
var root = document.querySelector(':root');
const fiterBOx = document.querySelector('.right')
//remove active class
const changeactiveItems = () => {
    menuItems.forEach(item => {
        item.classList.remove('active')
    })
}
menuItems.forEach(item => {
    item.addEventListener('click', () => {
        changeactiveItems()
        // item.classList.add('active');
        if (item.id != 'notifications') {
            document.querySelector('#noti').style.display = 'none'
        }
        else {
            document.querySelector('#noti').style.display = 'block'
            document.querySelector('#notifications .notification-count').style.display = 'none'

        }

    })

})

///////////////message///////////////////////

//message search//////////
const searchMessages = () => {
    const val = messageSearch.value.toLowerCase();

    message.forEach(chat => {
        let name = chat.querySelector('h5').textContent.toLowerCase();
        if (name.indexOf(val) != -1) {
            chat.style.display = 'flex'
        }
        else {
            chat.style.display = 'none'
        }

        console.log('yes')
    })

}
messageSearch.addEventListener('keyup', searchMessages)
////////////////////////

messageNotification.addEventListener('click', () => {
    console.log('lkskjldf')
    fiterBOx.style.display = 'block'
    messages.style.boxShadow = '0 0 1rem green'
    setTimeout(() => { messages.style.boxShadow = "none" }, 1000)

})




///////////////the custimisation//////

const openThemeModel = () => {
    themeModel.style.display = 'grid'
}

const closeThemeModel = (e) => {
    if (e.target.classList.contains('custumise-theme')) {
        themeModel.style.display = 'none'
    }
}

themeModel.addEventListener('click', closeThemeModel)
theme.addEventListener('click', openThemeModel)

const removeFontActive = () => {
    fontsize.forEach(change => {
        change.classList.remove('active')
    })
}

/////////set font size //////



fontsize.forEach(size => {
    let fonts

    size.addEventListener('click', () => {
        removeFontActive()
        size.classList.add('active')
        if (size.classList.contains('font-size-1')) {
            fonts = '10px'
            console.log(fonts)
            root.style.setProperty('--sticky-top-left', '5.4rem')
            root.style.setProperty('--sticky-top-right', '5.4rem')
        }
        else if (size.classList.contains('font-size-2')) {
            fonts = '13px'
            root.style.setProperty('--sticky-top-left', '5.4rem')
            root.style.setProperty('--sticky-top-right', '-7rem')
        }
        else if (size.classList.contains('font-size-3')) {
            fonts = '16px'
            root.style.setProperty('--sticky-top-left', '5.4rem')
            root.style.setProperty('--sticky-top-right', '-17rem')
        }
        else if (size.classList.contains('font-size-4')) {
            fonts = '19px'
            root.style.setProperty('--sticky-top-left', '5.4rem')
            root.style.setProperty('--sticky-top-right', '-25rem')
        }
        else if (size.classList.contains('font-size-5')) {
            fonts = '22px'
            root.style.setProperty('--sticky-top-left', '5.4rem')
            root.style.setProperty('--sticky-top-right', '-35rem')
        }
        document.querySelector('html').style.fontSize = fonts
    })

})




///////////category bottom-border//////

const h6Elements = document.querySelectorAll('.category h6');
const hideActive = document.querySelector('#nation')
h6Elements.forEach(h6 => {

    h6.addEventListener('click', () => {
        hideActive.classList.remove('active')
        h6.style.borderBottom = "4px solid black"; // Apply border to the clicked h6 element

        // Remove border from other h6 elements
        h6Elements.forEach(element => {
            if (element !== h6) {
                element.style.borderBottom = ""; // Remove existing border
            }
        });
    });
});

///////////////////nav-item-toggle////////////

// const nav = document.querySelector('.nav-icon')
// const left = document.querySelector('.left')
// const MenuItem = document.querySelectorAll('.menu-item')

// MenuItem.forEach(item => {
//     item.addEventListener('click', () => {
//         left.style.bottom = "-100%"
//     })
// })

// function togglePosition(element) {
   
//     if (left.style.bottom === "4rem") {
//         left.style.bottom = "-100%";
//     } else {
//         left.style.bottom = "4rem";
//     }
// }



//////////////////fiter box show small divice///////////////


const RihtClose = (e) => {
    if (e.target.classList.contains('right')) {
        fiterBOx.style.display = 'none'
    }
}

fiterBOx.addEventListener('click', RihtClose)

/////////////////filtering data using ajax////////////////////////
$(document).ready(function () {

    $('#nation,#district,#state').click(function () {
        action = $(this).attr('id')
        console.log(action)

        $.ajax({
            url: '/ajax/',
            data: { action: action },
            beforeSend: function() {
                $('.loading').css('display', 'flex'); 
        
              },
            success: function (response) {
                $('.loading').css('display', 'none'); 
                $("#filter-container").html(response.data);
                console.log(response.data[0])

            },
            error: function (xhr, errmsg, err) {

                console.log(xhr.status + ': ' + xhr.responseText);
            }
        });
    });
});

//////fitering base on each category///////////


$(document).ready(function () {
    console.log('get ready to boom')
    var selected = null
    $('#filter-container').on('click', '.message', function () {

        if (selected != null) {
            $('.message').css("background-color", "");
        }

        $(this).css("background-color", "rgba(226, 225, 225, 0.615)");
        selected = $(this);
         

        id = $(this).attr('id')

        category = $(this).attr('category')
        $.ajax({
            url: '/productfilter/',
            data: {
                id,
                category
            },
            beforeSend: function() {
                $('.loading').css('display', 'flex'); 
        
              },
            success: function (response) {
                $('.loading').css('display', 'none'); 
                $("#postfeeds").html(response.data);
                console.log(response, 'fgfgfgfg')
               
                var windowWidth = $(window).width();
  
                if (windowWidth <= 992) {
                    $(".right").hide();
                  // Execute code for screens with a maximum width of 768px
                  // For example:
                  console.log("Screen size is smaller than or equal to 768px");
                }
                else{
                    $(this).hide;
                }
            },
            error: function (xhr, errmsg, err) {

                console.log(xhr.status + ': ' + xhr.responseText);
            }
        })

    });
});


///////////////filter data using serchbar ////////////


///////////////searching//////////


$(document).ready(function() {
    $('#search , #creat-post').on('change', function() {
      var value = $(this).val();
      var button = $(this)
      console.log(value); // You can perform any action with the value here
      $.ajax({
        url: '/searchproduct/',
        data: {
            value
        },
        beforeSend: function() {
            $('.loading').css('display', 'flex'); 
    
          },
        success: function (response) {
            $('.loading').css('display', 'none'); 
            $("#postfeeds").html(response.data);
            console.log(response, 'fgfgfgfg')
           

        },
        error: function (xhr, errmsg, err) {

            console.log(xhr.status + ': ' + xhr.responseText);
        }
    })


    });
  });
  


//////////////////////add to cart ////////////
 
$(document).ready(function(){
   
    $('#postfeeds').on('click','.bookmark',function(){
        var id = $(this).attr('value');
        var bookmarkElement = $(this); 
        $.ajax({
            url:'/addtocart/',
            data:{id},
            success:function(){
                console.log('done we did it')
                bookmarkElement.css("color", "hsl(252,15%,60%)");
            }
        })

      
     })
})


///bookings

$(document).ready(function(){
   
    $('#postfeeds').on('click','.applay-btn',function(){
        var id = $(this).attr('value');
        var bookmarkElement = $(this); 
        alert(id)
        $.ajax({
            url:'/book/',
            data:{id},
            success:function(){
                console.log('done we did it')
                bookmarkElement.css("background-color", "hsl(252, 15%, 60%)");
            }
        })

      
     })
})


//slider
jQuery(document).ready(function ($) {
  
    $('#checkbox').change(function(){
      setInterval(function () {
          moveRight();
      }, 3000);
    });
    
      var slideCount = $('#slider ul li').length;
      var slideWidth = $('#slider ul li').width();
      var slideHeight = $('#slider ul li').height();
      var sliderUlWidth = slideCount * slideWidth;
      
      $('#slider').css({ width: slideWidth, height: slideHeight });
      
      $('#slider ul').css({ width: sliderUlWidth, marginLeft: - slideWidth });
      
      $('#slider ul li:last-child').prependTo('#slider ul');
  
      function moveLeft() {
          $('#slider ul').animate({
              left: + slideWidth
          }, 200, function () {
              $('#slider ul li:last-child').prependTo('#slider ul');
              $('#slider ul').css('left', '');
          });
      };
  
      function moveRight() {
          $('#slider ul').animate({
              left: - slideWidth
          }, 200, function () {
              $('#slider ul li:first-child').appendTo('#slider ul');
              $('#slider ul').css('left', '');
          });
      };
  
      $('a.control_prev').click(function () {
          moveLeft();
      });
  
      $('a.control_next').click(function () {
          moveRight();
      });
  
  });    
  
//slider



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





