class DragDrop
  constructor: ->
    @dropHandlers()

  dropHandlers: =>
    $(document).bind 'drop dragover', (e) -> 
      e.preventDefault()
    $('body').on('dragenter', @dragenterListener)
    $('body').on('dragleave', @dragleaveListener)

    $('#fileupload').fileupload(
      dataType: 'mp3,wav',
      drop: (e, data) =>
        for file in data.files
          $('body').append( $('<p/>').text(file.name))
        @dragleaveListener(e)
    )

  dragenterListener: (e) =>
    $('body').css('background-color', 'red')

  dragleaveListener: (e) =>
    $('body').css('background-color', 'white')


window.DragDrop = new DragDrop
window.context = new webkitAudioContext()
