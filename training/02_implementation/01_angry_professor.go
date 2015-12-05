// https://www.hackerrank.com/challenges/angry-professor
package main
import (
	"fmt"
    "bufio"
    "os"
    "strings"
    "strconv"
)

func main(){
    T := 0
	scanner := bufio.NewScanner(os.Stdin)
    fmt.Scanf("%d", &T)
    for T > 0{
        T--
		scanner.Scan()
        values := []int{}
		for _, v := range (strings.Fields(scanner.Text())) {
			num, _ := strconv.Atoi(v)
			values = append(values, num)
		}
        N := values[1]
		scanner.Scan()
        negative := 0
		for _, v := range (strings.Fields(scanner.Text())) {
			num, _ := strconv.Atoi(v)
			if num <= 0{
                negative++
            }
		}
		if N <= negative{
            fmt.Println("NO")
        } else {
            fmt.Println("YES")
        }
    }
}
