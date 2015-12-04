// https://www.hackerrank.com/challenges/staircase
package main
import (
	"fmt"
)

func main(){
	n := 0
	fmt.Scanf("%d", &n)
	for i := 1; i <= n; i++{
		stair := ""
		for j := 0; j < n - i; j++{
			stair += " "
		}
		for j := 0; j < i; j++{
			stair += "#"
		}
		fmt.Println(stair)
	}
}
