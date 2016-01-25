package main
import (
	"fmt"
	"os"
	"bufio"
	"strings"
	"strconv"
)

func main(){
	linesNum, reader, M := 6, bufio.NewReader(os.Stdin), [][]int{}
	for i := 0; i < linesNum; i++ {
		text, _ := reader.ReadString('\n')
		line := []int{}
		for _, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			line = append(line, num)
		}
		M = append(M, line)
	}
    
    max := -10 * 36
	for i := 0; i <= 3; i++ {
		for j := 0; j <= 3; j++ {
			attempt := M[i][j] + M[i][j + 1] + M[i][j + 2] + M[i + 1][j + 1] + M[i + 2][j] + M[i + 2][j + 1] + M[i + 2][j + 2]
            if attempt > max{
                max = attempt
            }
		}
	}
    fmt.Println(max)
}
