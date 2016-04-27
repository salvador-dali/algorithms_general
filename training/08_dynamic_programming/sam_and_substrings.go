/**
https://www.hackerrank.com/challenges/sam-and-substrings
calculate the sum of all substrings of the numbers
for example having a number 123, all substrings are

1, 2, 3, 12, 23, 123 so the sum is 164

I found out that if the string is
a1, a2, a3, ..., an
then the sum is an * n + 11 * a_n-1 * (n - 1) + and so on
so the main task is to get 1111 % modulo. This is just 1 + 10 + 10^2 + 10^3 mod, which is calculated
with modulo exponentiation
*/

package main

import "fmt"

func powMod(base, exponent, modulo int) int {
	res := 1
	base %= modulo
	for exponent > 0 {
		if exponent%2 == 1 {
			res = (res * base) % modulo
		}
		exponent /= 2
		base = (base * base) % modulo
	}
	return res
}

func generateString(numberString string, modulo int) int {
	sum, prev, n := 0, 0, len(numberString)
	for i := 0; i < n; i++ {
		prev = (prev + powMod(10, i, modulo)) % modulo
		sum = (sum + prev*(n-i)*int(numberString[n-i-1]-48)) % modulo
	}
	return sum
}

func main() {
	stringNum := ""
	fmt.Scanf("%s", &stringNum)
	fmt.Println(generateString(stringNum, 1000000007))
}
