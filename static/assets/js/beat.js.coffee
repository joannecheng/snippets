class Beat extends Backbone.Model

class BeatView extends Backbone.View
  className: 'beat'
  initialize: ->
    _.bindAll @, 'render'
    @model.bind('change', @render)
    @template = _.template($('#beat_template').html())

  render: ->
    renderedContent = @template(@model.toJSON())
    $(@el).html(renderedContent)
    @


$ ->
  window.Beat = Beat
  window.BeatView = BeatView
