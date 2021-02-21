$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#connection-contact .modal-content").html("");
        $("#connection-contact").modal("show");
      },
      success: function (data) {
        $("#connection-contact .modal-content").html(data.html_form);
      }
    });
  };

  var sendForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#connection-contact").modal("hide");
        }
        else {
          $("#connection-contact .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // make contact
  $(".js-connection-contact").click(loadForm);
  $("#connection-contact").on("submit", ".js-book-create-form", sendForm);

});