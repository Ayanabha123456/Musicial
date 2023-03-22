//handling friend requests
$('.send').click(function(){
    var username = $(this).attr("value"); //get username to whom friend request is to be sent
    $.ajax(
      {
        type:"POST",
        url:"social",
        data:{
          'friending':username
        },
        success: function(data)
        {
          //display success message
          $('.disp_send').text('Request sent to '+username)
          //remove the send button
          $('.send').remove()
        }
      }
    )
  });
  //handling accept request
  $('.accept').click(function(){
    var username = $(this).attr("value"); //get username whose friend request is to be accepted
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
    var username = $(this).attr("value") //get username whose friend request is to be deleted
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