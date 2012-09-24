class Beats extends Backbone.Collection
  model: Beat
  url: '/beats'

$ ->
  window.Beats = Beats
