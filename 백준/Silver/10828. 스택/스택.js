// 스택

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./10828.txt");
const INPUT = FS.toString().trim().split("\n");

let stack = [];

function pushIn(number, arr) {
    arr.push(number);
}

function popIn(arr) {
    if (arr.length === 0) {
        console.log(-1);
    } else {
        let topNumber = arr.pop();
        console.log(topNumber);
    }
}

function size(arr) {
    console.log(arr.length);
}

function isEmpty(arr) {
    if (arr.length === 0) {
        console.log(1);
    } else {
        console.log(0);
    }
}

function showTop(arr) {
    if (arr.length === 0) {
        console.log(-1);
    } else {
        console.log(arr.at(-1));
    }
}

INPUT.forEach(cmd => {
    if (cmd.includes("push")) {
        let number = Number(cmd.slice(5));
        pushIn(number, stack);
    } else if (cmd.includes("pop")) {
        popIn(stack);
    } else if (cmd.includes("size")) {
        size(stack);
    } else if (cmd.includes("empty")) {
        isEmpty(stack);
    } else if (cmd.includes("top")) {
        showTop(stack);
    }
});
