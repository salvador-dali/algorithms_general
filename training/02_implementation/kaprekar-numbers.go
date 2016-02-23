// https://www.hackerrank.com/challenges/kaprekar-numbers
package main
import (
	"fmt"
)

func isKaprekar(n uint64)bool{
	if n == 1 || n == 9{
		return true
	}

	tmp, mod := n, uint64(1)
	for tmp > 0{
		tmp /= 10
		mod *= 10
	}

	tmp = n * n
	first, second := tmp / mod, tmp % mod
	if second == 0{
		return false
	}
	return first + second == n
}

func main(){
	var p, q uint64
	fmt.Scanf("%d", &p)
	fmt.Scanf("%d", &q)

	arr := []uint64{}
	for i := p; i <= q; i++{
		if isKaprekar(i){
			arr = append(arr, i)
		}
	}
	if len(arr) != 0{
		for _, v := range(arr){
			fmt.Print(v, " ")
		}
	} else {
		fmt.Println("INVALID RANGE")
	}
}

