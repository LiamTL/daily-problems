function countPositivesSumNegatives(input) {
    negatives = 0
    positives = 0
    if (input === null) {
      return []
    }
    for (let num = 0; num < input.length; num++){
      if (input[num] > 0){
        positives += 1
      } else if (input[num] < 0) {
        negatives += input[num]
      } 
    }
    if (negatives === 0 && positives === 0){
      return []
    }
    return [positives, negatives]
  }