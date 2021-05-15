
function submitPostForm() {
    var http = new XMLHttpRequest();


    var payload = { 
        title: null, 
        subreddit: null, 
        username: null, 
        body: null, 
        numUpvotes: null, 
        date: null 
    }

    payload.title = document.getElementById("post_title").value;
    payload.subreddit = document.getElementById("subreddit").value;
    payload.username = document.getElementById("username").value;





    http.open("POST", "/posts", true);
    http.setRequestHeader("Content-type","application/json");









    http.send(params);
    http.onload = function() {
        alert(http.responseText);
    }
}


