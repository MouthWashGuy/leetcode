prices = [7,1,5,3,6,4]

def sol(prices):

# we can do it in O(n) time and O(1) space using a simple two pointer approach
        # the trick is to designate 2 pointers, one for the index for the day we wish to buy the stock
        # another for the index we wish to sell
        # when we find that the sell < buy pointers prices, we will shift both pointers to that location and continue checking from there

        if len(prices) <= 1:
            return 0

        buy_pointer = 0 # we try and buy on the first day
        sell_pointer = 1 # and then compare it to day 2

        max_profit = 0 # of course if we find that we keep running into negative profit, we can just return 0 at the end

        # heres the loop
        while(sell_pointer < len(prices)):

            # here we can do the shift if we notice that sell_pointer < buy pointer
            if prices[buy_pointer] < prices[sell_pointer]:
                buy_pointer = sell_pointer
                sell_pointer = buy_pointer + 1

            # now we can begin incrementing and price checks
            max_profit = max(max_profit, prices[sell_pointer] -  prices[buy_pointer])
            sell_pointer += 1

        return max_profit

print(sol(prices))

