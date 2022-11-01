// Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
// It should remove all values from list a, which are present in list b keeping their order.


function arrayDiff(a, b) {
    diff = []
    if (a === [] || a === null) {
      return []
    }
    for (let num = 0; num < a.length; num++){
        if (!b.includes(a[num])) {
            diff.push(a[num])
        }
    }
    return diff
}