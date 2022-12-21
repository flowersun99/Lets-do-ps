#카드게임


# R, B, Y, G, 각 9장씩 36장
color_list = []
num_list = []
for _ in range(5):
    color, num = input().split()
    num = int(num)
    color_list.append(color)
    num_list.append(num)
num_list.sort()
color_set = set(color_list)
num_set = set(num_list)
check_num = [(num_list[0] + i) for i in range(1, 6)]
# 카드 5장이 모두 같은 색이면서 숫자가 연속적일 때, 점수는 가장 높은 숫자에 900을 더한다. 
if len(color_set) == 1 and check_num in num_list:
    print(900 + max(num_list))
    exit()

# 카드 5장 중 4장의 숫자가 같을 때 점수는 같은 숫자에 800을 더한다. 
if len(num_set) == 2:
    if num_list[0] != num_list[1] or num_list[-1] != num_list[-2]:
        print(num_list[2] + 800)
    else:
        
# 카드 5장 중 3장의 숫자가 같고 나머지 2장도 숫자가 같을 때 점수는 3장이 같은 숫자에 10을 곱하고 2장이 같은 숫자를 더한 다음 700을 더한다.

# 5장의 카드 색깔이 모두 같을 때 점수는 가장 높은 숫자에 600을 더한다.
# 카드 5장의 숫자가 연속적일 때 점수는 가장 높은 숫자에 500을 더한다
# 카드 5장 중 3장의 숫자가 같을 때 점수는 같은 숫자에 400을 더한다.
# 카드 5장 중 2장의 숫자가 같고 또 다른 2장의 숫자가 같을 때 점수는 같은 숫자 중 큰 숫자에 10을 곱하고 같은 숫자 중 작은 숫자를 더한 다음 300을 더한다.
# 카드 5장 중 2장의 숫자가 같을 때 점수는 같은 숫자에 200을 더한다. 예를 들어, R5, Y2, B5, B3, G4 일 때 점수는 205(=5+200)점이다.
# 위의 어떤 경우에도 해당하지 않을 때 점수는 가장 큰 숫자에 100을 더한다.