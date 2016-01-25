package main
import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
)

func main(){
	T := 0
	fmt.Scanf("%d", &T)
	reader, arr := bufio.NewReader(os.Stdin), []int{}
	text, _ := reader.ReadString('\n')

	for _, v := range strings.Fields(text) {
		num, _ := strconv.Atoi(v)
		arr = append(arr, num)
	}
    
    for i := len(arr) - 1; i >= 0; i-- {
        fmt.Print(arr[i], " ")
    }
}
