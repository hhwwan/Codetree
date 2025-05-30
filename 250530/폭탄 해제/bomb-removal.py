unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class boom:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

Boom = boom(unlock_code, wire_color, seconds)

print('code :', Boom.code)
print('color :', Boom.color)
print('second :', Boom.second)