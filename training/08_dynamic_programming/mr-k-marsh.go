package main
import (
	"fmt"
	"time"
)

func main(){
	start := time.Now()
	n := 500
	a := 1
	for x1 := 0; x1 < n; x1++ {
		for y1 := 0; y1 < n; y1++ {
			for x2 := x1 + 1; x2 < n; x2++ {
				for y2 := y1 + 1; y2 < n; y2++ {
//					fmt.Println(x1, y1, x2, y2)
					a++
				}
			}
		}
	}


	elapsed := time.Since(start)
	fmt.Println(elapsed)
}
