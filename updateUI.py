import re
import sys
import os
from PySide6.QtWidgets import QPushButton, QApplication
import shiboken6
sudoku = []
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

selectedDigit = None
selectedCell = None
errors = 0
error_panel = None
grid_layout = None
main_heading = None
verticalLayout = None
MainWindow = None

def restart(self):
    QApplication.quit()
    executable = f'"{sys.executable}"'
    args = [executable] + [f'"{arg}"' for arg in sys.argv] 
    os.execv(sys.executable, args)

def setDigit(digit_value, cell, window):
    global selectedDigit
    if selectedDigit != None:
        selectedDigit = None
        selectedDigit = digit_value
        window.One.setStyleSheet("")
        window.Two.setStyleSheet("")
        window.Three.setStyleSheet("")
        window.Four.setStyleSheet("")
        window.Five.setStyleSheet("")
        window.Six.setStyleSheet("")
        window.Seven.setStyleSheet("")
        window.Eight.setStyleSheet("")
        window.Nine.setStyleSheet("")
        cell.setStyleSheet("background-color: #5A5A5A8E;")
    else:
        selectedDigit = digit_value
        cell.setStyleSheet("background-color: #5A5A5A8E;")

def setValueAtCell(cell):
    global selectedCell
    global selectedDigit
    if(selectedDigit == None):
        return
    global errors
    selectedCell = cell
    word_to_digit = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    text = cell.objectName()
    words = re.findall(r'[A-Z][a-z]*', text)
    digits_list = [word_to_digit[word.lower()] for word in words]
    row = digits_list[0]
    col = digits_list[1]
    if selectedDigit == board[row-1][col-1]:
        cell.setText(str(selectedDigit))
        sudoku[row-1][col-1] = selectedDigit
    else:
        errors += 1
        error_panel.setText(f"Errors: {errors}")

    game_not_finished = True
    # Assuming 'self.grid_layout' is your QGridLayout instance
    for row in range(0, 9):       # QGridLayout uses 0-indexed rows (0 to 8)
        for col in range(0, 9):    # and 0-indexed columns (0 to 8)

            # Fetch the layout item at the grid coordinates
            layout_item = grid_layout.itemAtPosition(row, col)

            if layout_item is not None:
                button = layout_item.widget()

                # Ensure it is actually a button before checking text
                if isinstance(button, QPushButton) and shiboken6.isValid(button):
                    if button.text().strip() == "":
                        game_not_finished = False

    if(game_not_finished):
        main_heading.setText("Game Finished! You Won.")
        main_heading.setStyleSheet("font-size: 30px; color: #2C2C2C; font-family: monospace;")
        error_panel.hide()
        button = QPushButton("Play Again")
        button.setStyleSheet("font-size: 16px; padding: 6px 12px; font-family: 'Arial Rounded MT Bold', sans-serif; font-weight: bold; color: #ffffff; background-color: #4edb31; border-radius: 8px;")
        button.clicked.connect(restart)
        verticalLayout.addWidget(button)


