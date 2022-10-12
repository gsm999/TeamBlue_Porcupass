const Cbutton = document.querySelector('.confirmBtn')
const Obutton = document.querySelector('.optionsBtn')

//const form   = document.querySelector('.form')

Cbutton.addEventListener('click', function() {
   window.close()
});
Obutton.addEventListener("click", function() {
   chrome.runtime.openOptionsPage()
});
