message_of_start = 'А теперь выделите то, что Вы считаете ошибкой. '
start = function(){
    if (document.body.style.cursor == "pointer") {

        document.body.style.cursor = "default";
    } else {
        document.body.style.cursor = "pointer";
        alert(message_of_start);
    }
}
get = function(){
    if (document.body.style.cursor == "pointer") {
        selected_text = window.getSelection().toString();
        if (selected_text){
            debug_message = window.location.href + '\n\n ' +  selected_text
            debug_message += '\n\n Поясните дополнительно и укажите контактные данные, если хотите.'
            var prompted = prompt(debug_message, "");
            if (prompted !== null) {

                // здесь должно быть то, что отправит данные на сервер


                document.body.style.cursor = "default";
                alert('Благодарю Вас!');
            }

        }
    }
}
function load_bug_report_stuff() {
    document.body.onmouseup = get;
}