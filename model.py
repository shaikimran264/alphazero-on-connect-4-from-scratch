"""
AlphaZero on Connect-4 from Scratch

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - make_empty_board
import numpy as np

def make_empty_board():
    """Return a 6x7 integer numpy array of zeros representing an empty Connect-4 board."""
    # TODO: create a 6x7 integer array of zeros and return it
    # pass
    array=np.zeros((6,7),dtype=int)
    return array

# Step 2 - column_top_row
def column_top_row(board, column):
    """Return the lowest empty row in `column`, or -1 if the column is full."""
    # TODO: scan the column from the bottom up and return the first empty row index
    # pass

    #In Connect Four, a column is playable only if the top cell is empty.
    if board[0][column]!=0:
        return -1
        
    for i in range(len(board)-1,-1,-1):
        if(board[i][column]==0):
            return i
    
    return -1

# Step 3 - drop_piece
def drop_piece(board, column, player):
    # TODO: place `player` in the lowest empty row of `column` and return the new board
    # pass
    landing_row=column_top_row(board,column)
    if landing_row == -1:
        raise ValueError("Column is full")
    
    new_board=board.copy()
    new_board[landing_row][column]=player

    return new_board

# Step 4 - column_full
import numpy as np

def column_full(board, column):
    """Return True if `column` has no empty rows left."""
    # TODO: check whether the column can still accept a piece
    # pass
    row=column_top_row(board,column)
    if row == -1:
        return True
    return False

# Step 5 - valid_moves
def valid_moves(board):
    # TODO: return a list of column indices that still have at least one empty row
    # pass
    valid_cols=[]
    for c in range(len(board[0])):
        row=column_top_row(board,c)
        if row !=-1:
            valid_cols.append(c)
    
    return valid_cols

# Step 6 - four_in_a_row_horizontal
def four_in_a_row_horizontal(board):
    # TODO: scan every row for four consecutive matching non-zero pieces horizontally
    # pass
    for i in range(len(board)):

        for j in range(len(board[i])-3):
            count1=0
            count2=0      
            for k in range(j,j+4):

                if board[i][k]==1:
                    count1+=1
                elif board[i][k]==2:
                    count2+=1

            if count1==4:
                return 1
            if count2==4:
                return 2
    
    return 0

# Step 7 - four_in_a_row_vertical
def four_in_a_row_vertical(board):
    # TODO: scan every column for four consecutive matching non-zero pieces vertically
    # pass
    
    for i in range(len(board[0])):

        for j in range(len(board)-3):
            count1=0
            count2=0      
            for k in range(j,j+4):

                if board[k][i]==1:
                    count1+=1
                elif board[k][i]==2:
                    count2+=1

            if count1==4:
                return 1
            if count2==4:
                return 2
    
    return 0

# Step 8 - four_in_a_row_diagonal_down_right
def four_in_a_row_diagonal_down_right(board):
    # TODO: scan every down-right diagonal of the 6x7 board for four matching non-zero pieces
    # pass
    # ro=-1
    for i in range(len(board[0])):
        # ro+=1
        row=0
        # col=i
        coli=i

        count_1=0
        count_2=0

        index_count=0

        while(row < len(board) and coli < len(board[0])):
            if board[row][coli]==1:
                count_1+=1
                count_2=0
            elif board[row][coli]==2:
                count_2+=1
                count_1=0
            else:
                count_1=0
                count_2=0
            
            # index_count+=1

            # if index_count==4:
            if count_1==4:
                    return 1
            if count_2==4:
                    return 2
                
                # index_count=0
            
            row+=1
            coli+=1
    
    # Start from left column (except top-left)
    for i in range(1,len(board)):
        row=i
        coli=0

        count_1=0
        count_2=0

        index_count=0

        while(row < len(board) and coli < len(board[0])):
            if board[row][coli]==1:
                count_1+=1
                count_2=0
            elif board[row][coli]==2:
                count_2+=1
                count_1=0
            else:
                count_1=0
                count_2=0
            
            # index_count+=1

            # if index_count==4:
            if count_1==4:
                return 1
            if count_2==4:
                return 2
                
                # index_count=0
            
            row+=1
            coli+=1


    
    return 0

# Step 9 - four_in_a_row_diagonal_up_right
def four_in_a_row_diagonal_up_right(board):
    # TODO: scan every up-right diagonal for four consecutive matching non-zero pieces
    # pass
    rows=len(board)
    cols=len(board[0])

    for i in range(rows):

        row=rows-1
        coli=i

        count_1=0
        count_2=0

        while(row >= 0 and coli < len(board[0])):
            if board[row][coli]==1:
                count_1+=1
                count_2=0
            elif board[row][coli]==2:
                count_2+=1
                count_1=0
            else:
                count_1=0
                count_2=0
            
            # index_count+=1

            # if index_count==4:
            if count_1==4:
                    return 1
            if count_2==4:
                    return 2
                
                # index_count=0
            
            row-=1
            coli+=1
    
    # Start from left column (except top-left)
    for i in range(rows-2,-1,-1):
        row=i
        coli=0

        count_1=0
        count_2=0


        while(row >= 0 and coli < len(board[0])):
            if board[row][coli]==1:
                count_1+=1
                count_2=0
            elif board[row][coli]==2:
                count_2+=1
                count_1=0
            else:
                count_1=0
                count_2=0
            
            if count_1==4:
                return 1
            if count_2==4:
                return 2
                
                # index_count=0
            
            row-=1
            coli+=1


    
    return 0

# Step 10 - check_winner
import numpy as np

def check_winner(board):
    """Return 1 or 2 if that player has four in a row, else 0."""
    # TODO: combine the four direction scans and return the first non-zero result
    # pass
    row_hor=four_in_a_row_horizontal(board)
    if row_hor !=0 :
        return row_hor

    row_ver=four_in_a_row_vertical(board)
    if row_ver !=0:
        return row_ver

    row_diag_down_right=four_in_a_row_diagonal_down_right(board)
    if row_diag_down_right !=0:
        return row_diag_down_right
    
    row_diag_up_right=four_in_a_row_diagonal_up_right(board)
    if row_diag_up_right !=0:
        return row_diag_up_right
    
    return 0

# Step 11 - board_is_full
def board_is_full(board):
    # TODO: return True when no column has an empty slot left
    # pass
    valid=valid_moves(board)

    if len(valid) ==0:
        return True
    
    return False

# Step 12 - is_terminal
def is_terminal(board):
    # TODO: return (done, winner) using check_winner and board_is_full.
    # pass

    done=False
    winner=check_winner(board)

    if winner!=0:
        return (True,winner)


    if board_is_full(board):
        done=True
        winner=check_winner(board)
        return (done,winner)
    
    return (done,winner)

# Step 13 - other_player
def other_player(player):
    # TODO: return the opponent's player code (1 <-> 2)
    # pass
    if player==1:
        return 2
    return 1

# Step 14 - step_env
def step_env(board, column, player):
    # TODO: drop piece for player, then return (new_board, done, winner, next_player).
    # pass
    new_board=drop_piece(board,column,player)
    done,winner=is_terminal(new_board)
    next_player=other_player(player)

    return (new_board,done,winner,next_player)

# Step 15 - encode_board
import torch
import numpy as np
def encode_board(board, current_player):
    """Encode a 6x7 board as a (2, 6, 7) float32 tensor from current_player's view."""
    # TODO: build two binary planes (current player, opponent) and stack them
    # pass
    opponent=other_player(current_player)
    current_board=np.zeros((6,7),dtype=int)
    opponent_board=np.zeros((6,7),dtype=int)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==current_player:
                current_board[i][j]=1.0
            elif board[i][j]==opponent:
                opponent_board[i][j]=1.0
    
    # current_board = torch.tensor(current_board,dtype=torch.float32)
    # opponent_board = torch.tensor(opponent_board,dtype=torch.float32)

    # # final_result=torch.stack((current_board,opponent_board),dim=0)
    # final_result=torch.concat((current_board.unsqueeze(0),opponent_board.unsqueeze(0)),dim=0)
    
    final_result=np.stack((current_board,opponent_board),axis=0).astype(np.float32)

    return final_result

