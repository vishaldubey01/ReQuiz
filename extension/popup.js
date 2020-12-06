// Copyright 2018 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

"use strict";

let changeColor = document.getElementById("changeColor");
let userid = document.getElementById("userid").value;

chrome.storage.sync.get("color", function (data) {
  changeColor.style.backgroundColor = data.color;
  changeColor.setAttribute("value", data.color);
});

function getText() {
  return document.body.innerText;
}

function login() {
  return userid;
}

changeColor.onclick = function (element) {
  userid = login();
  console.log("userid: " + userid);

  let color = element.target.value;
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    chrome.tabs.executeScript(
      tab.id,
      {
        code: "var config = 1;",
      },
      function () {
        chrome.tabs.executeScript(tab.id, { file: "content.js" });
      }
    );
  });
};
