class BugReport {
    static set_message(text){
        var bug_report_area = document.getElementById("bug_report_message");
        bug_report_area.innerHTML = text;
    }
    static get_report(event){
        if (event.altKey) {
            var selected_text = window.getSelection().toString();
            if (selected_text){
                var message = window.location.href +
                              '\n\n ' +
                              selected_text +
                              '\n\n ' +
                              'Поясните дополнительно и укажите контактные данные, если хотите.'
                var prompted = prompt(message, "");
                if (prompted != null) {
                    BugReport.set_message('Благодарю Вас!')
                    // honest send: message + user_message
                } else {
                    // force send of uncertain user unprompted message : message + user_message
                }
            }
        }

    }
}
window.onload = function() {
    document.body.onmouseup = BugReport.get_report;
};

