//https://www.hackerrank.com/contests/round-1-holiday-cup/challenges/oddities
package main

import (
	"bufio"
	"os"
	"strconv"
	"fmt"
)

func main(){
	var T int
	fmt.Scanf("%d", &T)

	scanner := bufio.NewScanner(os.Stdin)
	for T > 0 {
		T--
		scanner.Scan()
		num, _ := strconv.Atoi(scanner.Text())
		if num % 2 == 0 {
			fmt.Printf("%d is even\n", num)
		} else {
			fmt.Printf("%d is odd\n", num)
		}
	}
}
