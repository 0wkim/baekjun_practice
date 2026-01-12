// ISBN 

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./14626.txt");
const INPUT = FS.toString().trim().split("");

const findIndex = INPUT.indexOf("*");

const m = INPUT.pop();

let newNumList = [];
INPUT.forEach((number, index) => {
    if (index % 2 === 0) {
        newNumList.push(number);
    }
    else {
        newNumList.push(number * 3);
    }
});
let answer = newNumList.splice(findIndex, 1);

let newNumSum = (newNumList).map(Number).reduce((acc, cur) => {
    return acc + cur;
}, 0);

let firstNumber = (newNumSum + Number(m)) % 10;

if (findIndex % 2 !== 0) {
    let answerNumber = (10-firstNumber) % 10;

    while (true) {
        if (answerNumber % 3 === 0) break;
        answerNumber = answerNumber + 10;
    }

    answer = answerNumber / 3;
} else {
    answer = 10 - firstNumber;
}

// 일의자리가 0이면 답은 10이 아닌 0이 되어야 함
if (firstNumber === 0) {
    answer = 0;
}

console.log(answer);

