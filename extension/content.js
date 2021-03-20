var bubbleDOM = document.createElement('div');
bubbleDOM.setAttribute('class', 'selection_bubble');
document.body.appendChild(bubbleDOM);

if(document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded',afterDOMLoaded);
} else {
    afterDOMLoaded();
}

function afterDOMLoaded(){
    //Everything that needs to happen after the DOM has initially loaded.
    console.log('loaded')
    chrome.runtime.sendMessage({
        type:"getToggle"
    }, function(response){
        console.log("The current toggle_on is:" + response.result);
        if (response.result === "toggle_on") {
            document.addEventListener('mouseup', mouseUp);
            document.addEventListener('mousedown', mouseDown);
        } else if (response.result === "toggle_off") {
            console.log("default: toggle-off")
        }
    })
}


// Receive instructions from background.js (extension button)
chrome.extension.onMessage.addListener(function (msg, sender, sendResponse) {

    if (msg.action == 'toggle_on') {  // Turn on functionality

        console.log(msg.action)

            // Open bubble on text selection
            document.addEventListener('mouseup', mouseUp);

            // Close the bubble when we click on the screen.
            document.addEventListener('mousedown', mouseDown);
        
    } else if (msg.action == 'toggle_off') { // Turn off functionality
        console.log(msg.action)

        document.removeEventListener('mouseup', mouseUp);
        document.removeEventListener('mousedown', mouseUp);
    }

    // return true
});

function mouseUp(e) {
    var selection = window.getSelection().toString();

    if (selection.length) {
        console.log(selection);
        var top = e.clientY + window.scrollY;
        var left = e.clientX + window.scrollX;
        renderBubble(left, top, selection);

        //Post to server
        // chrome.runtime.sendMessage(
        //     {
        //         contentScriptQuery: "postData",
        //         data: JSON.stringify(selection),
        //         url: "apiUrl"
        //     }, function (response) {
        //         debugger;
        //         if (response != undefined && response != "") {
        //             console.log(response)

        //             var top = e.clientY + window.scrollY;
        //             var left = e.clientX + window.scrollX;

        //             renderBubble(left, top, response);
        //         } else {
        //             debugger;
        //             console.log("problem")
        //         }
        //     }
        // )

        // Test API merriam webster medical dictionary
        // chrome.runtime.sendMessage(
        //     {
        //         contentScriptQuery: "getData",
        //         data: JSON.stringify(selection),
        //         url: `https://www.dictionaryapi.com/api/v3/references/medical/json/${selection}?key=hidden`
        //     }, function (response) {
        //         if (response != undefined && response != "") {
        //             console.log(response)

        //             var top = e.clientY + window.scrollY;
        //             var left = e.clientX + window.scrollX;

        //             renderBubble(left, top, response);
        //         } else {
        //             debugger;
        //             console.log("problem")
        //         }
        //     }
        // )

    }
}

function mouseDown(e) {
    bubbleDOM.style.visibility = 'hidden';
}


// Move that bubble to the appropriate location.
function renderBubble(mouseX, mouseY, selection) {

    bubbleDOM.innerHTML = `<h3>Definition</h3><p>${selection}</p>`;
    bubbleDOM.style.top = mouseY + 'px';
    bubbleDOM.style.left = mouseX + 'px';
    bubbleDOM.style.visibility = 'visible';
}
