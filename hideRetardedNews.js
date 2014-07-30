// ==UserScript==
// @name        hideRetardedNews
// @namespace   googleNews
// @description Allow to remove elements from news
// @include     https://news.google.co.in/news*
// @version     1
// @grant       none
// ==/UserScript==

var className = 'esc-lead-article-title-wrapper';
var elements = document.getElementsByClassName(className);
console.log(elements[0]);
console.log("hello world why don't you work");
var hideDiv = document.createElement('h2');
var hideDivClassName = 'esc-lead-article-title';
// hideDiv.setAttribute('class', hideDivClassName);
var hideElement = document.createElement('a');

hideElement.class = "MyClassName";
var text = document.createTextNode("HIDE NEWS");

elements[0].appendChild(hideDiv);
hideDiv.appendChild(hideElement);
hideElement.appendChild(text);


var didClickHide = false;
hideElement.onclick = function(e) {
    e.stopPropagation();
    var divToRemove = elements[0];
    for (var i = 0; i < 4; i += 1) {
        console.log(divToRemove);
        if (divToRemove.parentNode != null) {
            divToRemove = divToRemove.parentNode;
        }
        console.log(i);
    }
    console.log("HElLO WORLD");
    console.log(divToRemove);
    if (divToRemove != null) {
        console.log("did find something to remove");
    } else {
        console.log("nothing to remove");
    }
    while (divToRemove.firstChild) {
        divToRemove.removeChild(divToRemove.firstChild);
    }
    didClickHide = true;
    e.stopPropagation();
};

// window.onbeforeunload = function() {
//   if (didClickHide) {
//     alert('do not redirect');
//     didClickHide = false;
//     return;
//   }
// };


