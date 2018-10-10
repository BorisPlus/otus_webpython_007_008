class BugReport {
    static setMessage(text){
        var bugReportMessageArea = document.getElementById("bug_report_message_area");
        bugReportMessageArea.innerHTML = text;
    }
    static getReport(event){
        var selectedText = window.getSelection().toString();
        if (selectedText){
            var message = window.location.href +
                          '\n\n ' +
                          selectedText +
                          '\n\n ' +
                          'Поясните дополнительно и укажите контактные данные, если хотите.'
            var prompted = prompt(message, "");
            if (prompted != null) {
                BugReport.setMessage('Благодарю Вас!')
                // honest send: message + user_message
                BugReport.sendReport(message + user_message, true)
            } else {
                // force send of uncertain user unprompted message : message + user_message
                BugReport.sendReport(message + user_message, false)
            }
        }

    }
    static sendReport(text, honestMarker){
        // send realization
        // alert(text)
    }

}
window.onload = function() {
    var button = document.getElementById("bug_report_button");
    button.onclick = BugReport.getReport;
};

