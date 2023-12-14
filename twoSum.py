/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let dic = new Object();
    for (let i = 0; i < nums.length; i++){
        compliment = target - nums[i]
        if (dic.hasOwnProperty(compliment)){
            return ([dic[compliment], i])
        }
        dic[nums[i]] = i;
    }
};
