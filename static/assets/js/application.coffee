class DragDrop
  constructor: ->
    @dropHandlers()

  dropHandlers: =>
    $(document).bind 'drop dragover', (e) -> 
      e.preventDefault()
    $('#drop_area').on('dragenter', @dragenterListener)
    $('#drop_area').on('dragleave', @dragleaveListener)

    $('#fileupload').fileupload(
      dataType: 'mp3,wav',
      drop: (e, data) =>
        for file in data.files
          $('body').append( $('<p/>').text(file.name))
        @dragleaveListener(e)
    )

  dragenterListener: (e) =>
    $('#drop_area').css('opacity', '0.8')

  dragleaveListener: (e) =>
    $('#drop_area').css('opacity', '1')


window.DragDrop = new DragDrop
