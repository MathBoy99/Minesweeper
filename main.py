import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import random
import time
changed=False
ete=0
# Base grid_length is 24
grid_length = 24
# Base grid_height is 16
grid_height = 16
# Base mine_density is 0.19
mine_density=0.19
# Base scale_factor is 1
scale_factor = 1
# Base find_four is False
find_four=False
# Base grid_size is [800,600]
grid_size=[800,600]

pygame.init()

def load_image(image_name, cell_size, scale_factor):
  image = pygame.image.load(image_name)
  scaled_size = int(cell_size * scale_factor)
  return pygame.transform.scale(image, (scaled_size, scaled_size))

screen = pygame.display.set_mode((grid_size), pygame.NOFRAME)

def get_index(mouse_x,mouse_y,grid_length,grid_height,size):
    gridx = (grid_length+1)*size
    gridy = (grid_height+1)*size
    iteration=-1
    thing1=grid_length+1
    thing2=grid_height+1
    for item in range(round(size),gridx, round(size)):
        iteration+=1
        if mouse_x < item:
            thing1=iteration
            break
    iteration=-1
    for item in range(round(size),gridy, round(size)):
        iteration+=1
        if mouse_y < item:
            thing2=iteration
            break
    if thing1<=grid_length-1 and thing2<=grid_height-1:
        return thing1+thing2*grid_length
    else:
        return ":("

def new_hide_grid(grid_lengthy,gridy,hide_gridy,empty_index):
    keep_going=[empty_index]
    no_repeat=[]
    thing=[]
    while True:
        for apple in keep_going:
            for item in adjecent:
                if item+apple>=0 and item+apple<len(grid) and (abs(apple%grid_length - (apple+item)%grid_length))<2:
                    hide_gridy[item+apple]=0
                    if gridy[item+apple]==10:
                        if (item+apple) not in no_repeat:
                            thing.append(item+apple)
                            no_repeat.append(item+apple)
            keep_going.remove(apple)
            no_repeat.append(apple)
        for thingy in thing:
            keep_going.append(thingy)
            thing.remove(thingy)
        if len(keep_going)==0:
            break
    return hide_gridy
mem_in_settings=False
def start_program_math(grid_length,grid_height,mine_density,scale_factor):
    guess_flag_help=0
    if grid_length*grid_height*mine_density>99:
        flagged_length=grid_length
    else:
        flagged_length=grid_length+2
    cell_width = grid_size[0] // (flagged_length)
    cell_height = grid_size[1] // grid_height
    cell_size = min(cell_width, cell_height)
    scaled_size = int(cell_size * scale_factor)
    listy_list=[0,0,0,0,0,0,0,0,0]
    wordy_word=["Empty:","One:","Two:","Three:","Four:","Five:","Six:","Seven:","Eight:"]
    zero= load_image('Tile0.png', cell_size,scale_factor)
    one = load_image('Tile1.png', cell_size, scale_factor)
    two = load_image('Tile2.png', cell_size, scale_factor)
    three = load_image('Tile3.png', cell_size, scale_factor)
    four = load_image('Tile4.png', cell_size, scale_factor)
    five = load_image('Tile5.png', cell_size, scale_factor)
    six = load_image('Tile6.png', cell_size, scale_factor)
    seven = load_image('Tile7.png', cell_size, scale_factor)
    eight = load_image('Tile8.png', cell_size, scale_factor)
    nine= load_image('Tile9.png', cell_size,scale_factor)
    mine = load_image('TileMine.png', cell_size, scale_factor)
    flag = load_image('TileFlag.png', cell_size, scale_factor)
    empty = load_image('TileEmpty.png', cell_size, scale_factor)
    locked = load_image('TileUnknown.png', cell_size, scale_factor)
    exploded = load_image('TileExploded.png', cell_size,scale_factor)
    wrong = load_image('WrongFlag.png', cell_size,scale_factor)
    img_list = [mine, one, two, three, four, five, six, seven, eight, flag, empty, locked, exploded, wrong]
    tiles_in_order=[zero,one,two,three,four,five,six,seven,eight,nine]
    Purple=load_image('Purple_Flag.png', cell_size, scale_factor)
    yelllow=load_image('Yellow_Flag.png', cell_size, scale_factor)
    green=load_image('Green_Flag.png', cell_size, scale_factor)
    Blue=load_image('Blue_Flag.png', cell_size, scale_factor)
    guess_flags=[Purple,yelllow,green,Blue]
    
    grid=[]
    hide_grid=[]
    for i in range(grid_length*grid_height):
        grid.append(random.randint(1,8))
        hide_grid.append(1)
    mines=round(grid_length*grid_height*mine_density)
    return guess_flag_help,listy_list,wordy_word,cell_size,scaled_size,img_list,tiles_in_order,guess_flags,grid,hide_grid,mines
