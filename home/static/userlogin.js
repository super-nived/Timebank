$(document).ready(function() {
    
    $('.login-page').click(function() {
 
        $('#signup-form').css('display', 'none');
        $('#login-form').css('display', 'flex');
        $('.signup-page').css('display','block')
        $(this).css('display','none')
    });
});


$(document).ready(function() {
    
    $('.signup-page').click(function() {
   
        $('#signup-form').css('display', 'flex');
        $('#login-form').css('display', 'none');
        $('.login-page').css('display','block')
        $(this).css('display','none')
    });
});

// $(document).ready(function() {
//     $('.login-btn').click(function() {
//         $('.login-form').css('display', 'block');
//         $('.sign-form').css('display', 'none');
        
//     });
// });