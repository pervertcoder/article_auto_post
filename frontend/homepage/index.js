"use strict";

const buttonIg = document.getElementById("ig");
const post = document.getElementById("post");

const testAPIUrl = "http://127.0.0.1:8000/health"
const apiTest = async function (url) {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data)

    post.value = data.message;
};

buttonIg.addEventListener("click", () => {
    apiTest(testAPIUrl)
});