Stuff=start_program_math(grid_length,grid_height,mine_density,scale_factor)
guess_flag_help=Stuff[0]
listy_list=Stuff[1]
wordy_word=Stuff[2]
cell_size=Stuff[3]
scaled_size=Stuff[4]
img_list=Stuff[5]
settings_img_list=Stuff[5]
tiles_in_order=Stuff[6]
settings_tiles_in_order=Stuff[6]
guess_flags=Stuff[7]
settings_guess_flags=Stuff[7]
grid=Stuff[8]
hide_grid=Stuff[9]
mines=Stuff[10]
apple_tree=0

settings_buttons=[pygame.Rect(0,0,scaled_size,scaled_size),pygame.Rect(scaled_size,0,scaled_size,scaled_size),pygame.Rect(0,scaled_size,scaled_size,scaled_size),pygame.Rect(scaled_size,scaled_size,scaled_size,scaled_size),pygame.Rect(0,scaled_size*2,scaled_size,scaled_size),pygame.Rect(scaled_size,scaled_size*2,scaled_size,scaled_size),pygame.Rect(0,scaled_size*3,scaled_size,scaled_size),pygame.Rect(scaled_size,scaled_size*3,scaled_size,scaled_size),pygame.Rect(scaled_size*2,scaled_size*3,scaled_size,scaled_size)]

settings_buttons_meaning=["grid_length_tens_digit","grid_length_ones_digit","grid_height_tens_digit","grid_height_ones_digit","mine_density_tens_digit","mine_density_ones_digit","scale_factor_ones_digit","scale_factor_tenths_digit","scale_factor_hundredths_digit"]
j=[2,4,1,6,1,9,1,0,0]
fill=[0,120,120]
e=0
times=0
started = False
def get_adjacent(grid_length):
    return [1,-1,grid_length,-grid_length,grid_length+1,grid_length-1,-grid_length+1,-grid_length-1]

