package main

import (
	"testing"
	"fmt"
)

func divisorSieve_1(n uint64) []uint64 {
	sieve := []uint64{}
	for i := uint64(0); i < n+1; i++ {
		if i % 2 == 0 {
			sieve = append(sieve, 2)
		} else {
			sieve = append(sieve, 0)
		}
	}
	sieve[0] = 0

	p := uint64(3)
	for p*p <= n {
		for i := p; i <= n; i += p {
			if sieve[i] == 0 {
				sieve[i] = p
			}
		}

		for p < n+1 && sieve[p] > 0 {
			p += 2
		}
	}

	for p < n+1 {
		if sieve[p] == 0 {
			sieve[p] = p
		}
		p += 2
	}
	return sieve
}

func divisorSieve_2(n uint64) []uint64 {
	sieve := make([]uint64, n + 1)
	for i := uint64(0); i < n+1; i++ {
		if i % 2 == 0 {
			sieve[i] = 2
		}
	}
	sieve[0] = 0

	p := uint64(3)
	for p*p <= n {
		for i := p; i <= n; i += p {
			if sieve[i] == 0 {
				sieve[i] = p
			}
		}

		for p < n+1 && sieve[p] > 0 {
			p += 2
		}
	}

	for p < n+1 {
		if sieve[p] == 0 {
			sieve[p] = p
		}
		p += 2
	}
	return sieve
}

func TestSievesEqual(t *testing.T) {
	n := uint64(40)
	res1 := divisorSieve_1(n)
	res2 := divisorSieve_2(n)
	fmt.Println(res1)
	fmt.Println(res2)
}

func BenchmarkSieve1_tiny(b *testing.B) {
	n := uint64(1000)
	for i := 0; i < b.N; i++ {
		divisorSieve_1(n)
	}
}

func BenchmarkSieve2_tiny(b *testing.B) {
	n := uint64(1000)
	for i := 0; i < b.N; i++ {
		divisorSieve_2(n)
	}
}

func BenchmarkSieve1_huge(b *testing.B) {
	n := uint64(100000000)
	for i := 0; i < b.N; i++ {
		divisorSieve_1(n)
	}
}

func BenchmarkSieve2_huge(b *testing.B) {
	n := uint64(100000000)
	for i := 0; i < b.N; i++ {
		divisorSieve_2(n)
	}
}

//10^8 takes 1.5 seconds
