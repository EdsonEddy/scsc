a, b = map( int, input().split() )
ls = [ _ for _ in list( map( int, input().split() )) if a <= _ <= b  ]

print( sum(ls) )