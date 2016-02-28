package main
import "fmt"

func isCorrect(s string) bool {
	m1, m2 := map [rune]int{}, map [int]int{}
	for _, v := range s {
		m1[v]++
	}

	for _, v := range m1 {
		m2[v]++
	}

	if len(m2) == 1 {
		return true
	}

	if len(m2) > 2{
		return false
	}

	for _, v := range m2 {
		if v == 1 {
			return true
		}
	}
	return false
}

func main() {
    s := ""
    fmt.Scanf("%s", &s)
    if isCorrect(s){
        fmt.Println("YES")
    } else {
        fmt.Println("NO")
    }
}
