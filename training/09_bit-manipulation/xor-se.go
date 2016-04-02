//https://www.hackerrank.com/challenges/xor-se
package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getValue(n uint64) uint64 {
	d := int(n % 8)
	if d < 2 {
		return n
	} else if d < 4 {
		return 2
	} else if d < 6 {
		return n + 2
	}
	return 0
}

func writeManyNumbers(numbers []uint64) {
	var buffer bytes.Buffer
	for _, v := range numbers {
		buffer.WriteString(strconv.FormatUint(v, 10) + "\n")
	}
	fmt.Print(buffer.String())
}

func main() {
	T := 0
	fmt.Scanf("%d", &T)

	reader, res := bufio.NewReader(os.Stdin), make([]uint64, T)
	for i := 0; i < T; i++ {
		text, _ := reader.ReadString('\n')
		tmp := [2]uint64{0, 0}
		for pos, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			tmp[pos] = uint64(num)
		}
		res[i] = getValue(tmp[0]-1) ^ getValue(tmp[1])
	}
	writeManyNumbers(res)
}
