

window.onload = () => {
    var url = window.location.href;
    console.log("URL IS " + url);
  
    if (url.includes("https://en.wikipedia.org/")) {
      var text = document.body
        .querySelector(".mw-parser-output")
        .innerText
        .trim();
    }
    console.log(text);
};
  