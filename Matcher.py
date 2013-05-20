

def check_row(player_moves):
    '''
	    matches player postion on board to all winning row combinations ([1,2,3], [4,5,6], [7,8,9])
	    returns the res(0,1) as a "win" variable
    '''
    print "....................... row check"
    L=player_moves
    row_mins = [1,4,7]
    res=0
    for x in row_mins:
        if x in L:
	    print x, "in",  L
            res = poi(L, x, 1)
            if res==1:
                return  res
        else:
            print x, "not in",  L
    return res



def check_col(player_moves):
    '''
	matches player postion on board to all winning column combinations ([1,4,7], [2,5,8], [3,6,9]
	returns the res(0,1) as a "win" variable
    '''
    print "....................... col check"
    L=player_moves
    col_mins = [1,2,3]
    res=0
    for x in col_mins:
        if x in L:
	    print x, "in",  L
            res = poi(L, x, 3)
            if res==1:
                return  res
        else:
            print x, "not in",  L
    return res



def check_leftDaigonal(L):
    '''
	matches player postion on board to winning left diagonal[1,5,9] position
    	returns the res(0,1) as a "win" variable
    '''

    print"....................... left_diagonal check"
    leftdiag_mins = [1]
    res=0
    for x in leftdiag_mins:
        if x in L:
	    print x, "in",  L
            res=poi(L, x, 4)
            if res==1:
                return res
        else:
            print x, "not in ", L
    return res




def check_rightDaigonal(L):
    '''
	matches player postion on board to winning right diagonal[3, 5, 7] position.
	returns the res(0,1) as a "win" variable.
    '''
    print"....................... right_diagonal check"
    rightdiag_mins = [3]
    res=0
    for x in rightdiag_mins:
        if x in L:
	    print x, "in",  L
            res=poi(L, x, 2)
            if res==1:
                return res
        else:
            print x, "not in ", L
    return res



def poi(L, min_ele, factor):
    '''
	find out winning postions of board for given dimenstion (row,column, diagonals)
    '''
    print "poi()...", min_ele
    is_match=0
    if(min_ele+factor) in L:
        if(min_ele+(factor*2)) in L:
            print "all three are there ", (min_ele, min_ele+factor, min_ele+(factor*2))
            is_match = 1
        else:
            print "3rd element not there"
    else:
        print "2nd element not there"
    return is_match
	
