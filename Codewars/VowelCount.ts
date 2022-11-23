export class Kata {
    static getCount(str: string): number {
      let vowels: string = "aeiouAEIOU";
      let count: number = 0;
      for (let vowel = 0; vowel < str.length; vowel++) {
        if (vowels.includes(str[vowel])) {
          count++;
        }
      }
      return count
    }
  }