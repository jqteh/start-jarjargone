var bubbleDOM = document.createElement('div');
bubbleDOM.setAttribute('class', 'selection_bubble');
document.body.appendChild(bubbleDOM);

var toggle = false

// Receive instructions from background.js (extension button)
chrome.extension.onMessage.addListener(function (msg, sender, sendResponse) {

    if (msg.action == 'toggle') {

        toggle = !toggle;
        console.log(toggle)

        if (toggle) { // Turn on functionality
            // Open bubble on text selection
            document.addEventListener('mouseup', mouseUp)

            // Close the bubble when we click on the screen.
            document.addEventListener('mousedown', mouseDown);
        } else { // Turn off functionality
            document.removeEventListener('mouseup', mouseUp);
            document.removeEventListener('mousedown', mouseUp);
        }
    }

    // return true
});

function mouseUp(e) {
    var selection = window.getSelection().toString();

    if (selection.length) {
        console.log(selection);

        chrome.runtime.sendMessage(
            {
                contentScriptQuery: "postData",
                data: JSON.stringify(selection),
                url: "apiUrl"
            }, function (response) {
                debugger;
                if (response != undefined && response != "") {
                    console.log(response)
             
                    var top = e.clientY + window.scrollY;
                    var left = e.clientX + window.scrollX;
            
                    renderBubble(left, top, response);
                } else {
                    debugger;
                    console.log("problem")
                }
            }
        )
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
