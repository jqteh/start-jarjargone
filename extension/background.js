// const CONTEXT_MENU_ID = "MY_CONTEXT_MENU";
// function getword(info,tab) {
//   if (info.menuItemId !== CONTEXT_MENU_ID) {
//     return;
//   }
//   console.log("Word " + info.selectionText + " was clicked.");
//   chrome.tabs.create({  
//     url: "http://www.google.com/search?q=" + info.selectionText
//   });
// }
// chrome.contextMenus.create({
//   title: "Search: %s", 
//   contexts:["selection"], 
//   id: CONTEXT_MENU_ID
// });
// chrome.contextMenus.onClicked.addListener(getword)