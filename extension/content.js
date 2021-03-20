var bubbleDOM = document.createElement('div');
bubbleDOM.setAttribute('class', 'selection_bubble');
document.body.appendChild(bubbleDOM);

document.addEventListener('mouseup', function (e) {
    var selection = window.getSelection().toString();

    if (selection.length) {
        console.log(selection);

        var top = e.clientY + window.scrollY;
        var left = e.clientX + window.scrollX;

        renderBubble(left, top, selection);
    }

}, false)

// Close the bubble when we click on the screen.
document.addEventListener('mousedown', function (e) {
    bubbleDOM.style.visibility = 'hidden';
}, false);



// Move that bubble to the appropriate location.
function renderBubble(mouseX, mouseY, selection) {

    // var viewportOffset = bubbleDOM.getBoundingClientRect();
    // // these are relative to the viewport, i.e. the window
    // var top = viewportOffset.top;
    // var left = viewportOffset.left;

    bubbleDOM.innerHTML = `<h3>Definition</h3><p>${selection}</p>`;
    bubbleDOM.style.top = mouseY + 'px';
    bubbleDOM.style.left = mouseX + 'px';
    bubbleDOM.style.visibility = 'visible';
}
