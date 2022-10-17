// In this simple exercise, you will build a program that takes a value, integer , and returns a list of its multiples up to another value, limit.
// If limit is a multiple of integer, it should be included as well.
// For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.

function findMultiples(integer, limit) {
    multiples = []
    for (let multiple = integer; multiple <= limit; multiple++){
        if (multiple % integer == 0) {
            multiples.push(multiple)
        }
        else{
            continue
      }
    }
    return multiples
}