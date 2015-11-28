package main
import (
	"fmt"
)

func que(arr []int, l, r int)int{
	for p := r - (r & -r); l <= r; r = p{
		q := 0
		if p+1 >= l {
			q = arr[r]
		} else {
			q =
		}

		? T[r] : (p=r-1) + 1;
        if( a[m] < a[q] )
            m = q;
		p -= p & - p
	}
	return 1
}

//int que( int l, int r ) {
//    int p, q, m = 0;
//
//    for( p=r-(r&-r); l<=r; r=p, p-=p&-p ) {
//        q = ( p+1 >= l ) ? T[r] : (p=r-1) + 1;
//        if( a[m] < a[q] )
//            m = q;
//    }
//
//    return m;
//}
//
//void upd( int x ) {
//    int y, z;
//    for( y = x; x <= N; x += x & -x )
//        if( T[x] == y ) {
//            z = que( x-(x&-x) + 1, x-1 );
//            T[x] = (a[z] > a[x]) ? z : x;
//        }
//        else
//            if( a[ T[x] ] < a[ y ] )
//                T[x] = y;
//}
