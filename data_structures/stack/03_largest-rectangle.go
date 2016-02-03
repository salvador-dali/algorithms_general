package main
import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"strconv"
)

func main(){
	reader, arr, T := bufio.NewReader(os.Stdin), []int{}, 0
	fmt.Scanf("%d", &T)
	text, _ := reader.ReadString('\n')
    if len(text) == 1 {
        text, _ = reader.ReadString('\n')
    }
	for _, v := range strings.Fields(text) {
		num, _ := strconv.Atoi(v)
		arr = append(arr, num)
	}
	
	max, i, stack, top := 0, 0, []int{}, 0
	for i < len(arr) {
		if len(stack) == 0 || arr[stack[len(stack) - 1]] <= arr[i] {
			stack = append(stack, i)
			i++
		} else {
			top, stack = stack[len(stack) - 1], stack[:len(stack) - 1]
			area := arr[top] * i
			if len(stack) > 0 {
				area = arr[top] * (i - stack[len(stack) - 1] - 1)
			}
			if max < area {
				max = area
			}
		}
	}

	for len(stack) > 0 {
		top, stack = stack[len(stack) - 1], stack[:len(stack) - 1]
		area := arr[top] * i
		if len(stack) > 0 {
			area = arr[top] * (i - stack[len(stack) - 1] - 1)
		}
		if max < area {
			max = area
		}
	}
	fmt.Println(max)
}
