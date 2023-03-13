# -*- coding:utf-8 -*- chatgpt写的，能运行，但错误也不少

class Gobang:
    board = [['' for x in range(15)] for y in range(15)]


    def __init__(self):
        self.board = [['' for x in range(15)] for y in range(15)]


    def display(self):
        str = "+  "
        for i in range(15):
            str = str + str(i) + "  "
        print(str)
        for i in range(15):
            out_str = str(i) + "  "
            for j in range(15):
                out_str = out_str + self.board[i][j] + "  "
            print(out_str)


    def setChessman(self, row, col, flag):
        if self.board[row][col] == '':
            self.board[row][col] = flag
            return True
        return False


    def checkFive(self, row, col, flag):
        count = self.checkSide(row, col, flag, 0, 1) + self.checkSide(row, col, flag, 1, 0) + \
        self.checkSide(row, col, flag, 1, 1) + self.checkSide(row, col, flag, -1, 1)
        if count >= 4:
            return True
        return False


    def checkSide(self, row, col, flag, offsetX, offsetY):
        count = 0
        for i in range(4):
            new_row = row + offsetX * i
            new_col = col + offsetY * i
            if 0 <= new_row < 15 and 0 <= new_col < 15 and self.board[new_row][new_col] == flag:
                count = count + 1
            else:
                break
        return count


def main():
    game = Gobang()
    player = 1
    flags = ['●','○']
    result = -1
    while result == -1:
        print("请玩家 %d 水平用数字，纵向用字母选择棋坐标，如a1" % player)
        pos = str(input("请落子："))
        row = int(pos[1:])
        col = ord(pos[0]) - ord('a')
        success = game.setChessman(row, col, flags[player - 1])
        if success:
            game.display()
            if game.checkFive(row, col, flags[player - 1]):
                result = player
            else:
                player = 3 - player
        else:
            print("此处位置已有棋子，请重新选择")
    print("玩家 %d 胜出！" % result)


if __name__ == '__main__':
    main()
