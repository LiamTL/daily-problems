// Complete the function that takes a non-negative integer n as input and returns a list of all the powers of 2 with the exponent ranging from 0 to n.

function powersOfTwo(n){
    powersLst = []
    for (let power = 0; power < n+1; power++)
      powersLst.push(2 ** power)
    return powersLst
  }