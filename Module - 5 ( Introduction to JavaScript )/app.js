// var num = "1.5";
// var num1 = 100;

// console.log(parseFloat(num)+num1);

// var txt = "rain";

// if(txt == 'rain' && true){
//     console.log("take rain coat");
// }
// else if(txt == 'rain'){
//     console.log("Take Umbrella");
// }
// else {
//     console.log("Don't go outside");
// }

// let objt = {
//     name : "Alif",
//     roll : 687817,
//     dept : "CMT",
//     age : 21
// };

// console.log(objt.key());

// var st = "Alif";

// var friends = ["abcd", 4, "klkf", st, 2.35, { roll: 687817 }, "Beef"];

// friends.push(["Alif", "..."]);
// friends.push("adfj");
// friends.pop();

// friends.unshift("Gias");
// friends.shift();

// console.log(friends);

// for (var i = 0; i < friends.length; i++) {
//     console.log(i);
// }


// let a = 5;
// a = 20;
// console.log(a);

// let name = "Alif";

// console.log(`Hello My name is ${name} and I'm ${a} years old`);

// let arr = [1,2,3,4,5,6,7,8,9];

// console.log(Math.max(...arr));


// const ob = {
//     name : "Alif",
//     roll : 687817,
//     dept : "CST"
// };

// const {name,dept} = ob;
// console.log(dept); 

//  Arrow function 
// const sum = (num1 , num2) => {
//     return num1+num2
// };

// const result = sum(20,50);
// console.log(result);


// const arr = [
//     { id: "01", name: "a" },
//     { id: "02", name: "b" },
//     { id: "03", name: "c" },
//     { id: "04", name: "d" },
// ];

// let x = arr.find(product => product.id == "03"); 
// console.log(x);


const even_odd=(aray)=> {
    let even_items = [];
    let odd_items = [];

    for(let i = 0; i < aray.length ; i++){
        if(aray[i]%2 == 0){
            even_items.push(aray[i]);
        }
        else{
            odd_items.push(aray[i]);
        }
    }
    return even_items;
}

const numbers = [1,2,3,4,5,6,7,8,9];

let od = even_odd(numbers);
console.log("From 105 line "+ od);