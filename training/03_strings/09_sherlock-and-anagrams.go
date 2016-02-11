/**
 this is O^3 solution, a better one in O(n^2) exist
 https://www.hackerrank.com/challenges/sherlock-and-anagrams/editorial
 */

package main
import "fmt"

func getMap(str string)[26]int{
	arr := [26]int{}
	for _, v := range(str){
		arr[v - 97]++
	}
	return arr
}

func stringAnalyse(str string)int{
	hash := map[[26]int]int{}
	for i := 0; i <= len(str); i++{
		for j := i + 1; j <= len(str); j++{
			arr := getMap(str[i:j])
			hash[arr]++
		}
	}

	s := 0
	for _, v := range(hash){
		if v > 1{
			s += v * (v - 1) / 2
		}
	}
	return s
}

func main(){
	str, T := "", 0
    fmt.Scanf("%d", &T)
    for T > 0{
        T--
        fmt.Scanf("%s", &str)
        fmt.Println(stringAnalyse(str))
    }
}

