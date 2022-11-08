def bytes2matrix(text):
   
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    
    ans = ""
    for i in range(4):
        for j in range(4):
            ans += chr(matrix[i][j])
    return ans

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))