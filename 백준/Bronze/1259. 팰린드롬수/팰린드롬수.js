// 팰린드롬수

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./1259.txt");
const INPUT = FS.toString().trim().split("\n");

INPUT.forEach((numbers) => {

    if (numbers === "0") return;

    let length = numbers.length;
    let iterateCount = Math.ceil(length / 2);
    let flag = true;

    for (let i = 0; i < iterateCount; i++) {
        if ((numbers[i] !== numbers[length-i-1]) || numbers[0] === "0") {
            flag = false;
            break;
        }
    }
    
    if (flag === false) {
        console.log("no");
    } else {
        console.log("yes");
    }
});

