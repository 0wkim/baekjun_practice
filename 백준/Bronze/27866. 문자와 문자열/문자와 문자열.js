// 문자와 문자열

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./27866.txt");
const INPUT = FS.toString().trim().split("\n");

const word = INPUT[0];
const i = INPUT[1];

console.log(word[i-1]);