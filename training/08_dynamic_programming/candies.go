//https://www.hackerrank.com/challenges/candies/
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func readManyNumbers() []int {
	var T int
	fmt.Scanf("%d", &T)

	scanner, numbers := bufio.NewScanner(os.Stdin), []int{}
	for T > 0 {
		T--
		scanner.Scan()
		num, _ := strconv.Atoi(scanner.Text())
		numbers = append(numbers, num)
	}
	return numbers
}

func getSolution(arr []int) int {
	res := make([]int, len(arr))
	for i := 0; i < len(arr); i++ {
		res[i] = 1
	}

	for i := 0; i < len(arr)-1; i++ {
		if arr[i] < arr[i+1] {
			res[i+1] = res[i] + 1
		}
	}

	for i := len(arr) - 1; i >= 1; i-- {
		if arr[i-1] > arr[i] {
			if res[i-1] > res[i]+1 {
				res[i-1] = res[i-1]
			} else {
				res[i-1] = res[i] + 1
			}
		}
	}

	val := 0
	for _, v := range res {
		val += v
	}
	return val
}

func main() {
	arr := readManyNumbers()
	fmt.Println(getSolution(arr))
}
