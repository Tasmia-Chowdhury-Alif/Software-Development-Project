//  Q.1

var result = 80;

if (result < 0) {
    console.log("Failed");
}
else if (result >= 0 && result < 40) {
    console.log("Tumi C grade paico");
}
else if (result >= 40 && result < 60) {
    console.log("Tumi B grade paico");
}
else if (result >= 60 && result < 70) {
    console.log("Tumi -A grade paico");
}
else if (result >= 70 && result < 80) {
    console.log("Tumi A grade paico");
}
else if (result >= 80 && result <= 100) {
    console.log("Tumi A+ grade paico");
}
else {
    console.log("invalid");
}

// Q.2

let num = prompt("Enter your name:");

if (num % 2 == 0) {
    console.log(`The Number ${num} is an Even`);
}
else {
    console.log(`The Number ${num} is an Odd`);
}


// Q.3

let numbers = [12, 5, 19, 1, 7, 15, 3, 20, 8, 2, 17, 4, 10, 14, 6, 9, 11, 13, 18, 16];

numbers.sort(
    function (a, b) {
        return a - b;
    }
)

console.log(numbers);


// Q.4

const check_leapyear = (y) => {
    return (y % 4 == 0 && (y % 100 != 0 || y % 400 == 0));
}

let year = parseInt(prompt("Enter a year to check leap year :"));

if (check_leapyear(year)) {
    console.log(`The year ${year} is a Leapyear`);
}
else {
    console.log(`The year ${year} is not a Leapyear`);
}

// Q.5 

const arr = [];
for (let i = 1; i <= 50; i++) {

    if (i % 3 == 0 && i % 5 == 0) {
        arr.push(i);
    }
}
console.log(arr);

// Q.6 

const largestName = (arr) => {
    let lgName = arr[0];

    for (let i = 1; i < arr.length; i++) {
        if (arr[i].length > lgName.length) {
            lgName = arr[i];
        }
    }
    return lgName;
}

var friends = ["rahim", "karim", "abdul", "sadsd", "heroAlom"];


const largestfriend = largestName(friends);

console.log(largestfriend);


// Q.7

var numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];

numbers = new Set(numbers);

for (let i of numbers) {
    console.log(i);
}
console.log(numbers);


// Q.8

var numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];

let maxNum = Math.max(...numbers);
console.log(maxNum);


// Q.9

const monthlySavings = (arr, num) => {
    if (!(Array.isArray(arr)) || typeof num != 'number') {
        console.log("invalid input");
        return;
    }

    let savings = 0;
    arr.forEach((payment) => {
        if (payment >= 3000) {
            payment -= payment * 0.2;
        }
        savings += payment;
    });

    savings -= num;
    if (savings < 0) {
        console.log("earn more");
    }
    else {
        console.log(savings);
    }
}

let allPayments = [1000, 2000, 3000];
let leavingCost = 5400;

monthlySavings(allPayments, leavingCost); 