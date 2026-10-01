As_friend = {"akshada","ananya","pooja","aishwarya"}
Bs_friend = {"akshada","mohan","jidnyasa","aishwarya"}
common = As_friend&Bs_friend
all_friends = As_friend|Bs_friend
only_a = As_friend-Bs_friend
only_b = Bs_friend-As_friend

print("common friends:",common)
print("all friends:",all_friends)
print("A's Friend:",only_a)
print("B's Friend:",only_b)