def updateUI(window):
    import random
    import copy

    global error_panel
    error_panel = window.errorLabel
    global grid_layout
    grid_layout = window.gridLayout
    global main_heading
    main_heading = window.label
    global verticalLayout
    verticalLayout = window.verticalLayout
    global MainWindow
    MainWindow = window
    
    def createPuzzle() :
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
            j = random.randrange(0, i + 1)
            [numbers[i], numbers[j]] = [numbers[j], numbers[i]]
        for r in range(9):
            for c in range(9):
                index = (r * 3 + r // 3 + c) % 9
                board[r][c] = numbers[index]

    def createEasy():
        createPuzzle()
        global sudoku
        sudoku = copy.deepcopy(board)
        cells = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(cells)
        for r, c in cells[:1]:
            sudoku[r][c] = 0

    createEasy()

    if(sudoku[0][0] != 0):
        window.OneOne.setText(str(sudoku[0][0]))
    else:
        window.OneOne.clicked.connect(lambda : setValueAtCell(window.OneOne))
    if(sudoku[0][1] != 0):
        window.OneTwo.setText(str(sudoku[0][1]))
    else:
        window.OneTwo.clicked.connect(lambda : setValueAtCell(window.OneTwo))
    if(sudoku[0][2] != 0):
        window.OneThree.setText(str(sudoku[0][2]))
    else:
        window.OneThree.clicked.connect(lambda : setValueAtCell(window.OneThree))
    if(sudoku[0][3] != 0):
        window.OneFour.setText(str(sudoku[0][3]))
    else:
        window.OneFour.clicked.connect(lambda : setValueAtCell(window.OneFour))
    if(sudoku[0][4] != 0):
        window.OneFive.setText(str(sudoku[0][4]))
    else:
        window.OneFive.clicked.connect(lambda : setValueAtCell(window.OneFive))
    if(sudoku[0][5] != 0):
        window.OneSix.setText(str(sudoku[0][5]))
    else:
        window.OneSix.clicked.connect(lambda : setValueAtCell(window.OneSix))
    if(sudoku[0][6] != 0):
        window.OneSeven.setText(str(sudoku[0][6]))
    else:
        window.OneSeven.clicked.connect(lambda : setValueAtCell(window.OneSeven))
    if(sudoku[0][7] != 0):
        window.OneEight.setText(str(sudoku[0][7]))
    else:
        window.OneEight.clicked.connect(lambda : setValueAtCell(window.OneEight))
    if(sudoku[0][8] != 0):
        window.OneNine.setText(str(sudoku[0][8]))
    else:
        window.OneNine.clicked.connect(lambda : setValueAtCell(window.OneNine))

    if(sudoku[1][0] != 0):
        window.TwoOne.setText(str(sudoku[1][0]))
    else:
        window.TwoOne.clicked.connect(lambda : setValueAtCell(window.TwoOne))
    if(sudoku[1][1] != 0):
        window.TwoTwo.setText(str(sudoku[1][1]))
    else:
        window.TwoTwo.clicked.connect(lambda : setValueAtCell(window.TwoTwo))
    if(sudoku[1][2] != 0):
        window.TwoThree.setText(str(sudoku[1][2]))
    else:
        window.TwoThree.clicked.connect(lambda : setValueAtCell(window.TwoThree))
    if(sudoku[1][3] != 0):
        window.TwoFour.setText(str(sudoku[1][3]))
    else:
        window.TwoFour.clicked.connect(lambda : setValueAtCell(window.TwoFour))
    if(sudoku[1][4] != 0):
        window.TwoFive.setText(str(sudoku[1][4]))
    else:
        window.TwoFive.clicked.connect(lambda : setValueAtCell(window.TwoFive))
    if(sudoku[1][5] != 0):
        window.TwoSix.setText(str(sudoku[1][5]))
    else:
        window.TwoSix.clicked.connect(lambda : setValueAtCell(window.TwoSix))
    if(sudoku[1][6] != 0):
        window.TwoSeven.setText(str(sudoku[1][6]))
    else:
        window.TwoSeven.clicked.connect(lambda : setValueAtCell(window.TwoSeven))
    if(sudoku[1][7] != 0):
        window.TwoEight.setText(str(sudoku[1][7]))
    else:
        window.TwoEight.clicked.connect(lambda : setValueAtCell(window.TwoEight))
    if(sudoku[1][8] != 0):
        window.TwoNine.setText(str(sudoku[1][8]))
    else:
        window.TwoNine.clicked.connect(lambda : setValueAtCell(window.TwoNine))

    if(sudoku[2][0] != 0):
        window.ThreeOne.setText(str(sudoku[2][0]))
    else:
        window.ThreeOne.clicked.connect(lambda : setValueAtCell(window.ThreeOne))
    if(sudoku[2][1] != 0):
        window.ThreeTwo.setText(str(sudoku[2][1]))
    else:
        window.ThreeTwo.clicked.connect(lambda : setValueAtCell(window.ThreeTwo))
    if(sudoku[2][2] != 0):
        window.ThreeThree.setText(str(sudoku[2][2]))
    else:
        window.ThreeThree.clicked.connect(lambda : setValueAtCell(window.ThreeThree))
    if(sudoku[2][3] != 0):
        window.ThreeFour.setText(str(sudoku[2][3]))
    else:
        window.ThreeFour.clicked.connect(lambda : setValueAtCell(window.ThreeFour))
    if(sudoku[2][4] != 0):
        window.ThreeFive.setText(str(sudoku[2][4]))
    else:
        window.ThreeFive.clicked.connect(lambda : setValueAtCell(window.ThreeFive))
    if(sudoku[2][5] != 0):
        window.ThreeSix.setText(str(sudoku[2][5]))
    else:
        window.ThreeSix.clicked.connect(lambda : setValueAtCell(window.ThreeSix))
    if(sudoku[2][6] != 0):
        window.ThreeSeven.setText(str(sudoku[2][6]))
    else:
        window.ThreeSeven.clicked.connect(lambda : setValueAtCell(window.ThreeSeven))
    if(sudoku[2][7] != 0):
        window.ThreeEight.setText(str(sudoku[2][7]))
    else:
        window.ThreeEight.clicked.connect(lambda : setValueAtCell(window.ThreeEight))
    if(sudoku[2][8] != 0):
        window.ThreeNine.setText(str(sudoku[2][8]))
    else:
        window.ThreeNine.clicked.connect(lambda : setValueAtCell(window.ThreeNine))

    if(sudoku[3][0] != 0):
        window.FourOne.setText(str(sudoku[3][0]))
    else:
        window.FourOne.clicked.connect(lambda : setValueAtCell(window.FourOne))
    if(sudoku[3][1] != 0):
        window.FourTwo.setText(str(sudoku[3][1]))
    else:
        window.FourTwo.clicked.connect(lambda : setValueAtCell(window.FourTwo))
    if(sudoku[3][2] != 0):
        window.FourThree.setText(str(sudoku[3][2]))
    else:
        window.FourThree.clicked.connect(lambda : setValueAtCell(window.FourThree))
    if(sudoku[3][3] != 0):
        window.FourFour.setText(str(sudoku[3][3]))
    else:
        window.FourFour.clicked.connect(lambda : setValueAtCell(window.FourFour))
    if(sudoku[3][4] != 0):
        window.FourFive.setText(str(sudoku[3][4]))
    else:
        window.FourFive.clicked.connect(lambda : setValueAtCell(window.FourFive))
    if(sudoku[3][5] != 0):
        window.FourSix.setText(str(sudoku[3][5]))
    else:
        window.FourSix.clicked.connect(lambda : setValueAtCell(window.FourSix))
    if(sudoku[3][6] != 0):
        window.FourSeven.setText(str(sudoku[3][6]))
    else:
        window.FourSeven.clicked.connect(lambda : setValueAtCell(window.FourSeven))
    if(sudoku[3][7] != 0):
        window.FourEight.setText(str(sudoku[3][7]))
    else:
        window.FourEight.clicked.connect(lambda : setValueAtCell(window.FourEight))
    if(sudoku[3][8] != 0):
        window.FourNine.setText(str(sudoku[3][8]))
    else:
        window.FourNine.clicked.connect(lambda : setValueAtCell(window.FourNine))

    if(sudoku[4][0] != 0):
        window.FiveOne.setText(str(sudoku[4][0]))
    else:
        window.FiveOne.clicked.connect(lambda : setValueAtCell(window.FiveOne))
    if(sudoku[4][1] != 0):
        window.FiveTwo.setText(str(sudoku[4][1]))
    else:
        window.FiveTwo.clicked.connect(lambda : setValueAtCell(window.FiveTwo))
    if(sudoku[4][2] != 0):
        window.FiveThree.setText(str(sudoku[4][2]))
    else:
        window.FiveThree.clicked.connect(lambda : setValueAtCell(window.FiveThree))
    if(sudoku[4][3] != 0):
        window.FiveFour.setText(str(sudoku[4][3]))
    else:
        window.FiveFour.clicked.connect(lambda : setValueAtCell(window.FiveFour))
    if(sudoku[4][4] != 0):
        window.FiveFive.setText(str(sudoku[4][4]))
    else:
        window.FiveFive.clicked.connect(lambda : setValueAtCell(window.FiveFive))
    if(sudoku[4][5] != 0):
        window.FiveSix.setText(str(sudoku[4][5]))
    else:
        window.FiveSix.clicked.connect(lambda : setValueAtCell(window.FiveSix))
    if(sudoku[4][6] != 0):
        window.FiveSeven.setText(str(sudoku[4][6]))
    else:
        window.FiveSeven.clicked.connect(lambda : setValueAtCell(window.FiveSeven))
    if(sudoku[4][7] != 0):
        window.FiveEight.setText(str(sudoku[4][7]))
    else:
        window.FiveEight.clicked.connect(lambda : setValueAtCell(window.FiveEight))
    if(sudoku[4][8] != 0):
        window.FiveNine.setText(str(sudoku[4][8]))
    else:
        window.FiveNine.clicked.connect(lambda : setValueAtCell(window.FiveNine))

    if(sudoku[5][0] != 0):
        window.SixOne.setText(str(sudoku[5][0]))
    else:
        window.SixOne.clicked.connect(lambda : setValueAtCell(window.SixOne))
    if(sudoku[5][1] != 0):
        window.SixTwo.setText(str(sudoku[5][1]))
    else:
        window.SixTwo.clicked.connect(lambda : setValueAtCell(window.SixTwo))
    if(sudoku[5][2] != 0):
        window.SixThree.setText(str(sudoku[5][2]))
    else:
        window.SixThree.clicked.connect(lambda : setValueAtCell(window.SixThree))
    if(sudoku[5][3] != 0):
        window.SixFour.setText(str(sudoku[5][3]))
    else:
        window.SixFour.clicked.connect(lambda : setValueAtCell(window.SixFour))
    if(sudoku[5][4] != 0):
        window.SixFive.setText(str(sudoku[5][4]))
    else:
        window.SixFive.clicked.connect(lambda : setValueAtCell(window.SixFive))
    if(sudoku[5][5] != 0):
        window.SixSix.setText(str(sudoku[5][5]))
    else:
        window.SixSix.clicked.connect(lambda : setValueAtCell(window.SixSix))
    if(sudoku[5][6] != 0):
        window.SixSeven.setText(str(sudoku[5][6]))
    else:
        window.SixSeven.clicked.connect(lambda : setValueAtCell(window.SixSeven))
    if(sudoku[5][7] != 0):
        window.SixEight.setText(str(sudoku[5][7]))
    else:
        window.SixEight.clicked.connect(lambda : setValueAtCell(window.SixEight))
    if(sudoku[5][8] != 0):
        window.SixNine.setText(str(sudoku[5][8]))
    else:
        window.SixNine.clicked.connect(lambda : setValueAtCell(window.SixNine))

    if(sudoku[6][0] != 0):
        window.SevenOne.setText(str(sudoku[6][0]))
    else:
        window.SevenOne.clicked.connect(lambda : setValueAtCell(window.SevenOne))
    if(sudoku[6][1] != 0):
        window.SevenTwo.setText(str(sudoku[6][1]))
    else:
        window.SevenTwo.clicked.connect(lambda : setValueAtCell(window.SevenTwo))
    if(sudoku[6][2] != 0):
        window.SevenThree.setText(str(sudoku[6][2]))
    else:
        window.SevenThree.clicked.connect(lambda : setValueAtCell(window.SevenThree))
    if(sudoku[6][3] != 0):
        window.SevenFour.setText(str(sudoku[6][3]))
    else:
        window.SevenFour.clicked.connect(lambda : setValueAtCell(window.SevenFour))
    if(sudoku[6][4] != 0):
        window.SevenFive.setText(str(sudoku[6][4]))
    else:
        window.SevenFive.clicked.connect(lambda : setValueAtCell(window.SevenFive))
    if(sudoku[6][5] != 0):
        window.SevenSix.setText(str(sudoku[6][5]))
    else:
        window.SevenSix.clicked.connect(lambda : setValueAtCell(window.SevenSix))
    if(sudoku[6][6] != 0):
        window.SevenSeven.setText(str(sudoku[6][6]))
    else:
        window.SevenSeven.clicked.connect(lambda : setValueAtCell(window.SevenSeven))
    if(sudoku[6][7] != 0):
        window.SevenEight.setText(str(sudoku[6][7]))
    else:
        window.SevenEight.clicked.connect(lambda : setValueAtCell(window.SevenEight))
    if(sudoku[6][8] != 0):
        window.SevenNine.setText(str(sudoku[6][8]))
    else:
        window.SevenNine.clicked.connect(lambda : setValueAtCell(window.SevenNine))

    if(sudoku[7][0] != 0):
        window.EightOne.setText(str(sudoku[7][0]))
    else:
        window.EightOne.clicked.connect(lambda : setValueAtCell(window.EightOne))
    if(sudoku[7][1] != 0):
        window.EightTwo.setText(str(sudoku[7][1]))
    else:
        window.EightTwo.clicked.connect(lambda : setValueAtCell(window.EightTwo))
    if(sudoku[7][2] != 0):
        window.EightThree.setText(str(sudoku[7][2]))
    else:
        window.EightThree.clicked.connect(lambda : setValueAtCell(window.EightThree))
    if(sudoku[7][3] != 0):
        window.EightFour.setText(str(sudoku[7][3]))
    else:
        window.EightFour.clicked.connect(lambda : setValueAtCell(window.EightFour))
    if(sudoku[7][4] != 0):
        window.EightFive.setText(str(sudoku[7][4]))
    else:
        window.EightFive.clicked.connect(lambda : setValueAtCell(window.EightFive))
    if(sudoku[7][5] != 0):
        window.EightSix.setText(str(sudoku[7][5]))
    else:
        window.EightSix.clicked.connect(lambda : setValueAtCell(window.EightSix))
    if(sudoku[7][6] != 0):
        window.EightSeven.setText(str(sudoku[7][6]))
    else:
        window.EightSeven.clicked.connect(lambda : setValueAtCell(window.EightSeven))
    if(sudoku[7][7] != 0):
        window.EightEight.setText(str(sudoku[7][7]))
    else:
        window.EightEight.clicked.connect(lambda : setValueAtCell(window.EightEight))
    if(sudoku[7][8] != 0):
        window.EightNine.setText(str(sudoku[7][8]))
    else:
        window.EightNine.clicked.connect(lambda : setValueAtCell(window.EightNine))

    if(sudoku[8][0] != 0):
        window.NineOne.setText(str(sudoku[8][0]))
    else:
        window.NineOne.clicked.connect(lambda : setValueAtCell(window.NineOne))
    if(sudoku[8][1] != 0):
        window.NineTwo.setText(str(sudoku[8][1]))
    else:
        window.NineTwo.clicked.connect(lambda : setValueAtCell(window.NineTwo))
    if(sudoku[8][2] != 0):
        window.NineThree.setText(str(sudoku[8][2]))
    else:
        window.NineThree.clicked.connect(lambda : setValueAtCell(window.NineThree))
    if(sudoku[8][3] != 0):
        window.NineFour.setText(str(sudoku[8][3]))
    else:
        window.NineFour.clicked.connect(lambda : setValueAtCell(window.NineFour))
    if(sudoku[8][4] != 0):
        window.NineFive.setText(str(sudoku[8][4]))
    else:
        window.NineFive.clicked.connect(lambda : setValueAtCell(window.NineFive))
    if(sudoku[8][5] != 0):
        window.NineSix.setText(str(sudoku[8][5]))
    else:
        window.NineSix.clicked.connect(lambda : setValueAtCell(window.NineSix))
    if(sudoku[8][6] != 0):
        window.NineSeven.setText(str(sudoku[8][6]))
    else:
        window.NineSeven.clicked.connect(lambda : setValueAtCell(window.NineSeven))
    if(sudoku[8][7] != 0):
        window.NineEight.setText(str(sudoku[8][7]))
    else:
        window.NineEight.clicked.connect(lambda : setValueAtCell(window.NineEight))
    if(sudoku[8][8] != 0):
        window.NineNine.setText(str(sudoku[8][8]))
    else:
        window.NineNine.clicked.connect(lambda : setValueAtCell(window.NineNine))

    window.One.clicked.connect(lambda: setDigit(1, window.One, window))
    window.Two.clicked.connect(lambda: setDigit(2, window.Two, window))
    window.Three.clicked.connect(lambda: setDigit(3, window.Three, window))
    window.Four.clicked.connect(lambda: setDigit(4, window.Four, window))
    window.Five.clicked.connect(lambda: setDigit(5, window.Five, window))
    window.Six.clicked.connect(lambda: setDigit(6, window.Six, window))
    window.Seven.clicked.connect(lambda: setDigit(7, window.Seven, window))
    window.Eight.clicked.connect(lambda: setDigit(8, window.Eight, window))
    window.Nine.clicked.connect(lambda: setDigit(9, window.Nine, window))