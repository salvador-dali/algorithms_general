// https://www.hackerrank.com/challenges/balanced-parentheses
package main
import (
	"fmt"
    "bufio"
    "os"
    "strings"
)

func isParenthesis(s string) bool{
	lookup := map[byte]byte{
		')': '(',
		']': '[',
		'}': '{',
	}

	stack := []byte{}
	for _, v := range s {
		if lookup[byte(v)] == 0 {
			stack = append(stack, byte(v))
		} else {
            if len(stack) == 0 {
                return false
            }
			el := stack[len(stack) - 1]
			if el != lookup[byte(v)] {
				return false
			}
			stack = stack[:len(stack) - 1]
		}
	}
	return len(stack) == 0
}

func main(){
	reader, T := bufio.NewReader(os.Stdin), 0
	fmt.Scanf("%d", &T)
	for ; T > 0; T-- {
		s, _ := reader.ReadString('\n')
        if isParenthesis(strings.TrimSpace(s)) {
            fmt.Println("YES")
        } else {
            fmt.Println("NO")
        }
	}
}
