// ==UserScript==
// @name        removeFacebookFeed
// @namespace   facebook
// @description Remove Facebook Feed 
// @include     https://www.facebook.com/*
// @version     1
// @grant       none
// ==/UserScript==

var div = document.getElementById("contentArea");
if (div) {
    // hide it
    div.style.display = "none";
    // also let's remove it
    div.parentNode.removeChild(div); 
}

// remove href attribute from page logo
var logo = document.getElementById("pageLogo");
if (logo) {
    var aRef = logo.firstChild;
    if (aRef) {
        aRef.removeAttribute("href");
    }
}
