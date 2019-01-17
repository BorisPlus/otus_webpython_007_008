// МАГИЯ
// https://stackoverflow.com/questions/5100539/django-csrf-check-failing-with-an-ajax-post-request
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});
// конец магии

$(document).ready(function() {
    const DEBUG = true;
    DEBUG && console.log('$(document).ready');
// Определим, что должно происходить при клике на класс to_subscribe
// при включенном JavaScript (происходить будет Ajax запрос)
    $(".subscribing").click(function () {
        DEBUG && console.group('$(".subscribing").click');
        // Уникальный идентификатор кликнутого элемента
        const html_container_id = '#'+$(this).attr('id');
        DEBUG && console.log('html_container_id = ' + html_container_id);

        // Далее нам необъодимо перезагрузить картинку статуса факта обработки материала
        // Уникальный идентификатор тега статуса (IMG) составим из имеющихся данных
        // об id оработанного файла, который указан в спецатрибуте кликнутого элемента, и спецпрефикса
        const lesson_id = $(this).attr('data-lesson_id');
        DEBUG && console.log('lesson_id = ' + lesson_id);
        const lesson_name = $(this).attr('data-lesson_name');
        DEBUG && console.log('lesson_name = ' + lesson_name);
        const current_subscription = $(html_container_id).attr('data-current_subscription').toLowerCase();
        DEBUG && console.log('current_subscription = ' + current_subscription);
        $(this).attr('href', 'javascript: void(0)');
        // url_href - аттрибут будет содержать исходную ссылку
        // он нужен, для возможности осуществления повторного клика без перезагрузки страницы
        let url_href = $(this).attr('data-url_href');
        DEBUG && console.log('url_href = ' + url_href);
        if (!url_href) {
            // если он не установлен, то установим его, заменив исходный HREF на якорь
            url_href = $(this).attr('href');
            $(this).attr('data-url_href', url_href);
            $(this).attr('href', html_container_id);
        }
        DEBUG && console.log('url_href = ' + url_href);
        let allow_for_request = false;
        if (current_subscription == 'subscribed'){
            if (confirm('Вас точно не будет на уроке: '+lesson_name+' ?')) {
                allow_for_request = true;
            }
        } else {
            allow_for_request = true;
        }
        DEBUG && console.log('allow_for_request = ' + allow_for_request);
        if (allow_for_request) {
             $.ajax({
                url: url_href,
                dataType: 'json',
                success: function (data) {
                    // AJAX запрос должен вернуть строгую структуру словаря данных
                    // dict(ajax_response=..., ajax_raw_response=...)
                    DEBUG && console.log('ajax_response = ' + JSON.stringify(data));
                    if (data.ajax_response) {
                        // Устанавливаем текст ссылки
                        // $(html_container_id).html(data.ajax_response.value);
                        // Устанавливаем картинку
                        const src = data.ajax_response.value == 'was_subscribed' ?
                            '/static/img/mediator.raw.green.svg.png' :
                            '/static/img/mediator.raw.gray.svg.png';
                        const title = data.ajax_response.value == 'was_subscribed' ?
                            'Вы записаны на урок' :
                            'Вы не записаны на урок';
                        const active_subscription = data.ajax_response.value == 'was_subscribed' ?
                            'subscribed' :
                            'unsubscribed';
                        $(html_container_id).attr('src', src);
                        $(html_container_id).attr('title', title);
                        $(html_container_id).attr('data-current_subscription', active_subscription);
                    }else{
                        alert('Что-то не то с AJAX ответом');
                    }
                }
            });
        } else {
//                alert('Why did you press cancel? You should have confirmed');
        }
        DEBUG && console.groupEnd();
    });
});
