// https://www.hackerrank.com/challenges/funny-string
package main

import "fmt"

func readNum() int {
	var n int
	_, err := fmt.Scanf("%d", &n)
	if err != nil {
		panic(err)
	}
	return n
}

func readWord() string {
	var s string
	_, err := fmt.Scanf("%s", &s)
	if err != nil {
		panic(err)
	}
	return s
}

func calc(i1 uint8, i2 uint8) uint8 {
	if i1 > i2 {
		return i1 - i2
	} else {
		return i2 - i1
	}
}

func isFunny(s string) bool {
	for i := 0; i < len(s)-1; i++ {
		if calc(s[i+1], s[i]) != calc(s[len(s)-i-1], s[len(s)-i-2]) {
			return false
		}
	}
	return true
}

func main() {
	var s string
	n := readNum()
	for i := 0; i < n; i++ {
		s = readWord()
		if isFunny(s) {
			fmt.Println("Funny")
		} else {
			fmt.Println("Not Funny")
		}
	}
}
