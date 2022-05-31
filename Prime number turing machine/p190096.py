atimes = int (input("Enter  length of a's : "))
string=""
while(atimes>0):
    string=string+'a'
    atimes=atimes-1

length = len(string) + 2

tape = ['B','B']*length
i = 1
tapehead = 1
for s in string: #loop to place string in tape
    tape[i] = s
    i += 1

state = 0
#assigning characters to variable so that don't have to use characters each time
X, Y, S, B, R, L = 'a', '*', '+', 'B', 'R', 'L' 
oldtapehead = -1
accept = False

def action(input_char, replace_with, move, new_state):
    global tapehead, state
    if tape[tapehead] == input_char:
        tape[tapehead] = replace_with
        state = new_state
        if move == 'L':
            tapehead -= 1
            return True
        elif move == 'R':
            tapehead += 1
            return True
    return False

while(oldtapehead != tapehead): #if tapehead not moving that means terminate Turing machine
    oldtapehead = tapehead
    print(tape , "with tapehead at index", tapehead, "on state" , state)
    
    if state == 0:
        if action(X, X, R, 1)  :
            pass
        
    elif state == 1:
        if action(X, X, R, 2) :
            pass
        
    elif state == 2:
        if action('a', 'a', R, 3) or action(B,B,R,29) :
            pass
            
    elif state == 3:
        if action('a', 'a', R, 4)  or action(B,B,R,29) :
            pass
    
    elif state == 4:
        if action(X, X, R, 5)   :
            pass
        
    elif state == 5:
        if action(X, X,R,6) or action(B,B,R,29) :
            pass
            
    elif state == 6:
        if action(X, X,R,7)  :
            pass
            
    elif state == 7:
        if action(X ,X, R, 30) or action(B,B,R,29) :
            pass
            
    elif state == 8:
        if action(X, X, R, 9) or action(B, B, L, 10) :
            pass        
    elif state == 9:
        if action(X, X, R, 8)   :
            pass        
    elif state == 10:
        if action(X, X, L, 10) or action(B,B,R,11) :
            pass        
    elif state == 11:
        if action(X, X, R, 12) or action(B,B,L,28) :
            pass 
    elif state == 12:
        if action(X, X, R, 13) or action(B,B,L,14) :
            pass 

    elif state == 13:
        if  action(X, X, R, 11) or action(B,B,L,14) :
            pass 
    elif state == 14:
        if action(X, X, L, 14) or action(B,B,R,15) :
            pass
    elif state == 15:
        if action(X, X, R, 16) or action(B, B, L, 28) :
            pass    
    elif state == 16:
        if action(X, X, R, 17) or action(B, B, L, 20)  :
            pass 
    elif state == 17:
        if action(X, X, R, 18) or action(B,B,L,20)  :
            pass
    elif state == 18:
        if action(X, X, R, 19) or action(B,B,L,20):
            pass   

    elif state == 19:
        if action(X, X, R, 15) or action(B,B,L,20)  :
            pass  
    elif state == 20:
        if action(X, X, L, 20) or action(B,B,R,21)  :
            pass 

    elif state == 21:
        if action(X, X, R, 22) or action(B,B,R,28) :
            pass 
    elif state == 22:
        if action(X, X, R, 23) or action(B,B,R,29) :
            pass
    elif state == 23:
        if action(X, X, R, 24) or action(B,B,R,29) :
            pass
    elif state == 24:
        if action(X, X, R, 25) or action(B,B,R,29) :
            pass
    elif state == 25:
        if action(X, X, R, 26) or action(B,B,R,29) :
            pass
    elif state == 26:
        if action(X, X, R, 27) or action(B,B,R,29) :
            pass
    elif state == 27:
        if action(X, X, R, 29)  :
            pass 
   
    elif state == 30:
        if action(X, X, L, 30) or action(B,B,R,9)  :
            pass 

    elif state == 28:
        accept=False

    elif state == 29:
        accept=True
   
    
  

    else:
        accept = False
        
            
if accept:
    print("String accepted on state = ", state)
else:
    print("String not accepted on state = ", state)