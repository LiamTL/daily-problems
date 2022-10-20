// Complete the function that takes two integers (a, b, where a < b).
// Return an array of all integers between the input parameters, a and b.

function between(a, b) {
    lst = []
    for (let i = a; i <= b; i++) {
        lst.push(i)
    } return lst
}
