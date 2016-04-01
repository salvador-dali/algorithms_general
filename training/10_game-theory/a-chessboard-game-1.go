//https://www.hackerrank.com/challenges/a-chessboard-game-1
package main
import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
)

func main() {
	T, reader := 0, bufio.NewReader(os.Stdin)
	fmt.Scanf("%d", &T)
	for i := 0; i < T; i++ {
		text, _ := reader.ReadString('\n')
		tmp := [2]int{0, 0}
		for pos, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			tmp[pos] = num
		}
		x, y := tmp[0] - 1, tmp[1] - 1

		if x % 4 < 2 && y % 4 < 2{
			fmt.Println("Second")
		} else {
			fmt.Println("First")
		}
	}
}
