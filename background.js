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
/*chrome.commands.onCommand.addListener((command) => {

    if (command === '_execute_browser_action')
        chrome.system.display.getInfo({ singleUnified: true }, (info) => {
        
          const wDimension = info[0].workArea;
          const { top, left, height, width } = wDimension;
          console.log(top);
          const w = 440;
          const h = 220;
          const l = width / 2 - w / 2 + left;
          const t = height / 2 - h / 2 + top;
          const newWindow = () => {
            console.log('in new window function');
          };
          chrome.windows.create(
            {
              url: 'change-password.html',
              type: 'popup',
              width: w,
              height: h,
              left: Math.round(l),
              top: Math.round(t),
            },
            newWindow
          );
        });
});*/
chrome.alarms.create('testAlarm', {
	periodInMinutes: 1,
    when: Date.now()
});

chrome.alarms.onAlarm.addListener((alarm) => {
    if (alarm.name === "testAlarm") {
        chrome.notifications.create('test', {
            type: 'basic',
            iconUrl: '/pics/icon128.png',
            title: 'Password Alert',
            message: 'Its time to update your passwords!',
            priority: 1
        });
    }
});