originalRows = 1324
handTiles = "85 31 32 96 25 1 68"
drawPile = "30 35 42 11 78 39 19 9 81"

originalRows = str(originalRows).zfill(4)
handTiles = handTiles.split()
handTiles = [q.zfill(2) for q in handTiles]
handTiles = [[d for d in q] for q in handTiles]

drawPile = drawPile.split()
drawPile = [q.zfill(2) for q in drawPile]
drawPile = [[d for d in q] for q in drawPile]
global turn
turn = 0

def add():
    global turn
    if turn == 3:
        turn = 0
        return
    turn += 1
    return
    
def sub():
    global turn
    if turn == 0:
        turn = 3
        return
    turn -= 1
    return

rows = [["0" + originalRows[0]], ["0" + originalRows[1]], ["0" + originalRows[2]], ["0" + originalRows[3]]]

print(handTiles)
arr = []
# samhand = []
done = True
while len(handTiles) != 0:
    arr.append(len(handTiles))
    # print(arr)
    # if samhand == rows:
    #     break
    # samhand = rows.copy()
    # sub()
    # print(rows[turn][-1])
    if not done:
        break
    done = False
    if len(rows[turn]) > 1 and rows[turn][-1][0] == rows[turn][-1][1]: #deal with double case first
        print("double case")
        for i in range(len(handTiles[:])):
            if rows[turn][-1][1] == handTiles[i][0]:
                rows[turn].append("".join(handTiles[i]))
                handTiles.pop(i)
                print("run1")
                print(handTiles)
                print(rows)
                done = True
                break
            elif rows[turn][-1][1] == handTiles[i][1]:
                rows[turn].append("".join(handTiles[i][::-1]))
                handTiles.pop(i)
                print("run2")
                print(handTiles)
                print(rows)
                done = True
                break
                
            if i == len(handTiles) - 1:
                print("draw")
                for i in range(len(drawPile[:])):
                    if len(drawPile) == 0:
                        break
                    # if drawPile[0] == "92":
                    #     print("-=----------------")
                    #     print(rows[turn][-1])
                    if rows[turn][-1][1] == drawPile[0][0]:
                        rows[turn].append("".join(drawPile[0]))
                        drawPile.pop(0)
                        print("draw1")
                        print(handTiles)
                        print(rows)
                        done = True
                        break
                    elif rows[turn][-1][1] == drawPile[0][1]:
                        rows[turn].append("".join(drawPile[0][::-1]))
                        drawPile.pop(0)
                        print("draw2")
                        print(handTiles)
                        print(rows)
                        done = True
                        break
                    handTiles.append(drawPile[0])
                    drawPile.pop(0)   
        add()
        continue
    if len(arr) > 1: #fixed case 8, 1, 3
        add()
    for i in range(len(handTiles[:])):
        flag = False
        for x in range(4):
            if rows[turn][-1][1] == handTiles[i][0]:
                rows[turn].append("".join(handTiles[i]))
                handTiles.pop(i)
                print("run3")
                print(handTiles)
                print(rows)
                flag = True
                done = True
                break
            elif rows[turn][-1][1] == handTiles[i][1]:
                rows[turn].append("".join(handTiles[i][::-1]))
                handTiles.pop(i)
                print("run4")
                print(handTiles)
                print(rows)
                flag = True
                done = True
                break
            add()
        if flag:
            break
        
        if i == len(handTiles) - 1:
            for i in range(len(drawPile[:])):
                flag = False
                for x in range(4):
                    if len(drawPile) == 0:
                        break
                    # if (drawPile[0][0] == '7' and drawPile[0][1] == "4"):
                    #     print("dfs")
                    #     breakpoint()
                    if rows[turn][-1][1] == drawPile[0][0]:
                        rows[turn].append("".join(drawPile[0]))
                        drawPile.pop(0)
                        print("draw3")
                        print(handTiles)
                        print(rows)
                        flag = True
                        done = True
                        break
                    elif rows[turn][-1][1] == drawPile[0][1]:
                        rows[turn].append("".join(drawPile[0][::-1]))
                        drawPile.pop(0)
                        print("draw4")
                        print(handTiles)
                        print(rows)
                        flag = True
                        done = True
                        break
                    add()
                if flag:
                    break 
                else:
                    handTiles.append(drawPile[0])
                    drawPile.pop(0)               
    print(rows)
total_sum = sum(int(digit) for sublist in handTiles for digit in sublist)
print(total_sum)
print(rows)
print(total_sum)