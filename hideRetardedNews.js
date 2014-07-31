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
var elementCount = elements.length;

for (var j = 0; j < elementCount; j += 1) {
    var element = elements[j];
    var hideDiv = document.createElement('h2');
    var hideDivClassName = 'esc-lead-article-title';
    // hideDiv.setAttribute('class', hideDivClassName);
    var hideElement = document.createElement('a');

    hideElement.class = "MyClassName";
    var text = document.createTextNode("HIDE NEWS");

    element.appendChild(hideDiv);
    hideDiv.appendChild(hideElement);
    hideElement.appendChild(text);


    var didClickHide = false;

    hideElement.onclick = function(hE) {
        return function(e) {
            e.stopPropagation();

            var divToRemove = hE;

            for (var i = 0; i < 10; i += 1) {
                console.log(divToRemove);
                if (divToRemove.parentNode != null) {
                    divToRemove = divToRemove.parentNode;
                }
            }
            console.log(divToRemove);
            while (divToRemove.firstChild) {
                divToRemove.removeChild(divToRemove.firstChild);
            }
            didClickHide = true;
            e.stopPropagation();
        };
    } (hideElement);
}

// window.onbeforeunload = function() {
//   if (didClickHide) {
//     alert('do not redirect');
//     didClickHide = false;
//     return;
//   }
// };

