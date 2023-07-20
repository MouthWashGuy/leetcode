// Problem 121: Best Time to Buy and Sell Stock

// data structures

// helper functions

// test inputs
let prices1 = [7,1,5,3,6,4];
let prices2 = [7,6,4,3,1];

// solution here
// important notes: this is an array representing the prices of a single stock, the price fluctuates day by day, but the crux of it, is we must buy it on a certain day and be able to sell it for more in the future.
// key idea, we can keep track of the lowest price seen as we iterate over the price list, when we see a lower price than the one before, we begin checking against that one instead
// at the end we return the highest profit seen from all comparisons

function solution(prices) {

    let max_profit = 0;
    let lowest_price = prices[0];

    // now the for loop
    for (let price of prices) {

        // if the ith price is < than the previously seen lowest, dont bother comparing, just switch em
        if (price < lowest_price) {
            lowest_price = price;
        } else {
            max_profit = Math.max(max_profit, price - lowest_price);
        }
    }

    // now return the max profit seen
    return max_profit;

}


// testing
console.log(solution(prices1));
console.log(solution(prices2));
