package main

import (
	"fmt"
)

func bestPalindrome(s []byte, k int) ([]byte, bool) {
	n, cnt, pos_change := len(s), 0, map[int]bool{}
	for i := 0; i < n/2; i++ {
		if s[i] != s[n-i-1] {
			cnt++
			pos_change[i] = true
		}
	}

	if cnt > k {
		return []byte{}, false
	}

	for i := 0; i < n/2; i++ {
		if s[i] != s[n-i-1] {
			if s[i] > s[n-i-1] {
				s[n-i-1] = s[i]
			} else {
				s[i] = s[n-i-1]
			}
		}
	}

	k, i := k-cnt, 0

	for ; k > 0 && i < n/2; i++ {
		_, ok := pos_change[i]
		if ok {
			if s[i] != 9 {
				k -= 1
				s[i], s[n-i-1] = 9, 9
			}
		} else if k >= 2 && s[i] != 9 {
			k -= 2
			s[i], s[n-i-1] = 9, 9
		}
	}

	if k > 0 && n%2 == 1 {
		s[n/2] = 9
	}
	return s, true
}

func main() {
	n, k := 0, 0
	fmt.Scanf("%d %d", &n, &k)
	s := make([]byte, n)
	fmt.Scanf("%s", &s)

	for i := 0; i < n; i++ {
		s[i] -= 48
	}

	res, ok := bestPalindrome(s, k)
	if ok {
		for _, v := range res {
			fmt.Print(v)
		}
		fmt.Println()
	} else {
		fmt.Println(-1)
	}
}
