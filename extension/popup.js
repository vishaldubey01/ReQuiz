// Copyright 2018 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

"use strict";

let changeColor = document.getElementById("changeColor");

var url = window.location.href;
console.log("URL IS " + url);

if (url.includes("https://en.wikipedia.org/")) {
  var text = document.body
    .querySelector(".mw-parser-output")
    .innerText
    .trim();
}
console.log(text);

chrome.storage.sync.get("color", function (data) {
  changeColor.style.backgroundColor = data.color;
  changeColor.setAttribute("value", data.color);
});

function getText() {
  return document.body.innerText;
}

changeColor.onclick = function (element) {
  let color = element.target.value;
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    chrome.tabs.executeScript(tabs[0].id, {
      code: 'document.body.style.backgroundColor = "' + color + '";',
    });
  });
};
