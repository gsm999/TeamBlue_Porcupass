chrome.tabs.getSelected(null, function (tab) {
    var inputs = document.getElementByTagName('input');
    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].getAttribute('type') == 'password') {
            alert("Open extension");
            break;
        }
    }
});