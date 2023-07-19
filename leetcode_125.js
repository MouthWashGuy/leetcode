// Problem 125: Valid Palindrome

// data structures

// helper functions

// test inputs
var test1 = "A man, a plan, a canal: Panama";
var test2 = "race a car";

// solution here
function solution(s) {
    
    // two pointer approach
    let left = 0;
    let right = s.length - 1;

    // regex to determine if its alphanumeric
    let regex = /^[0-9a-zA-Z]+$/;

    // now just move each pointer in to determine if we have a palindrome
    while (left < right) {

        // if its not alphanumeric
        if (!s.charAt(right).match(regex)) {
            right -= 1;
        } else if (!s.charAt(left).match(regex)) {
            left += 1;
        } else {
            if (s.charAt(right).toLowerCase() != s.charAt(left).toLowerCase()) {
                return false;
            } else {
                right -= 1;
                left += 1;
            }
        }
    }

    return true;
}

// testing
console.log(solution(test1));
console.log(solution(test2));