# Step 16 - board_to_torch_tensor
import torch
def board_to_torch_tensor(board, current_player):
    # TODO: encode the board and return it as a float32 torch tensor of shape (1, 2, 6, 7).
    # pass
    encoded_board=encode_board(board,current_player)

    tensor=torch.tensor(encoded_board,dtype=torch.float32)
    tensor=tensor.unsqueeze(0)
    return tensor

# Step 17 - init_conv_backbone
def init_conv_backbone(in_channels=2, hidden_channels=16):
    # TODO: Build a small convolutional backbone preserving the 6x7 spatial shape.
    # pass

    convo=torch.nn.Conv2d(in_channels=in_channels,out_channels=hidden_channels,kernel_size=3,padding='same')
    act1=nn.ReLU()
    convo_2=torch.nn.Conv2d(in_channels=hidden_channels,out_channels=hidden_channels,kernel_size=3,padding='same')
    return nn.Sequential(convo,act1,convo_2,act1)

# Step 18 - init_policy_head (not yet solved)
# TODO: implement

# Step 19 - init_value_head (not yet solved)
# TODO: implement

# Step 20 - build_policy_value_net (not yet solved)
# TODO: implement

# Step 21 - policy_value_forward (not yet solved)
# TODO: implement

# Step 22 - action_mask (not yet solved)
# TODO: implement

