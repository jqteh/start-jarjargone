document.addEventListener('mouseup', function (event) {
    var sel = window.getSelection().toString();

    if (sel.length) {

        console.log(sel)
        
        // function logText(info, tab) {
        // console.log(info.selectionText);
        // chrome.tabs.create({
        //     url: "http://www.google.com/search?q=" + info.selectionText
        // });
        // }
        // chrome.contextMenus.create({
        //     title: "Console log this",
        //     contexts: ["selection"],
        //     onclick: logText
        // });
    }

})