/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let l = 0
    let r = nums.length - 1
    let res = []

    while (l <= r){
        if (Math.abs(nums[l]) < Math.abs(nums[r])){
            res.push(nums[r] ** 2)
            r--
        }else{
            res.push(nums[l] ** 2)
            l++
        }
    }

    return res.reverse()

    // Time: O(n)
    // Space: O(n)

};
