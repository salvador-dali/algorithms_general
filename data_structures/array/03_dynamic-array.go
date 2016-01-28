package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
    "fmt"
)

func main(){
	N, Q, reader := 0, 0, bufio.NewReader(os.Stdin)
    hash, lastAns := map[int] []int{}, 0
    fmt.Scanf("%d %d", &N, &Q)
    for ; Q > 0; Q--{
		text, _ := reader.ReadString('\n')
		arr := []int{}
		for _, v := range (strings.Fields(text)) {
			num, _ := strconv.Atoi(v)
			arr = append(arr, num)
		}
        
        pos := (arr[1] ^ lastAns) % N
		if arr[0] == 1 {
            hash[pos] = append(hash[pos], arr[2])
        } else {
            lastAns = hash[pos][arr[2] % len(hash[pos])]
            fmt.Println(lastAns)
        }
    }
}
