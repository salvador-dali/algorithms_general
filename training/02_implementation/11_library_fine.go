//https://www.hackerrank.com/challenges/library-fine
package main
import (
	"fmt"
)

func main(){
	var d1, m1, y1, d2, m2, y2 int

	fmt.Scanf("%d %d %d", &d1, &m1, &y1)
	fmt.Scanf("%d %d %d", &d2, &m2, &y2)
	
	if d1 + m1 * 100 + 10000 * y1 <= d2 + m2 * 100 + 10000 * y2{
		fmt.Println(0)
	} else if y1 != y2{
		fmt.Println(10000)
	} else if m1 != m2{
		fmt.Println((m1 - m2) * 500)
	} else if d1 != d2{
		fmt.Println((d1 - d2) * 15)
	}
}
