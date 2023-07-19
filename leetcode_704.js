// Problem 704: Binary Search

// data structures

// helper functions

// test inputs
let test1 = [-1,0,3,5,9,12];

// solution here
function solution(nums, target) {

    // standard binary search 
    let hi = nums.length;
    let lo = 0;

    while (lo < hi - 1) {

        // find the midpoint
        let mid = Math.floor((hi+lo)/2);

        // now reduce the search space
        if (nums[mid] <= target) {
            lo = mid;
        } else {
            hi = mid;
        }
    }

    // now we item should be at array[lo], if it is not, its not in the array
    if (nums[lo] == target) {
        return lo;
    } else {
        return -1;
    }
}

// testing
console.log(solution(test1, 9));
console.log(solution(test1, 2));
