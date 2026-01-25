// 팩토리얼 0의 개수 

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./1676.txt");
// const INPUT = (FS.toString().trim().split("\n")).map(Number);

const n = Number(FS.toString());

let zeroCount = Math.floor(n/5) + Math.floor(n/25) + Math.floor(n/125);
console.log(zeroCount);