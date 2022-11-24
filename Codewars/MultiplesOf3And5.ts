// Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
// Additionally, if the number is negative, return 0 (for languages that do have them).
// Note: If the number is a multiple of both 3 and 5, only count it once.

export class Challenge {
    static solution(num: number) {
      let summ: number = 0;
      for (let multiple = 0; multiple < num; multiple++) {
        if (multiple % 3 === 0 || multiple % 5 === 0) {
          summ += multiple
        }
      }
      return summ
    }
}