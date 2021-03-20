var toggle = false;

// Called when the user clicks on the browser action.
chrome.browserAction.onClicked.addListener(function (tab) {

  toggle = !toggle;

  if (toggle) {
    chrome.browserAction.setIcon({ path: "icon.png" });
    chrome.browserAction.setBadgeText({ text: 'ON' });
    // Send toggle on to the active tab
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      chrome.tabs.sendMessage(tabs[0].id, { action: "toggle_on" }, function (response) { });
    });
  }
  else {
    chrome.browserAction.setIcon({ path: "icon-off.png" });
    chrome.browserAction.setBadgeText({ text: '' });
    // Send toggle off to the active tab
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      chrome.tabs.sendMessage(tabs[0].id, { action: "toggle_off" }, function (response) { });
    });
  }
});


chrome.runtime.onMessage.addListener(
  function (request, sender, sendResponse) {
    //handle POST requests to server
    if (request.contentScriptQuery === "postData") {
      fetch(request.url, {
        method: 'POST',
        headers: {
          'Accept': 'application/json, application/xml, text/plain, text/html, *.*',
          'Content-Type': 'application/json'
        },
        body: request.data
      })
        .then(response => response.json())
        .then(response => sendResponse(response))
        .catch(error => console.log('Error:', error));
      return true;
    }

    //handle GET requests from server
    if (request.contentScriptQuery === "getData") {
      fetch(request.url)
        .then(response => response.json())
        .then(response => sendResponse(response[0]["shortdef"]))
        .catch(error => console.log('Error:', error));
      return true;
    }

    //handle fresh page requests
    if (request.type === "getToggle") {
      if (toggle) {
        sendResponse({result: "toggle_on"})
      } else {
        sendResponse({result: "toggle_off"})
      }
      
    } 
  }
);


