// Problem 20: Valid Parantheses

// data structures

// helper functions

// test inputs
let test1 = "()";
let test2 = "()[]{}";
let test3 = "(]";
let test4 = "[(())]"
let test5 = "]"

// solution here
function solution(s) {

    // dict used to map one parantheses type to the other
    var char_map = {"]":"[", "}":"{", ")":"("};

    // idea, we can check if a parantheses is valid by performing a linear scan of the string, adding right side parantheses to a stack and popping them when observing a leftside parantheses
    let stack = [];

    // simple for each/of loop
    for (let char of s) {

        if (char == "[" || char == "(" || char == "{") {
            stack.push(char);
        } else {
            
            // we also have to check if the stack is empty since popping from an empty stack is null
            if (stack.length == 0) {
                return false;
            }

            // if not then we can check for the fail condition
            if (stack.pop() != char_map[char]) {
                return false;
            }
        }
    }

    // now we can do a final check to see if the stack still has unmatched items
    return (stack.length == 0);
}

// testing
console.log(solution(test1));
console.log(solution(test2));
console.log(solution(test3));
console.log(solution(test4));
console.log(solution(test5));
