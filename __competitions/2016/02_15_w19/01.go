package main
import (
	"fmt"
)

func isPositive(a, b, c, d, e, f int) bool{
	if a + b + c + d < 0 || a + b + f < 0 || a + e + d < 0 {
		return false
	}
	return true
}

func findSmallest(a, b, c, d, e, f int) int {
	if isPositive(a, b, c, d, e, f) {
		return 0
	}

	minimum := 100000
	for i := 1; i < minimum; i++ {
		if isPositive(a + i, b, c, d, e, f){
			minimum = i
			break
		}
	}

	for i := 1; i < minimum; i++ {
		if isPositive(a, b + i, c, d, e, f){
			minimum = i
			break
		}
	}

	for i := 1; i < minimum; i++ {
		if isPositive(a, b, c + i, d, e, f){
			minimum = i
			break
		}
	}

	for i := 1; i < minimum; i++ {
		if isPositive(a, b, c, d + i, e, f){
			minimum = i
			break
		}
	}

	for i := 1; i < minimum; i++ {
		if isPositive(a, b, c, d, e + i, f){
			minimum = i
			break
		}
	}

	for i := 1; i < minimum; i++ {
		if isPositive(a, b, c, d, e, f + i){
			minimum = i
			break
		}
	}

	return minimum
}

func main(){
	a, b, c, d, e, f := 0, 0, 0, 0, 0, 0
	fmt.Scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f)
	fmt.Println(findSmallest(a, b, c, d, e, f))
}
