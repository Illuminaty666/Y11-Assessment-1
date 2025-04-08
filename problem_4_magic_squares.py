from testhelper import test

def is_square_magic(square):
    num = square[0][0] + square[0][1] + square[0][2]
    if square[0][0] + square[0][1] + square[0][2] == num and square[1][0] + square[1][1] + square[1][2] == num and square[2][0] + square[2][1] + square[2][2] == num and square[0][0] + square[1][0] + square[2][0] == num and square[0][1] + square[1][1] + square[2][1] == num and square[0][2] + square[1][2] + square[2][2] == num:
        return("True")       
    else:
        return("False")




### TESTS - Run the code that calls the function to check it works.
valid_square = [[4, 9, 2],[3, 5, 7],[8, 1, 6]]

invalid_square = [[4, 9, 2], 
                [8, 1, 6],
                [3, 5, 7]]
test("Magic Square 1", True, is_square_magic(valid_square))
test("Magic Square 2", False, is_square_magic(invalid_square))