// https://www.hackerrank.com/challenges/maximum-element
// maintain two stacks. One with elements, another with maximum elements
package main
import (
	"fmt"
	"os"
	"bufio"
    "strings"
    "strconv"
)

func main(){
	T, reader := 0, bufio.NewReader(os.Stdin)
    fmt.Scanf("%d", &T)
    stack_values, stack_max := []int{}, []int{}
    for ; T > 0; T--{
		text, _ := reader.ReadString('\n')
		arr := []int{}
		for _, v := range (strings.Fields(text)) {
			num, _ := strconv.Atoi(v)
			arr = append(arr, num)
		}
        if arr[0] == 1 {
            stack_values = append(stack_values, arr[1])
			appending := 0
            if len(stack_max) == 0 {
				appending = arr[1]
			} else if stack_max[len(stack_max) - 1] <= arr[1] {
				appending = arr[1]
			} else {
				appending = stack_max[len(stack_max) - 1]
			}
			stack_max = append(stack_max, appending)
        } else if arr[0] == 2 {
			stack_values = stack_values[:len(stack_values) - 1]
			stack_max = stack_max[:len(stack_max) - 1]
        } else {
			fmt.Println(stack_max[len(stack_max) - 1])
        }
    }
}
