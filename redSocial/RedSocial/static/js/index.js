$(function () {

    var comma_separator_number_step = $.animateNumber.numberStepFactories.separator(',')



    //BEGIN TODOS LIST
    $("#todos-list-sort").sortable();
    $("#todos-list-sort").disableSelection();


    $('#todos-list-add').click(function () {
        var index = $('#todos-list-sort > li').length;
        $('ul#todos-list-sort').append('<li><input type="checkbox" id="task-item-' + index + '" /><label for="task-item-' + index + '" >' + $("#todos-list-input").val() + '</label><a class="delete" href="javascript:;" data-hover="tooltip" data-original-title="remove"><span class="fa fa-trash-o"></span></a></li>');
        $("[data-hover='tooltip']").tooltip();
    });
    $('#todos-list-sort li a.delete').live('click', function () {
        $(this).parent().remove();
    });
    //END TODOS LIST

    //BEGIN JQUERY JVECTORMAP
    $('.widget-weather').css('height', '322px');
    $('#world-map').css('width', $('.col-lg-6').width());
    $('#world-map').css('height', '342px');
    $('#world-map').vectorMap({
        map: 'world_mill_en',
        backgroundColor: 'transparent',
        series: {
            regions: [
                {
                    values: gdpData,
                    scale: ['#B8312F', '#fc6e51'],
                    normalizeFunction: 'polynomial'
                }
            ]
        },
        hoverOpacity: 0.7,
        hoverColor: false
    });
    $(window).resize(function () {
        $('#world-map').css('width', $('.col-lg-6').width());
        $('#world-map').css('height', '342px');
    });
    //END JQUERY JVECTORMAP

    //BEGIN JQUERY ANIMATE NUMBER
    $({value: 0}).animate({value: $('.tp-chart input').attr("rel")}, {
        duration: 5000,
        easing: 'swing',
        step: function () {
            $('.tp-chart input').val(Math.ceil(this.value)).trigger('change');
        }
    });
    $({value: 0}).animate({value: $('.is-chart input').attr("rel")}, {
        duration: 5000,
        easing: 'swing',
        step: function () {
            $('.is-chart input').val(Math.ceil(this.value)).trigger('change');
        }
    });
    $('#tp-number').animateNumber({
        number: 55,
        numberStep: comma_separator_number_step
    }, 5000);
    $({value: 0}).animate({value: $('.tp-chart input').attr("rel")}, {
        duration: 5000,
        easing: 'swing',
        step: function () {
            $('.tp-chart input').val(Math.ceil(this.value)).trigger('change');
        }
    })

    $(".dial").knob({
        'draw': function () {
            $(this.i).val(this.cv + '%')
        },
        'fgColor': '#B8BEC8'
    });
    $({value: 0}).animate({value: $('.stats-chart.visits-stats input').attr("rel")}, {
        duration: 5000,
        easing: 'swing',
        step: function () {
            $('.stats-chart.visits-stats input').val(Math.ceil(this.value)).trigger('change');
        }
    })
    $({value: 0}).animate({value: $('.stats-chart.pageviews-stats input').attr("rel")}, {
        duration: 5000,
        easing: 'swing',
        step: function () {
            $('.stats-chart.pageviews-stats input').val(Math.ceil(this.value)).trigger('change');
        }
    })
    $('#bg-number').animateNumber({
        number: 13287,
        numberStep: comma_separator_number_step
    }, 5000);
    $('#at-number').animateNumber({
        number: 8636,
        numberStep: comma_separator_number_step
    }, 5000);
    $('#tm-number').animateNumber({
        number: 853,
        numberStep: comma_separator_number_step
    }, 5000);
    $('#gr-number').animateNumber({
        number: 15,
        numberStep: comma_separator_number_step
    }, 5000);
    $('#is-number').animateNumber({
        number: 1305,
        numberStep: comma_separator_number_step
    }, 5000);
    $({value: 0}).animate({value: $('.is-chart input').attr("rel")}, {
        duration: 5000,
        easing: 'swing',
        step: function () {
            $('.is-chart input').val(Math.ceil(this.value)).trigger('change');
        }
    })
    $('#visits-number').animateNumber({
        number: 16107,
        numberStep: comma_separator_number_step
    }, 5000);
    $('#pageviews-number').animateNumber({
        number: 62142,
        numberStep: comma_separator_number_step
    }, 5000);


    $('#users-number').animateNumber({
        number: 15,
        numberStep: comma_separator_number_step
    }, 5000);
    $('#app-number').animateNumber({
        number: 32890,
        numberStep: comma_separator_number_step
    }, 5000);
    //END JQUERY ANIMATE NUMBER

    //BEGIN SKYCON
    var icons = new Skycons({"color": "white"});

    icons.set("clear-day", Skycons.CLEAR_DAY);
    icons.set("clear-night", Skycons.CLEAR_NIGHT);
    icons.set("partly-cloudy-day", Skycons.PARTLY_CLOUDY_DAY);
    icons.set("partly-cloudy-night", Skycons.PARTLY_CLOUDY_NIGHT);
    icons.set("cloudy", Skycons.CLOUDY);
    icons.set("rain", Skycons.RAIN);
    icons.set("sleet", Skycons.SLEET);
    icons.set("snow", Skycons.SNOW);
    icons.set("wind", Skycons.WIND);
    icons.set("fog", Skycons.FOG);

    icons.play();
    //END SKYCON










});

