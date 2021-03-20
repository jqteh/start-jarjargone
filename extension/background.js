var toggle = false;

// Called when the user clicks on the browser action.
chrome.browserAction.onClicked.addListener(function (tab) {

  toggle = !toggle;
  
  if (toggle) {
    chrome.browserAction.setIcon({ path: "icon.png" });
    chrome.browserAction.setBadgeText({ text: 'ON' });
  }
  else {
    chrome.browserAction.setIcon({ path: "icon-off.png" });
    chrome.browserAction.setBadgeText({ text: '' });
    // chrome.tabs.executeScript(tab.id, { code: "alert()" });
  }

  // Send a message to the active tab
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    chrome.tabs.sendMessage(tabs[0].id, { action: "toggle" }, function (response) { });
  });
});


chrome.runtime.onMessage.addListener(
  function (request, sender, sendResponse) {
    if (request.message === "open_new_tab") {
      chrome.tabs.create({ "url": request.url });
    }
  }
);


