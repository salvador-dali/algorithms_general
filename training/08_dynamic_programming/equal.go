/**
https://www.hackerrank.com/challenges/equal/
the problem is equivalent of removing 1, 2, 5 from any element of the array
till all the in the array will be the same. The result will be the number of
times you need to take these values

The steps are independent (the way you are taking elements from array[1] does not
depend on how you were taking elements from array[0]), and one thing to notice is
that if you have a n elements the shortest way to take them would be to take greedy
as many 5 as possible, then 2 and then 1

Also notice that from starting array [7, 12, 23, 8, 13]
we need to try to reach from 7 ( the smallest) to each number, 6, 5, 4, 3, 2, 1, 0
But after more though consideration it is seen that every number of steps for an array
less than 7-5 will be bigger than one of the previous 5 elements
*/

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func bestToReach(num int) int {
	stepsNum, stepsValues := 0, []int{5, 2, 1}
	for _, step := range stepsValues {
		stepsNum += num / step
		num %= step
	}
	return stepsNum
}

func bestToReachArr(arr []int) int {
	s := 0
	for _, v := range arr {
		s += bestToReach(v)
	}
	return s
}

func findStepNumbers(arr []int) {
	min := arr[0]
	for _, v := range arr {
		if v < min {
			min = v
		}
	}

	smallest := 1000000000
	for start := min; start >= 0 && min-start < 6; start-- {
		tmp := []int{}
		for _, v := range arr {
			tmp = append(tmp, v-start)
		}
		r := bestToReachArr(tmp)
		if r < smallest {
			smallest = r
		}
	}
	fmt.Println(smallest)
}

func readManyArrays() {
	T := 0
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Scanf("%d", &T)
	for T > 0 {
		T--
		scanner.Scan()
		scanner.Scan()
		arr := []int{}
		for _, v := range strings.Fields(scanner.Text()) {
			num, _ := strconv.Atoi(v)
			arr = append(arr, num)
		}
		findStepNumbers(arr)
	}
}

func main() {
	readManyArrays()
}
