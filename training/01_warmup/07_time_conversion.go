// https://www.hackerrank.com/challenges/time-conversion
package main
import (
	"fmt"
	"strconv"
)

func superFunc(s string)string{
	if s == "12:00:00AM"{
		return "00:00:00"
	}

	if s == "12:00:00PM"{
		return "12:00:00"
	}

	hour, _ := strconv.Atoi(s[0:2])
	minute := s[3:5]
	second := s[6:8]
	t := string(s[8])

	if t == "P"{
		if hour == 12 {
			return s[0:8]
		}
		return strconv.Itoa(hour + 12) + ":" + minute + ":" + second
	} else {
		if hour == 12 {
			return "00:" + minute + ":" + second
		}
		return s[0:8]
	}
	return ""
}

func main(){
    s := ""
    fmt.Scanf("%s", &s)
	fmt.Println(superFunc(s))
}
