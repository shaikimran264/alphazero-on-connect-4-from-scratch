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

# Step 18 - init_policy_head
import torch
import torch.nn as nn

def init_policy_head(hidden_channels=16, num_columns=7):
    """Return an nn.Module mapping (B, hidden_channels, 6, 7) -> (B, num_columns) logits."""
    # TODO: build a small policy head that projects backbone features to column logits
    # pass
    conv=nn.Conv2d(in_channels=hidden_channels,out_channels=1,kernel_size=3,padding='same')
    flattened=torch.nn.Flatten()
    output=torch.nn.Linear(6*7,num_columns)

    return nn.Sequential(conv,flattened,output)

# Step 19 - init_value_head
import torch
import torch.nn as nn

def init_value_head(hidden_channels=16):
    """Return an nn.Module mapping (B, hidden_channels, 6, 7) -> (B, 1) in (-1, 1)."""
    # TODO: build a value head that collapses backbone features to a single bounded scalar per board.
    # pass
    conv=nn.Conv2d(in_channels=hidden_channels,out_channels=1,kernel_size=3,padding='same')
    flattened=torch.nn.Flatten()
    output=torch.nn.Linear(6*7,1)
    act=nn.Tanh()

    return nn.Sequential(conv,flattened,output,act)

# Step 20 - build_policy_value_net
import torch
import torch.nn as nn

class network(nn.Module):
    def __init__(self,in_channels,hidden_channels,num_columns):
        super().__init__()
        self.backbone=init_conv_backbone(in_channels=in_channels,hidden_channels=hidden_channels)
        self.policy_head=init_policy_head(hidden_channels=hidden_channels,num_columns=num_columns)
        self.value_head=init_value_head(hidden_channels=hidden_channels)
    def forward(self,x):
        out_1=self.backbone(x)
        out_2=self.policy_head(out_1)
        out_3=self.value_head(out_1)

        return out_2,out_3
def build_policy_value_net(in_channels=2, hidden_channels=16, num_columns=7):
    """Compose backbone + policy head + value head into one nn.Module."""
    # TODO: build an nn.Module with backbone, policy_head, value_head attributes
    # pass

    return network(in_channels,hidden_channels,num_columns)

# Step 21 - policy_value_forward
import torch
import torch.nn as nn

def policy_value_forward(net, encoded_board):
    """Run encoded_board (B,2,6,7) through net and return (logits, value)."""
    # TODO: call the network on the encoded board and return its two outputs
    # pass
    logits,value=net(encoded_board)

    return logits,value

# Step 22 - action_mask
import numpy as np

def action_mask(board):
    # TODO: return a length-7 boolean mask, True where the column is legal
    # pass
    cols=valid_moves(board)
    valid_cols=valid_moves(board)
    out=np.zeros(7,dtype=bool)
    for i in range(7):
        if i in valid_cols:
            out[i]=1
    
    return out

# Step 23 - masked_policy_logits
import torch

def masked_policy_logits(logits, mask):
    """Set logits at illegal columns to -inf.

    logits: torch.Tensor of shape (..., 7)
    mask:   bool array/tensor of shape (7,), True = legal
    returns: torch.Tensor of same shape as logits
    """
    # TODO: replace logits at illegal columns with negative infinity
    # pass

    mask = torch.as_tensor(mask, device=logits.device, dtype=torch.bool)
    
    new_logits=logits.clone()
    for i in range(len(mask)):
        if not mask[i]:
            new_logits[...,i]=float('-inf')
    
    return new_logits

# Step 24 - masked_log_softmax
import torch

def masked_log_softmax(logits, mask):
    """Log-softmax of logits with illegal columns (mask=False) forced to -inf."""
    # TODO: mask out illegal columns, then apply log-softmax over the last dim.
    # pass
    new_logits=masked_policy_logits(logits,mask)

    fun=torch.nn.LogSoftmax()

    probs=fun(new_logits)

    return probs

# Step 25 - sample_action_from_policy
import torch

