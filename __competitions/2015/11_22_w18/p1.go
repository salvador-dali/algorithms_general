/*
https://www.hackerrank.com/contests/w18/challenges/ghosts
just a straight forward iteration through all the values to check
whether it passes all the conditions

Fully solved
 */
package main
import (
	"fmt"
    "bufio"
    "strings"
    "strconv"
    "os"
)

func gcd(x, y int) int {
    for y != 0 {
        x, y = y, x % y
    }
    return x
}

func readArr() []int {
	arr := []int{}
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	for _, v := range (strings.Fields(scanner.Text())) {
		num, _ := strconv.Atoi(v)
		arr = append(arr, num)
	}
	return arr
}

func main(){
	arr := readArr()
	A, B, C, D := arr[0], arr[1], arr[2], arr[3]

	count := 0
	for a := 1; a <= A; a++ {
		for b := 1; b <= B; b++ {
			for c := 1; c <= C; c++ {
				for d := 1; d <= D; d++ {
					if (a - b) % 3 == 0 && (b + c) % 5 == 0 && (a*c) % 4 == 0 && gcd(a, d) == 1 {
						count++
					}
				}
			}
		}
	}
	fmt.Println(count)
}
