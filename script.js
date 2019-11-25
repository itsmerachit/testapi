var loadscript = new Promise(function(resolve, reject) {
    var script = document.createElement('script');
    script.setAttribute('type', 'text/javascript');
    script.setAttribute('src', 'https://wchat.freshchat.com/js/widget.js');
    document.body.appendChild(script);
    console.log("here");
});
console.log(loadscript);
loadscript.then(function(){
console.log("111");
    window.fcWidget.init({
        token: "0ade0b51-2f2a-4e74-8e16-2a008f321465",
        host: "https://wchat.freshchat.com",
    });
});
