// 음계

const FS = require('fs').readFileSync(process.platform === "linux"?"/dev/stdin":"./2920.txt");
const numbers = (FS.toString().split(" ")).map(Number);

const ascendingNumbers = [...numbers].sort((a, b) => a - b);
const descendingNumbers = [...numbers].sort((a, b) => b - a);

if (numbers.join(" ") === ascendingNumbers.join(" ")) {
    console.log("ascending");
}
else if (numbers.join(" ") === descendingNumbers.join(" ")) {
    console.log("descending");
}
else {
    console.log("mixed");
}