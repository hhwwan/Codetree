secret_code, meeting_point, time = input().split()
time = int(time)

class code:
    def __init__(self, secret_code, meeting_point, time):
        self.c = secret_code
        self.m = meeting_point
        self.t = time

result = code(secret_code, meeting_point, time)
print('secret code :', result.c)
print('meeting point :', result.m)
print('time :', result.t)