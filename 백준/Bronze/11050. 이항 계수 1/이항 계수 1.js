// 최대공약수와 최소공배수 

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./11050.txt");
const INPUT = (FS.toString().trim().split(" ")).map(Number);

const n = INPUT[0];
const k = INPUT[1];

const numList = Array.from({length: k}, (_, i) => n - i);
const numListProduct = numList.reduce((acc, cur) => {
    return acc * cur;
}, 1);

const denList = Array.from({length: k}, (_, i) => k - i);
const denListProduct = denList.reduce((acc, cur) => {
    return acc * cur;
}, 1);

const result = numListProduct / denListProduct;
console.log(result);