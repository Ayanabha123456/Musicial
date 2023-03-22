//handling Playlist display
$('.playlist').click(function(){
    var playlist = $(this).attr('value') //getting playlist which has been selected from dropdown
    $.ajax(
      {
        type:'POST',
        url:'playlist',
        data:{
          'disp_playlist':playlist
        },
        success: function(data)
        {
          //removing currently displayed playlist
          $('#songs-list').children().remove();
          //adding each song to a list to be displayed for currently selected playlist
          data['songs'].forEach(function(song) {
            var outer_div = $("<div class='row' style='display:flex;justify-self: space-between;overflow:auto'>")
            
            var div1 = $("<div class='col-sm-4'>")
            var img = $("<img width='70px;'>")
            img.attr('src',song.image_url)
            div1.append(img)

            var div2 = $("<div class='col-sm-4'>")
            var h5 = $("<h5>").text(song.name)
            var p = $("<p>").text(song.artist)
            div2.append(h5)
            div2.append(p)

            var div3 = $("<div class='col-sm-4'>")
            var source = $("<source type='audio/mpeg'>")
            source.attr('src',song.music_url)
            var audio = $("<audio controls>")
            audio.append(source)
            div3.append(audio)

            outer_div.append(div1)
            outer_div.append(div2)
            outer_div.append(div3)
            var li = $("<li class='list-group-item'>")
            li.append(outer_div)
            
            $("#songs-list").append(li);
          })
        }
      }
    )
  });