//handling song addition to playlist
$('.add-song').click(function(){
  //getting song details whose add button has been clicked
    var song_id = $(this).attr("value");
    var song_name = $('#song_name'+song_id).text();
    var artist = $('#song_artist'+song_id).text();
    var image = $('#song_image'+song_id).attr('src');
    var music_url = $('#song_url'+song_id).attr('src');
    var playlist = $('#playlist'+song_id).val();
    if (playlist == null) //if user has no playlist, website will prompt to create one
    {
      window.alert('Create or select a playlist first!!')
    }
    else
    {
      $.ajax(
          {
          type:"PUT",
          url:"songs",
          data:JSON.stringify({
              'song':{'playlist':playlist,'songid':song_id,'name':song_name,'artist':artist,'music_url':music_url,'image_url':image}
          }),
          success: function(data)
          {
              window.alert('Song added to playlist!!') //website will prompt once song is added to playlist
          }
      }
      )
    }
    
  });