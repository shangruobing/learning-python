guests = ['ruobing', 'shang', 'liang']
print(guests)
name = guests[2]
print(f"Sorry {name.title()} can't come")
guests.remove('liang')
guests.append(33)
print(guests)
guests.insert(0, "first")
guests.insert(2, "middle")
print(guests)
name = guests.pop(0)
print(f"Sorry {name.title()},You can't come")
guests.pop(1)
del (guests[1])
print(f"一共邀请了{len(guests)}位客人")
