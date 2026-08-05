"use strict";

// DOM變數
const buttonIg = document.getElementById("ig");
const buttonThreads = document.getElementById("threads");
const post = document.getElementById("post");

// 呼叫API的函式跟參數

// 健康測試API
const checkHealthAPIUrl = "http://127.0.0.1:8000/health";
const checkHealth = async function (url) {
  const response = await fetch(url);
  const data = await response.json();
  console.log(data);
};

// 用健康測試API測試按鈕
const testAPIUrl = "http://127.0.0.1:8000/health";
const apiTest = async function (url) {
  const response = await fetch(url);
  const data = await response.json();
  console.log(data);

  post.value = "test";
};

// Threads post API
const threadsAPIUrl = "http://127.0.0.1:8000/poster/threads";
const threadApi = async function (url) {
  // 這邊需要考慮空白
  const no_space_string = post.value.trim();
  if (no_space_string === "") {
    alert("please enter at least one word");
    return;
  }
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ content: post.value }),
  });
  const data = await response.json();

  console.log(data);
};

// 按鈕事件
buttonIg.addEventListener("click", () => {
  apiTest(testAPIUrl);
});

buttonThreads.addEventListener("click", () => {
  // console.log("test");
  threadApi(threadsAPIUrl);
});

// 健康測試（間隔10秒）
setInterval(() => {
  checkHealth(checkHealthAPIUrl)
}, 10000);