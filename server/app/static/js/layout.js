require(['/static/config.js'], function () {
  require(['jquery', 'semantic'], function ($, Semantic) {
    $('.ui.dropdown').dropdown();

    $('.ui.modal').modal({
        blurring: true
    }).modal('show');

    $('.special.cards .image').dimmer({
      on: 'hover'
    });
    var ua = window.navigator.userAgent;
    var msie = ua.indexOf("MSIE ");

    if (msie > 0 || !!navigator.userAgent.match(/Trident.*rv\:11\./)) {
      console.log("MS IE Detected :(");
    }
    else {
      $('#content').addClass('sticky-content');
      $('#body').addClass('sticky-body');
    }
  });
});
