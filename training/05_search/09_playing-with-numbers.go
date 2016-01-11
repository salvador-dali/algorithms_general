// https://www.hackerrank.com/challenges/playing-with-numbers
// https://www.hackerrank.com/contests/101hack21/challenges/playing-with-numbers/
package main
import (
    "fmt"
    "os"
    "bufio"
    "strings"
    "strconv"
    "sort"
)


func summation(arr []int, queries []int){
	l := len(arr)
	sort.Ints(arr)
	cumulative := make([]int, l + 1)
	for i := 0; i < l; i++{
		cumulative[i + 1] = cumulative[i] + arr[i]
	}

	x := 0
	for _, el := range(queries){
		x += el
		i := sort.Search(l, func(i int) bool { return arr[i] >= -x })
		n_bigger := l - i
		n_smaller:= i

		sum1 := n_bigger * x + cumulative[l] - cumulative[i]
		sum2 := -cumulative[i] - n_smaller * x
		fmt.Println(sum1 + sum2)
	}

}
func main() {
    arr, queries := []int{}, []int{}
    reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')
    text, _ = reader.ReadString('\n')

	for _, v := range (strings.Fields(text)) {
		num, _ := strconv.Atoi(v)
		arr = append(arr, num)
	}
    text, _ = reader.ReadString('\n')
    text, _ = reader.ReadString('\n')
	for _, v := range (strings.Fields(text)) {
		num, _ := strconv.Atoi(v)
		queries = append(queries, num)
	}
    summation(arr, queries)
}
