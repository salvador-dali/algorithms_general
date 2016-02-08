// https://www.hackerrank.com/challenges/song-of-pi
package main
import (
	"fmt"
	"bufio"
    "os"
	"strings"
)

func readManyStrings() []string {
	var T int
	fmt.Scanf("%d", &T)

	scanner, arr_strings := bufio.NewScanner(os.Stdin), []string{}
	for T > 0 {
		T--
		scanner.Scan()
		arr_strings = append(arr_strings, scanner.Text())
	}
	return arr_strings
}

func checkValidity(sentence string)bool{
	words := strings.Fields(sentence)
	lengths := []int{3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 3}
	for i := 0; i < len(words); i++{
		if len(words[i]) != lengths[i]{
			return false
		}
	}
	return true
}

func main(){
	strings := readManyStrings()
	for _, v := range(strings){
		if checkValidity(v){
			fmt.Println("It's a pi song.")
		} else {
			fmt.Println("It's not a pi song.")
		}
	}
}
