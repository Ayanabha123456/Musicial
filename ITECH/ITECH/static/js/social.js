//handling friend requests
$('.send').click(function(){
    var username = $(this).attr("value");
    $.ajax(
      {
        type:"POST",
        url:"social",
        data:{
          'friending':username
        },
        success: function(data)
        {
          $('.disp_send').text('Request sent to '+username)
          $('.send').remove()
        }
      }
    )
  });
  //handling accept request
  $('.accept').click(function(){
    var username = $(this).attr("value");
    $.ajax(
      {
        type:"POST",
        url:"social",
        data:{
          'accept':username
        },
        success: function(data)
        {
          //update current friend list
          $('.list_of_friends').append('<li class="list-group-item">'+username+'</li>')
          //remove pending friend request
          $('#pending'+username).remove()
        }
      }
    )
  })
  //handling delete request
  $('.reject').click(function(){
    var username = $(this).attr("value")
    $.ajax(
      {
        type:"POST",
        url:"social",
        data:{
          'reject':username
        },
        success: function(data)
        {
          //remove pending friend request
          $('#pending'+username).remove()
        }
      }
    )
  })