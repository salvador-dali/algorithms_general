// https://www.hackerrank.com/challenges/plus-minus
package main
import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
)

func main() {
	n := 0
	fmt.Scanf("%d", &n)
	zero, positive, negative := 0, 0, 0
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	for _, v := range (strings.Fields(scanner.Text())) {
		num, _ := strconv.Atoi(v)
		if num > 0{
			positive++
		} else if num < 0 {
			negative++
		} else {
			zero++
		}
	}
	fmt.Printf("%.3f\n", float64(positive)/ float64(n))
	fmt.Printf("%.3f\n", float64(negative)/ float64(n))
	fmt.Printf("%.3f\n", float64(zero)/ float64(n))
}