adjecent = get_adjacent(grid_length)
play=True
r=True
count=0
grids_generated=0
grids_with=[0,0,0,0,0,0,0,0,0]
gen_grids=False
find_eight=False
pl=False
flagged=mines
sad=[0,0]
bad=[]
running = True
in_settings = False
while running:
    time.sleep(0.01)
    screen.fill(fill)
    if not in_settings:
        iteration = 0
        if not grid_length*grid_height*mine_density>99:
            flag=str(flagged)
            if len(flag)==1:
                flag="0"+flag
            if flagged>0:
                sad[0]=int(flag[0])
                sad[1]=int(flag[1])
            else:
                sad=[0,0]
            ruey=-scaled_size
            for item in sad:
                ruey+=scaled_size
                screen.blit(tiles_in_order[item], ((scaled_size*grid_length)+ruey, 0))
        for row in range(grid_height):
            for col in range(grid_length):
                if iteration < grid_length*grid_height:
                    x = col * scaled_size
                    y = row * scaled_size
                    if hide_grid[iteration]==0:
                        thing = img_list[grid[iteration]]
                    elif hide_grid[iteration]==1:
                        thing = img_list[11]
                    elif hide_grid[iteration]==2:
                        thing = img_list[9]
                    else:
                        thing = guess_flags[hide_grid[iteration]-3]
                    screen.blit(thing, (x, y))
                iteration+=1
        if play or gen_grids:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        e=1
                        times=8
                    elif event.key == pygame.K_d:
                        e=1
                        times=0
                    elif event.key == pygame.K_r:
                        if r:
                            grid=[]
                            hide_grid=[]
                            for i in range(grid_length*grid_height):
                                grid.append(random.randint(1,8))
                                hide_grid.append(1)
                            e=0
                            times=0
                            started = False
                            play=True
                            count+=1
                            if pl:
                                e=1
                                times=4
                            flagged=mines
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_p:
                        ete=2
                    elif event.key == pygame.K_k:
                        gen_grids=True
                        find_eight=False
                    elif event.key == pygame.K_l:
                        find_eight=True
                        gen_grids=True
                    elif event.key == pygame.K_m:
                        find_eight=False
                        gen_grids=False
                    elif event.key == pygame.K_1:
                        guess_flag_help=1
                    elif event.key == pygame.K_2:
                        guess_flag_help=2
                    elif event.key == pygame.K_3:
                        guess_flag_help=3
                    elif event.key == pygame.K_4:
                        guess_flag_help=4
                    elif event.key == pygame.K_s:
                        apple_tree=2
                elif ete==2 and event.type==pygame.KEYUP and grids_generated>0:
                    y=-1
                    ete=0
                    asdjk=0
                    for item in listy_list:
                        print("")
                        y+=1
                        ads=item
                        ads=str(round(((ads/sum(listy_list))*100),2))+"%"
                        print(wordy_word[y]+str(ads))
                        print("Number of "+str(y)+" tiles found: "+str(item))
                        if y!=8:
                            print("Percent of grids with "+str(y)+" tiles: "+str(round(((grids_with[y]/grids_generated)*100),2))+"%")                 
                        else:
                            print("Percent of grids with 8 tiles: "+str(round(((grids_with[y]/grids_generated)*100),6))+"%")
                        print("Grids without "+str(y)+" tiles: "+str(grids_generated-grids_with[y]))
                        print("Average number of "+str(y)+" tiles: "+str(round(item/grids_generated)))
                        asdjk+=item*y
                    print("")
                    print("The average number is: "+str(round(asdjk/sum(listy_list),4)))
                    print("")
                    print("Number of grids generated: "+str(grids_generated))
                elif apple_tree==2 and event.type==pygame.KEYUP:
                    apple_tree=0
                    changed=False
                    in_settings = True
            if pl:
                if r:
                    grid=[]
                    hide_grid=[]
                    for i in range(grid_length*grid_height):
                        grid.append(random.randint(1,8))
                        hide_grid.append(1)
                    e=1
                    times=4
                    started = False
                    play=True
                    count+=1
                    flagged=mines
                    pl=False
            if e==1 and (event.type == pygame.KEYUP or gen_grids):
                e=0
                if times>7:
                    times=0
                    if started:
                        index=get_index(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],grid_length,grid_height,scaled_size)
                        if str(index) !=":(":
                            index=int(index)
                            if hide_grid[index]==1 or hide_grid[index]>2:
                                hide_grid[index]=2
                                flagged-=1
                            elif hide_grid[index]==2:
                                hide_grid[index]=1
                                flagged+=1
                else:
                    times=0
                    index=get_index(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],grid_length,grid_height,scaled_size)
                    if str(index)!=":(" and (len(grid)-1) >= index and index>-1 and hide_grid[index]==1:
                        if not started:
                            do_go=list(range(len(grid)))
                            do_go.remove(index)
                            hide_grid[index]=0
                            for item in adjecent:
                                if item+index>=0 and item+index<len(grid):
                                    do_go.remove(item+index)
                            for item in range(mines):
                                three=(random.sample(do_go,1))[0]
                                grid[three]=0
                                do_go.remove(three)
                            iteration=-1
                            added_to=[False,False,False,False,False,False,False,False,False]
                            for item in grid:
                                iteration+=1
                                if item!=0:
                                    e=0
                                    for items in adjecent:
                                        if iteration+items>=0 and iteration+items<len(grid):
                                            if grid[iteration+items]==0:
                                                if abs(iteration%grid_length - (iteration+items)%grid_length)<2:
                                                    e+=1
                                    grid[iteration]=e
                                    if e in range(9):
                                        listy_list[e]+=1
                                        if not added_to[e]:
                                            added_to[e]=True
                                            grids_with[e]+=1
                                    if e==8 and find_eight:
                                        fill=[0,0,0]
                                        r=False
                                        gen_grids=False
                                    if e==0:
                                        grid[iteration]=10
                            if not added_to[4] and find_four:
                                fill=[0,0,0]
                                r=False
                                gen_grids=False
                            hide_grid=new_hide_grid(grid_length,grid,hide_grid,index)
                            started=True
                            grids_generated+=1
                            if gen_grids:
                                pl=True
                            
                            win=True
                            e=[]
                            for item in range(len(grid)):
                                if grid[item]>0:
                                    if hide_grid[item]>0:
                                        win=False
                                        break
                            if win:
                                play=False
                                print("You won")
                        else:
                            hide_grid[index]=0
                            if grid[index]==0:
                                it=-1
                                grid[index]=12
                                for item in grid:
                                    it+=1
                                    if item==0:
                                        if hide_grid[it]==1:
                                            hide_grid[it]=0
                                    else:
                                        if hide_grid[it]>1:
                                            grid[it]=13
                                            hide_grid[it]=0
                                play=False
                                print("You lost")
                                fill=[0,120,120]
                                r=True
                            elif grid[index]==10:
                                hide_grid=new_hide_grid(grid_length,grid,hide_grid,index)
                            if play:
                                win=True
                                e=[]
                                for item in range(len(grid)):
                                    if grid[item]>0:
                                        if hide_grid[item]>0:
                                            win=False
                                            break
                                if win:
                                    play=False
                                    print("You won")
                                    r=True
                                    fill=[0,120,120]
            else:
                if guess_flag_help>0 and event.type == pygame.KEYUP and started:
                    index=get_index(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],grid_length,grid_height,scaled_size)
                    if str(index)!=":(":
                        index=int(index)
                        if hide_grid[index]==2:
                            flagged+=1
                        if hide_grid[index]==1:
                            hide_grid[index]=guess_flag_help+2
                            guess_flag_help=0
                        elif hide_grid[index]>1:
                            if hide_grid[index]==guess_flag_help+2:
                                hide_grid[index]=1
                                guess_flag_help=0
                            else:
                                hide_grid[index]=guess_flag_help+2
                                guess_flag_help=0
        else:
            for event in pygame.event.get():
                if ete==2 and event.type==pygame.KEYUP and grids_generated>0:
                    y=-1
                    ete=0
                    asdjk=0
                    for item in listy_list:
                        print("")
                        y+=1
                        ads=item
                        ads=str(round(((ads/sum(listy_list))*100),2))+"%"
                        print(wordy_word[y]+str(ads))
                        print("Number of "+str(y)+" tiles found: "+str(item))
                        if y!=8:
                            print("Percent of grids with "+str(y)+" tiles: "+str(round(((grids_with[y]/grids_generated)*100),2))+"%")
                        else:
                            print("Percent of grids with 8 tiles: "+str(round(((grids_with[y]/grids_generated)*100),6))+"%")
                        print("Grids without "+str(y)+" tiles: "+str(grids_generated-grids_with[y]))
                        print("Average number of "+str(y)+" tiles: "+str(round(item/grids_generated)))
                        asdjk+=item*y
                    print("")
                    print("The average number is: "+str(round(asdjk/sum(listy_list),4)))
                    print("")
                    print("Number of grids generated: "+str(grids_generated))
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        if r:
                            grid=[]
                            hide_grid=[]
                            for i in range(grid_length*grid_height):
                                grid.append(random.randint(1,8))
                                hide_grid.append(1)
                            e=0
                            times=0
                            started = False
                            play=True
                            count+=1
                            print(count)
                            flagged=mines
                    elif event.key == pygame.K_p:
                        ete=2
                    elif event.key == pygame.K_s:
                        in_settings = True
                        apple_tree=0
    elif in_settings:
        for item in settings_buttons:
            screen.blit(settings_tiles_in_order[j[settings_buttons.index(item)]], (item.x, item.y))
        if apple_tree==0:
            mem_grid_length=grid_length
            mem_grid_height=grid_height
            mem_mine_density=mine_density
            mem_scale_factor=scale_factor
            apple_tree=1
            mem_in_settings=True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_s:
                    mem_in_settings = False
                elif event.unicode.isdigit():
                    mousex=pygame.mouse.get_pos()[0]
                    mousey=pygame.mouse.get_pos()[1]
                    thingy_thing=0
                    for item in settings_buttons:
                        if item.collidepoint(mousex,mousey):
                            if j[thingy_thing]!=int(f"{event.unicode}"):
                                j[thingy_thing]=int(f"{event.unicode}")
                        thingy_thing+=1
            elif event.type == pygame.KEYUP and not mem_in_settings:
                mem_in_settings=True
                if j[0]*10+j[1]!=mem_grid_length or j[2]*10+j[3]!=mem_grid_height or (j[4]/10+j[5]/100)!=mem_mine_density or j[6]+j[7]/10+j[8]/100!=mem_scale_factor:
                    changed=True
                if changed:
                    Stuff=start_program_math(j[0]*10+j[1],j[2]*10+j[3],(j[4]/10+j[5]/100),j[6]+j[7]/10+j[8]/100)
                    guess_flag_help=Stuff[0]
                    listy_list=Stuff[1]
                    wordy_word=Stuff[2]
                    cell_size=Stuff[3]
                    scaled_size=Stuff[4]
                    img_list=Stuff[5]
                    tiles_in_order=Stuff[6]
                    guess_flags=Stuff[7]
                    grid=Stuff[8]
                    hide_grid=Stuff[9]
                    mines=Stuff[10]
                    flagged=mines
                    grid_length=j[0]*10+j[1]
                    grid_height=j[2]*10+j[3]
                    adjecent = get_adjacent(grid_length)
                    started=False
                    mine_density=j[4]/10+j[5]/100
                    scale_factor=j[6]+j[7]/10+j[8]/100
                    grids_generated=0
                    grids_with=[0,0,0,0,0,0,0,0,0]
                    play=True
                in_settings=False
                
    pygame.display.flip()
pygame.quit()