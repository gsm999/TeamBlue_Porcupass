/*let active_tab_id = 0;
chrome.tabs.onActivated.addListener(tab => {
    chrome.tabs.get(tab.tabID, current_tab_info => {
        active_tab_id = tab.tabID;

        if (/^https:\/\/www\.google/.test(current_tab_info.url)) {
            chrome.tabs.insertCSS(null, {file: './styles.css'})
            chrome.tabs.executeScript(null,{file: './foreground.js'})
        };
    });
});
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.message === 'login') {
        flip_user_status(true, request.payload)
            .then(res => sendResponse(res))
            .catch(err => console.log(err));
        return true;
    } else if (request.message === 'logout') {
        flip_user_status(false, null)
            .then(res => sendResponse(res))
            .catch(err => console.log(err));
        return true;
    } 
});*/