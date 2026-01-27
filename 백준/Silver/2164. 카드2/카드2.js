// 카드2

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./2164.txt");
const INPUT = FS.toString().trim().split("\n");

let top = 0; 

let numList = [];
for (let i = 1; i < Number(INPUT[0])+1; i++) {
    numList.push(i);
}

while (numList.length - top > 1) {
    top++;
    let firstNum = numList[top];
    top++;
    numList.push(Number(firstNum));
}

console.log(numList[top]);


