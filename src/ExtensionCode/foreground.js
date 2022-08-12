/*console.log('from foreground')

const first = document.createElement('button');
first.innerText = "set data";
first.id = "first";
const second = document.createElement('button');
second.innerText = "reach backend";
second.id = "first";

document.querySelector('body').appendChild(first);
document.querySelector('body').appendChild(second);

first.addEventListener('click', () => {
    chrome.storage.local.set({"password": "123"});
    console.log('data set');
});
second.addEventListener('click', () => {
    chrome.runtime.sendMessage({message: 'storage check'});
    console.log('storage check sent');
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse)=> {
    console.log(request.message)
});*/