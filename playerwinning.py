class Play:

    def __init__(self):
        pass

    #... method finds out if player is winnig on next move or not 
    #.. if winning returns a tuple("win", move) else returns tuple("no", None)
    def is_player_win(self, A):
	# all possible cases of winning
        x_win = [ {1,2,3}, {4,5,6}, {7,8,9}, {1,4,7}, {2,5,8}, {3,6,9}, {1,5,9}, {3,5,7}  ]
        for B in x_win:
            if len(B-A)==1:
                print "win_move ", list(B-A)[0]
                return ("win", list(B-A)[0])
            print "\n"
        return ("no", None)




if __name__ == "__main__":
    obj = Play()
    (player_win, move ) = obj.is_player_win({1,5, 8})  #..passing previous move of a player
    print "player winnning =", player_win
    print "move", move


