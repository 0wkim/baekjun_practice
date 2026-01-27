// 수 찾기 

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./1920.txt");
const INPUT = FS.toString().trim().split("\n");

let nList = new Map();

const n = (INPUT[1].split(" ")).map(Number);
n.forEach((number) => {
    nList.set(number);
});


const m = (INPUT[3].split(" ")).map(Number);
m.forEach((number) => {
    if (nList.has(number)) {
        console.log(1);
    } else {
        console.log(0);
    }
});
