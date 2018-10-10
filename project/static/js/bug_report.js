class BugReport {
    static setMessage(text, style){
        var bugReportTextArea = document.getElementById("bug_report_text_area");
        var bugReportButtonArea = document.getElementById("bug_report_button_area");
        var re_text = bugReportTextArea.innerHTML;
        bugReportTextArea.innerHTML = text;
        if (style == 'normal'){
            bugReportButtonArea.style.display = 'block';
            bugReportTextArea.className = "bug_report_text_normal";
            return
        }
        bugReportButtonArea.style.display = 'none';
        bugReportTextArea.className = "bug_report_text_thanks";
        setTimeout(() => BugReport.setMessage(re_text, 'normal'), 3000);
    }
    static getReport(event){
        var selectedText = window.getSelection().toString();
        if !(selectedText) return
        var message = window.location.href +
                      '\n\n ' +
                      selectedText +
                      '\n\n ' +
                      'Поясните дополнительно и укажите контактные данные, если хотите.';
        var user_prompt = prompt(message, "");
        if (user_prompt != null) {
            BugReport.setMessage('Благодарю Вас!');
            BugReport.sendReport(message + ':' + user_prompt, true); // honest send: message + user_prompt
            return
        }
        // force send of uncertain user unprompted message : message + user_message
        BugReport.sendReport(message, false);
    }
    static sendReport(text, honestMarker){
        // send realization
        // alert('SEND: ' + text);
    }
}
window.onload = function() {
    var button = document.getElementById("bug_report_button");
    button.onclick = BugReport.getReport;
};

