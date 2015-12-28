//https://www.hackerrank.com/contests/round-1-holiday-cup/challenges
package main
import (
	"fmt"
	"bufio"
	"os"
	"strconv"
)

func sieveEratosthenes(n int) []bool {
	is_primes := make([]bool, n+1)
	for i := 2; i <= n; i++ {
		is_primes[i] = true
	}

	for i := 2; i*i <= n; i++ {
		if is_primes[i] {
			for j := i * i; j <= n; j += i {
				is_primes[j] = false
			}
		}
	}
	return is_primes
}

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

func findRepresentation(n int, primes []int) [][]int{
	res := [][]int{}
	for i := 0; i < len(primes); i++ {
		for j := i; j < len(primes); j++ {
			if primes[i] + primes[j] == n {
				res = append(res, []int{primes[i], primes[j]})
			}
		}
	}
	return res
}

func main(){
	prime_arr := sieveEratosthenes(32010)
	primes := []int{}
	for k, v := range prime_arr{
		if v {
			primes = append(primes, k)
		}
	}

	numbers := readManyNumbers()

	for _, n := range numbers {
		res := findRepresentation(n, primes)
		fmt.Printf("%d has %d representation(s)\n", n, len(res))
		for _, nums := range res {
			fmt.Printf("%d+%d\n", nums[0], nums[1])
		}
		fmt.Println("")
	}
}