def sample_action_from_policy(logits, mask, temperature=1.0):
    """Sample a legal column from a tempered masked categorical policy."""
    # TODO: scale logits by temperature, mask illegal columns, sample one index
    # pass
    temp_logits=logits/temperature

    log_probs=masked_log_softmax(temp_logits, mask)

    probs=torch.exp(log_probs)

    col = torch.multinomial(probs,1)

    return col.item()

# Step 26 - greedy_action_from_policy
import torch

def greedy_action_from_policy(logits, mask):
    """Return the argmax legal column index from masked policy logits."""
    # TODO: mask out illegal columns then return the argmax as a python int
    # pass

    # temp_logits=logits/temperature

    log_probs=masked_log_softmax(logits, mask)

    probs=torch.exp(log_probs)

    col = torch.argmax(probs,dim=-1)

    return col.item()

# Step 27 - make_mcts_node
def make_mcts_node(prior=0.0, parent=None):
    # TODO: build a dict with prior, visit_count, value_sum, children, and parent fields.
    # pass

    mcts_node = {'prior': prior, 'visit_count': 0, 'value_sum': 0.0, 'children': {}, 'parent': parent}

    return mcts_node

# Step 28 - node_q_value
def node_q_value(node):
    # TODO: return the mean value Q = value_sum / visit_count, or 0.0 if visit_count == 0
    # pass
    if node['visit_count']==0:
        return 0.0
        
    val=node['value_sum']/node['visit_count']

    return val

# Step 29 - ucb_score
import math

def ucb_score(parent, child, c_puct=1.5):
    # TODO: return Q(child) + c_puct * prior * sqrt(N_parent) / (1 + N_child)
    # pass
    q_value=node_q_value(child)

    score=q_value + c_puct * child['prior'] * (math.sqrt(parent['visit_count']) / (1 + child['visit_count']))

    return score

# Step 30 - select_best_child
def select_best_child(node, legal_actions, c_puct=1.5):
    # TODO: return (action, child) maximizing PUCT among legal children of node.
    # pass
    
    maxi=float('-inf')
    action=None

    for act in legal_actions:
        score=ucb_score(node, node['children'][act], c_puct=c_puct)
        if score > maxi:
            maxi=score
            action=act
            
    
    return (action,node['children'][action])

# Step 31 - select_leaf
def select_leaf(root, c_puct):
    # TODO: walk down the MCTS tree picking the best PUCT child until a non-expanded node is reached
    # pass
    
    node=root
    while node.get("is_expanded", False):
        legal_actions=node['children'].keys()
        action,best_child=select_best_child(node, legal_actions, c_puct=c_puct)
        node=best_child
    
    return node

# Step 32 - evaluate_with_network
def evaluate_with_network(net, state, to_play):
    # TODO: run net on encoded state and return (masked priors np.ndarray (7,), value float)
    # pass
    net=net.eval()
    board=state
    encoded_board = encode_board(state, to_play)

    encoded_board = torch.tensor(encoded_board,dtype=torch.float32).unsqueeze(0) # batch of 1
    with torch.no_grad():
        logits,val=net(encoded_board)
    
    mask=action_mask(board)

    log_probs = masked_log_softmax(logits,mask)

    probs=torch.exp(log_probs)

    priors=probs.squeeze(0).cpu().numpy()

    return priors,val.item()

# Step 33 - expand_node
def expand_node(node, priors):
    # TODO: attach a child node for every legal move with the corresponding network prior
    # pass
    leaf=node
    board=node['board']
    player=node['to_play']

    valid_cols=valid_moves(board)  # valid cols or actions
    for i in range(len(valid_cols)):
        new_board = drop_piece(board, valid_cols[i], player)
        child = make_mcts_node(priors[valid_cols[i]],parent=node)
        child['board']=new_board

        child['to_play']=other_player(player)

        node['children'][valid_cols[i]]=child
    
    node['is_expanded']=True

    return node

