//handling likes
$('.likes').click(function(){
    var pic_id = $(this).attr("value"); //getting the id of the picture whose like button has been pressed
    console.log(pic_id)
    $.ajax(
      {
        type:"POST",
        url:"landing",
        data:{
          'picture_id':pic_id,
          'type':'like'
        },
        success: function(data)
        {
          $('#likes'+pic_id).text(data['likes']) //displaying the no. of likes beside the like button
        }
      }
    )
  });
  //handling comments
  $('.comments').click(function(){
    var pic_id = $(this).attr("value") //getting the id of the picture whose comment button has been pressed
    var comment_text = $('.comment-text'+pic_id).val() //getting the actual comment
    $('.comment-text'+pic_id).val('') //emptying the comment box
    $.ajax(
      {
        type:"POST",
        url:"landing",
        data:{
          'picture_id':pic_id,
          'type':'comment',
          'comment':comment_text
        },
        success: function(data)
        {
          //displaying the new comment
          data['comments'].forEach(function(comment){
            var li = $("<li class='list-group-item'>")
            li.text(comment)
            $('#comments'+pic_id).append(li)
          })
        }
      }
    )
  })