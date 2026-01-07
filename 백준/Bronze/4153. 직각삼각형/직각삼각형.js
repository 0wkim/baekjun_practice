// 직각삼각형

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./4153.txt");
const INPUT = FS.toString().split("\n");

let numbersList = INPUT.map((numbers) => {
    return (numbers.split(" ")).map(Number);
});
// numbersList.pop();

numbersList.map((list) => {
    list.sort((a, b) => a - b);
});

for (let i = 0; i < numbersList.length; i++) {
    if (numbersList[i][0] === 0 && numbersList[i][1] === 0 && numbersList[i][2] === 0) break;

    if (numbersList[i][0]**2 + numbersList[i][1]**2 === numbersList[i][2]**2) {
        console.log("right");
    }
    else {
        console.log("wrong");
    }
}