class Member:
    def __init__(self):
        self.name = None
        self.account = None
        self.passwd = None
        self.birthyear = None


mem1 = Member()
mem2 = Member()
mem3 = Member()

mem1.name = "피치"
mem1.account = 1313
mem1.passwd = "3131"
mem1.birthyear = 1990

mem2.name = "릴리"
mem2.account = 1414
mem2.passwd = "4141"
mem2.birthyear = 1990

mem3.name = "데이지"
mem3.account = 1515
mem3.passwd = "5151"
mem3.birthyear = 1990


mem = {'1': mem1, '2': mem2, '3': mem3}
for i, member in mem.items():
    print(f"회원{i}: {member.name}({member.account}, {member.passwd}, {member.birthyear})")
