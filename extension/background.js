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
    //handle POST requests to server
    if (request.contentScriptQuery === "postData") {
      fetch(request.url, {
        method: 'POST',
        headers: {
          'Accept': 'application/json, application/xml, text/plain, text/html, *.*',
          'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
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
  }
);


