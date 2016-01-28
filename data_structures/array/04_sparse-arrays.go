package main
import (
	"fmt"
	"bufio"
	"os"
    "strings"
    "strconv"
)

func main(){
	reader, hash, T := bufio.NewReader(os.Stdin), map [string]int{}, 0
	fmt.Scanf("%d", &T)
	for ; T > 0; T-- {
		text, _ := reader.ReadString('\n')
		hash[strings.TrimSpace(text)]++
	}
	text, _ := reader.ReadString('\n')

    T, _ = strconv.Atoi(strings.TrimSpace(text))
	for ; T > 0; T-- {
		text, _ := reader.ReadString('\n')
        fmt.Println(hash[strings.TrimSpace(text)])
	}
}
