/*
https://www.hackerrank.com/challenges/half
This is a nim_half game from games.go
with the only difference that we need to find the smallest element
*/
package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func writeManyNumbers(numbers []int) {
	var buffer bytes.Buffer
	for _, v := range numbers {
		buffer.WriteString(strconv.Itoa(v) + "\n")
	}
	fmt.Print(buffer.String())
}

var breakpoints = []int{2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912}
var grades = []int{1, 2, 7, 8, 4, 5, 127, 128, 121, 125, 97, 113, 64, 65, 32767, 32768, 32761, 32765, 32737, 32753, 32641, 32705, 32257, 32513, 30721, 31745, 24577, 28673, 16384, 16385}

func main() {
	T, reader := 0, bufio.NewReader(os.Stdin)
	fmt.Scanf("%d", &T)
	res := make([]int, T)
	for i := 0; i < T; i++ {
		text, _ := reader.ReadString('\n')
		num, _ := strconv.Atoi(strings.TrimRight(text, "\n"))
		if num%2 == 1 {
			res[i] = 1
		} else {
			val := sort.Search(len(breakpoints), func(i int) bool { return breakpoints[i] >= num }) - 1
			res[i] = grades[val]
		}
	}
	writeManyNumbers(res)
}