# Step 23 - masked_policy_logits (not yet solved)
# TODO: implement

# Step 24 - masked_log_softmax (not yet solved)
# TODO: implement

# Step 25 - sample_action_from_policy (not yet solved)
# TODO: implement

# Step 26 - greedy_action_from_policy (not yet solved)
# TODO: implement

# Step 27 - make_mcts_node (not yet solved)
# TODO: implement

# Step 28 - node_q_value (not yet solved)
# TODO: implement

# Step 29 - ucb_score (not yet solved)
# TODO: implement

# Step 30 - select_best_child (not yet solved)
# TODO: implement

# Step 31 - select_leaf (not yet solved)
# TODO: implement

# Step 32 - evaluate_with_network (not yet solved)
# TODO: implement

# Step 33 - expand_node (not yet solved)
# TODO: implement

# Step 34 - backup_value (not yet solved)
# TODO: implement

# Step 35 - run_one_simulation (not yet solved)
# TODO: implement

# Step 36 - run_mcts (not yet solved)
# TODO: implement

# Step 37 - visit_count_policy (not yet solved)
# TODO: implement

# Step 38 - mcts_choose_action (not yet solved)
# TODO: implement

# Step 39 - record_self_play_step (not yet solved)
# TODO: implement

# Step 40 - play_self_play_game (not yet solved)
# TODO: implement

# Step 41 - assign_value_targets (not yet solved)
# TODO: implement

# Step 42 - generate_self_play_batch (not yet solved)
# TODO: implement

# Step 43 - value_loss_mse (not yet solved)
# TODO: implement

# Step 44 - policy_loss_cross_entropy (not yet solved)
# TODO: implement

# Step 45 - l2_regularization_loss (not yet solved)
# TODO: implement

# Step 46 - combined_loss (not yet solved)
# TODO: implement

# Step 47 - encode_batch_states (not yet solved)
# TODO: implement

# Step 48 - iterate_minibatches (not yet solved)
# TODO: implement

# Step 49 - training_step (not yet solved)
# TODO: implement

# Step 50 - training_epoch (not yet solved)
# TODO: implement

# Step 51 - self_play_iteration (not yet solved)
# TODO: implement

# Step 52 - train_loop (not yet solved)
# TODO: implement

# Step 53 - random_policy_action (not yet solved)
# TODO: implement

# Step 54 - greedy_agent_action (not yet solved)
# TODO: implement

# Step 55 - play_one_match (not yet solved)
# TODO: implement

# Step 56 - match_win_rate (not yet solved)
# TODO: implement

# Step 57 - evaluate_against_random (not yet solved)
# TODO: implement

