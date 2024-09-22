import os
import random

grid=[]
words=[]
max_collision=10000

############################################
def init_grid(size=20):
    
    global grid
    
    letters =[chr(e) for e in range(65,91)]
    grid=[]
    
    for x in range(size):
            row=[]
            for y in range(size):
                row.append(random.choice(letters))
            grid.append(row)
   
   
   
############################################
def print_grid(hide=True):
    
    global grid
    
    grid_string=""
    
    if hide:
        for row in grid:
            #print("\n",*map(str.upper,row), end=" ")
            row_string=""
            for letter in row:
                row_string+=" "+letter.upper()
                
            grid_string+="\n"+row_string
        
    else:
        #print()
        for row in grid:
            
            row_string=""
            for letter in row:
                if letter.isupper():
                    #print("░",end=" ")
                    row_string+=" -"
                    
                else:
                    #print(letter,end=" ")
                    row_string+=" "+letter
            #print()
            grid_string+="\n"+row_string
    
    return grid_string

############################################     
def insert_vertically(word,reversed=False):
    
    global grid
    collision_total=0
    
    if reversed: word= word[::-1]
    word=word.lower()
    
    row_with= len(grid[0])
    
    while collision_total< max_collision:
        
        #if collision_total> 10: print("Skip", word)
            
        row_column =random.randint(0,(len(grid)-1)-len(word))
        random_column = random.randint(0,row_with-1)
        
        collision=False
        ##Check for collision
        for i in range(len(word)):
            if grid[i+row_column][random_column].islower():
                print(f"{word} vertically collision | ", end=" ")
                collision_total+=1
                collision=True
                    
            if word[i] == grid[i+row_column][random_column]:
                collision=False
                
        if collision: continue
        
        ##UPDATE
        for i in range(len(word)):
            grid[i+row_column][random_column]=word[i]
        break
    
    else:
        print("\nSkip ->", word)
        words.remove(word)
        
        

############################################
def insert_horizontally(word,reversed=False):
    
    global grid
    collision_total = 0
    
    if reversed: word= word[::-1]
    word=word.lower()
    
    while collision_total< max_collision:
        
        #if collision_total> 10: print("Skip", word)
        
        
        random_row = random.randint(0,len(grid)-1)
        random_column = random.randint(0,len(grid[random_row])-len(word))
        
        collision=False
        ##Check for collision
        for i in range(len(word)):
            if grid[random_row][random_column+i].islower():
                   
                print(f"{word} horizontally collision - ", end=" ")
                collision_total+=1
                collision=True
                
            if word[i] == grid[random_row][random_column+i]:
                collision=False
                
        if collision: continue
                
        ##UPDATE
        for i,letter in enumerate(word):
            #print(grid[random_row][random_column+i],"=", letter)
            grid[random_row][random_column+i]= word[i]
        break
    
    else:
        print("\nSkip ->", word)
        words.remove(word)
    
    

############################################
def insert_diagonally(word,reversed=False):
    
    global grid
    collision_total=0
    
    if reversed: word= word[::-1]
    word=word.lower()
    
    grid_with= len(grid[0])-1
    grid_hight= len(grid)-1
    
    while collision_total< max_collision:
        
        #if collision_total> 10: print("Skip", word)
        
        random_row = random.randint(0,(len(grid)-1)-len(word))
        random_column = random.randint(0,len(grid[random_row])-len(word))
        
        collision=False
        
        ##Check for collision
        for i in range(len(word)):
            if grid[i+random_row][i+random_column].islower():
                print(f"{word} diagonally collision \ ",end=" ")
                collision_total+=1
                collision=True
            
            if word[i] == grid[random_row+i][random_column+i]:
                collision=False
                
        if collision: continue
        
        ##UPDATE
        for i in range(len(word)):
            grid[random_row+i][random_column+i]= word[i]
        
        break
    else:
        print("\nSkip ->", word)
        words.remove(word)
    
            
    

############################################
def insert_diagonally_(word,reversed=False):
    
    global grid
    collision_total =0
    
    if reversed: word= word[::-1]
    
    grid_with= len(grid[0])-1
    grid_hight= len(grid)-1

    while collision_total< max_collision:
        
        #if collision_total> 10: print("Skip", word)
        
        random_column= random.randint(0,grid_with-len(word))
        random_row = random.randint(len(word),grid_hight)
        
        collision=False
            
        ##Check for collision
        for i in range(len(word)):
            if grid[random_row-i][random_column+i].islower():
                print(f"{word} diagonally collision / ", end=" ")
                collision_total+=1
                collision=True
            
            if word[i] == grid[random_row-i][random_column+i]:
                collision=False
                
        if collision: continue
        
        ##UPDATE       
        for i in range(len(word)):
            grid[random_row-i][random_column+i]=word[i]

        break
    
    else:
        print("\nSkip ->", word)
        words.remove(word)
    
            
     
############################################
############################################
def insert_words(words):
    
    global grid
    
    for word in words:
        direction =random.randint(0,3)
        #reversed=random.choice([True, False])
        reversed=False
        
        if direction == 0:
            insert_vertically(word,reversed)

        elif direction == 1:
            insert_horizontally(word,reversed)
            
        elif direction == 2:
            insert_diagonally(word,reversed)
        
        elif direction == 3:
            insert_diagonally_(word,reversed)
    


############################################
def pick_words(file='words.txt',number_of_words=6 ):
    global words
    
    word_list=[]
    if os.path.exists(file):
        with open(file) as f:
                    rows = f.readlines()
                    for x in rows:
                        word_list.append(x.replace("\n",""))
    else:
        print(f"{file} not found, default words used.")
        word_list=["cow","puppy","cat","monkey","loin","sheep","dog","frog","grandmother",\
                   "advertisement","hall","wish","crime","doll","whip","snakes"]
        
    
    if number_of_words<= len(word_list):
        words=random.sample(word_list,number_of_words)
    else:
        print(f"{len(word_list)} available.")
        words=random.sample(word_list,len(word_list))
    
    """
    ##remove words that are too long for the grid
    for word in words:
        if len(word) >=len(grid[0]):
            words.remove(word)
            print(word,"to long  for grid",)
        else:
            print(word)
    """ 
   
    words.sort(key=len, reverse=True)# sort length descending
    


############################################
def save_to_file(name="word_search"):
    
    random.shuffle(words)
    words_string=""
    for i, word in enumerate(words):
        words_string+=str(i+1)+":"+word.title()+"  "
        
        if (i+1)%5==0:
            words_string+="\n\n"
    
    f = open(name+".txt", "w")
    f.write(print_grid() +"\n\n"+words_string)
    f.close()

    f = open(name+"_solution.txt", "w")
    f.write(print_grid(False)+"\n\n"+words_string)
    f.close()



############################################
############################################
##Testing
while True:
    os.system('cls')
   
    init_grid(15)
    pick_words(number_of_words=20)
    insert_words(words)

    save_to_file()

    print(print_grid())

    print("\n","--"*20)
    print(words)

    input("::")
    print(print_grid(False))
    input("::")
    



