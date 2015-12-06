// https://www.hackerrank.com/challenges/caesar-cipher-1
package main
import (
	"fmt"
)

func main(){
	tmp, s, k, out := 0, "", uint8(0), ""
    fmt.Scanf("%d", &tmp)
	fmt.Scanf("%s", &s)
	fmt.Scanf("%d", &k)
	for i := 0; i < len(s); i++{
		char := s[i]
		if char >= 65 && char <= 90{
			char += k
			for char > 90{
				char -= 26
			}
		} else if char >= 97 && char <= 122{
			char += k
			for char > 122{
				char -= 26
			}
		}
		out += string(char)
	}
	
	fmt.Println(out)
}
