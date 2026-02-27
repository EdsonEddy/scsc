while True:
    try:
        for _ in range( int( input() ) ):
            n, k = map( int, input().split() )

            for i in range( k ):
                sumaDig = ( ( n -1 ) % 9 ) +1
                strN = str(sumaDig) + str( n )
                n = int( strN[:-1] )
            print( n )
    except EOFError:
        break
    except Exception as e:
        break