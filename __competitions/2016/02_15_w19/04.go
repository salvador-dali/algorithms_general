package main
import (
	"fmt"
	"bufio"
	"os"
	"strconv"
	"strings"
)

func readArray() []uint64 {
	reader, arr, T := bufio.NewReader(os.Stdin), []uint64{}, 0
	fmt.Scanf("%d", &T)
	text, _ := reader.ReadString('\n')
	for _, v := range strings.Fields(text) {
		num, _ := strconv.Atoi(v)
		arr = append(arr, uint64(num))
	}
	return arr
}

func minArr(arr []uint64) uint64{
	min := uint64(1844674407370955161)
	for _, v := range arr {
		if v < min {
			min = v
		}
	}
	return min
}

func bruteforce2(arr []uint64) uint64{
    ans, mod := uint64(0), uint64(1000000007)
	for a := 0; a < len(arr); a++{
		for b := a; b < len(arr); b++{
			el1 := minArr(arr[a:b + 1])
			for c := b + 1; c < len(arr); c++{
				for d := c; d < len(arr); d++{
                    v := uint64(0)
                    s := minArr(arr[c:d + 1])

                    if s < el1 {
                        v = s
                    } else {
                        v = el1
                    }
					ans = (ans + v) % mod
				}
			}
		}
	}
	return ans
}

func main(){
//    arr := readArray()
	arr := []uint64{3, 2, 1}
    fmt.Println(bruteforce2(arr))
}
