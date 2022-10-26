function solution(number){
    summ = 0
    for (let multiple = 0; multiple < number; multiple++){
      if (multiple % 3 === 0 || multiple % 5 === 0) {
        summ += multiple
      }
    }
    return summ
  }