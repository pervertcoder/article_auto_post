"use strict";

// DOM變數
const buttonIg = document.getElementById("ig");
const buttonThreads = document.getElementById("threads");

const buttonAddParagraph = document.getElementById("add");
const buttonDeleteParagraph = document.getElementById("delete");

const parentSection = document.querySelector(".workarea");

// 畫面功能函式
let dataId = 0;
const alphabet = [
  "b",
  "c",
  "d",
  "e",
  "f",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z",
];
const addParagraphFun = function () {
  const addedParagraph = document.createElement("textarea");
  addedParagraph.name = "post";
  addedParagraph.id = "post" + "_" + alphabet[dataId];
  addedParagraph.classList = "poster";
  addedParagraph.dataset.id = dataId + 1;
  addedParagraph.rows = 10;
  addedParagraph.cols = 30;

  const addParagraph = parentSection.appendChild(addedParagraph);
  dataId++;
};
const deleteParagraphFun = function () {
  if (parentSection.childElementCount >= 4) {
    parentSection.removeChild(parentSection.lastElementChild);
    dataId--;
  } else {
    console.log("no more added paragraph to delete");
    return;
  }
};

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
  const poster_context = document.querySelectorAll(".poster");
  const response = await fetch(url);
  const data = await response.json();
  console.log(data);

  const nodeListNum = poster_context.length;
  let context_arr = [];
  for (let i = 0; i < nodeListNum; i++) {
    // console.log(poster_context[i].value);
    context_arr.push(poster_context[i].value);
  }
  console.log(context_arr);
};

// Threads post API
const threadsAPIUrl = "http://127.0.0.1:8000/poster/threads";
const threadApi = async function (url) {
  const poster_context = document.querySelectorAll(".poster");
  // 這邊需要考慮空白
  // const no_space_string = post.value.trim();
  // if (no_space_string === "") {
  //   alert("please enter at least one word");
  //   return;
  // }
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ content: no_space_string }),
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

buttonAddParagraph.addEventListener("click", () => {
  addParagraphFun();
});

buttonDeleteParagraph.addEventListener("click", () => {
  deleteParagraphFun();
});

// 健康測試（間隔1分鐘）
setInterval(() => {
  checkHealth(checkHealthAPIUrl);
}, 600000);
