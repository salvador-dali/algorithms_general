go test -bench=. -benchmem -benchtime 5s

### Appending vs pre-allocating

**allocations_test.go**

Pre-allocating at least 4 times faster with any size.

    BenchmarkArr1_tiny-4    	20000000	       409 ns/op	     256 B/op	       5 allocs/op
    BenchmarkArr2_tiny-4    	100000000	        83.9 ns/op	      80 B/op	       1 allocs/op
    BenchmarkArr1_small-4   	10000000	      1189 ns/op	    2048 B/op	       8 allocs/op
    BenchmarkArr2_small-4   	20000000	       308 ns/op	     896 B/op	       1 allocs/op
    BenchmarkArr1_medium-4  	  100000	     91816 ns/op	  385793 B/op	      20 allocs/op
    BenchmarkArr2_medium-4  	  300000	     21367 ns/op	   81920 B/op	       1 allocs/op
    BenchmarkArr1_huge-4    	   10000	   1131859 ns/op	 4653871 B/op	      30 allocs/op
    BenchmarkArr2_huge-4    	   30000	    211296 ns/op	  802818 B/op	       1 allocs/op
    BenchmarkArr1_enormous-4	     500	  12020731 ns/op	45188699 B/op	      53 allocs/op
    BenchmarkArr2_enormous-4	    3000	   2164440 ns/op	 8003655 B/op	       2 allocs/op
    
### Decoding json partially

**json_decode_test.go**

If you need only couple of fields from a json to know where to move it, it is faster to partially
decode it. Takes 10 times less allocations, 5 times less B/op and at least 3 times faster.

    Benchmark_json1_small-4 	  500000	     16303 ns/op	    3406 B/op	     100 allocs/op
    Benchmark_json2_small-4 	 2000000	      4837 ns/op	     592 B/op	      10 allocs/op
    Benchmark_json1_medium-4	  200000	     32687 ns/op	    6250 B/op	     175 allocs/op
    Benchmark_json2_medium-4	 1000000	     11898 ns/op	    1216 B/op	      12 allocs/op
    
