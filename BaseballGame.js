/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function(operations) {
    let s = []

    for (let i of operations){
        if (i === '+'){
            s.push(s[s.length - 1] + s[s.length - 2])
        }else if (i === 'D'){
            s.push(s[s.length - 1] * 2)
        }else if (i === 'C'){
            s.pop()
        }else{
            s.push(parseInt(i))
        }
    }

    let res = 0
    for (let i of s){
        res += i
    }
    return res

    // Time: O(n)
    // Space: O(n)
};