# Step 34 - backup_value
def backup_value(leaf, value):
    # TODO: walk from leaf up through parents, updating visits and value_sum with alternating signs
    # pass
    # node=leaf
    
    while(leaf):
        parent=leaf['parent']
        leaf['value_sum'] += value
        leaf['visit_count']+=1
        leaf['visits']=leaf['visit_count']
        leaf=parent
        value = value*(-1)

# Step 35 - run_one_simulation
def run_one_simulation(root, net, c_puct):
    # TODO: run one MCTS simulation: select a leaf, evaluate, expand if non-terminal, backup.
    # pass
    if "is_expanded" not in root:
      root["is_expanded"] = False

    leaf = select_leaf(root, c_puct)

    done,winner = is_terminal(leaf['board'])

    if not done:
       priors,value = evaluate_with_network(net, leaf['board'], leaf['to_play'])
       expand_node(leaf, priors)
    else:
        if winner == 0:
            value = 0.0          # draw
        elif winner == leaf["to_play"]:
            value = 1.0
        else:
            value = -1.0

        
    backup_value(leaf, value)

# Step 36 - run_mcts
def run_mcts(state, to_play, net, num_simulations, c_puct):
    # TODO: build a fresh root for (state, to_play) and run num_simulations PUCT simulations
    # pass
    root = make_mcts_node()
    root['board']=state.copy()   # .copy(),Because MCTS should store a snapshot of the board. If later you modify the original board, the tree should not change.
    root['to_play']=to_play

    for _ in range(num_simulations):
      run_one_simulation(root, net, c_puct)
    
    return root

# Step 37 - visit_count_policy
def visit_count_policy(root, temperature=1.0):
    # TODO: convert root child visit counts into a length-7 probability vector over columns
    # pass
    acts=root['children'].keys()
    total=0
    probs=[0.0]*7
    
    # No children -> uniform distribution
    if len(acts)==0:
        return [1/7]*7

    if temperature == 0:
        maxi=float('-inf')
        best_act=None
        for act in acts:
            count=root['children'][act]['visit_count']
            if count > maxi:
                best_act=act
                maxi=count
        
        probs[best_act]=1.0
        return probs


    for act in acts:
        total+=(root['children'][act]['visit_count'])**(1/temperature)
    
    if total == 0:
        legal_actions=list(root['children'].keys())
        prob=1/len(legal_actions)

        for act in legal_actions:
            probs[i]=prob
        
        return probs
    
    for act in acts:
        probs[act]=(((root['children'][act]['visit_count'])**(1/temperature)) / total)
    
    return probs

# Step 38 - mcts_choose_action
def mcts_choose_action(state, to_play, net, num_simulations, c_puct, temperature=1.0):
    # TODO: Run MCTS at the given state and return (action, visit-count policy vector).
    # pass
    root  = run_mcts(state, to_play, net, num_simulations, c_puct)
    probs = visit_count_policy(root, temperature=temperature)
    tensors=torch.tensor(probs,dtype=torch.float32)
    act = torch.multinomial(tensors,1)

    return act.item(),np.array(probs)

# Step 39 - record_self_play_step
def record_self_play_step(history, board, policy, to_play):
    # TODO: append a dict with 'board', 'policy', 'to_play' to history and return history
    # pass
    bo=board.copy()
    po=policy.copy()
    # tp=to_play.copy()

    ans={'board':bo,'policy':po,'to_play':to_play}

    history.append(ans)

    return history

# Step 40 - play_self_play_game
def play_self_play_game(net, num_simulations, c_puct, temperature=1.0):
    # TODO: play one Connect-4 game with both sides driven by MCTS, recording every step
    # pass
    board = make_empty_board()
    to_play=1
    done=False
    history=[]

    while not done:
       act,probs =  mcts_choose_action(state=board, to_play=to_play, net=net, num_simulations=num_simulations, c_puct=c_puct, temperature=temperature)
    
       record_self_play_step(history, board=board, policy=probs, to_play=to_play)
       new_board,done,winner,next_player = step_env(board=board, column=act, player=to_play)
       to_play = next_player
       board=new_board

    return history,winner

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

