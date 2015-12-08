// https://www.hackerrank.com/challenges/extra-long-factorials
package main

import (
    "fmt"
    "math/big"
)

func main() {
	n := int64(0)
	fmt.Scanf("%d", &n)
    x := new(big.Int)
    x.MulRange(1, n)
    fmt.Println(x)
}
