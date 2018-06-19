$('.alert').alert()

$('.collapse').collapse()

$('#collapseExample').collapse({
  toggle: true
})

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})