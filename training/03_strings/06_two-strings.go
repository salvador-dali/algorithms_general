//https://www.hackerrank.com/challenges/two-strings
package main
import "fmt"

func subst(s1 string, s2 string) bool {
	m := map[uint8]bool{}

	for i := 0; i < len(s1); i++ {
		m[s1[i]] = true
	}

	for i := 0; i < len(s2); i++ {
		if m[s2[i]] {
			return true
		}
	}
	return false
}

func main() {
	var n int
	var s1, s2 string

	fmt.Scanf("%d", &n)
	for i := 0; i < n; i++ {
		fmt.Scanf("%s", &s1)
		fmt.Scanf("%s", &s2)
		if subst("hello", "word") {
			fmt.Println("YES")
		} else {
			fmt.Println("NO")
		}
	}
}
