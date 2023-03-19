//handling likes
$('.likes').click(function(){
    var pic_id = $(this).attr("value");
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
          $('#likes'+pic_id).text(data['likes'])
        }
      }
    )
  });
  //handling comments
  $('.comments').click(function(){
    var pic_id = $(this).attr("value")
    var comment_text = $('.comment-text'+pic_id).val()
    $('.comment-text'+pic_id).val('')
    console.log(comment_text)
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
          $('#comments'+pic_id).text(data['comments'])
        }
      }
    )
  })