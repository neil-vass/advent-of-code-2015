# https://adventofcode.com/2015/day/3

def fetch_data(path):
    with open(path, 'r') as f:
        return f.readline().rstrip()

def house_count(data):
    x,y = 0,0
    visited = {(x,y)}
    for dir in data:
        if dir == '>':
            x,y = x,y+1
        elif dir == '<':
            x,y = x,y-1
        elif dir == '^':
            x,y = x-1,y
        elif dir == 'v':
            x,y = x+1,y
        visited.add((x,y)) 
    return len(visited)

def house_count_with_robo_santa(data):
    santa = [0,0]
    robo_santa = [0,0]
    actor = santa
    visited = {tuple(actor)}
    for dir in data:
        if dir == '>':
            actor[1] += 1
        elif dir == '<':
            actor[1] -= 1
        elif dir == '^':
            actor[0] -= 1
        elif dir == 'v':
            actor[0] += 1
        visited.add(tuple(actor)) 
        actor = santa if actor == robo_santa else robo_santa
    return len(visited)


#--------------------- tests -------------------------#

def test_house_count():
    assert house_count('>') == 2
    assert house_count('^>v<') == 4
    assert house_count('^v^v^v^v^v') == 2

def test_house_count_with_robo_santa():
    assert house_count_with_robo_santa('^v') == 3
    assert house_count_with_robo_santa('^>v<') == 3
    assert house_count_with_robo_santa('^v^v^v^v^v') == 11

#-----------------------------------------------------#

if __name__ == "__main__":
    data = fetch_data('data/day03.txt')
    print(house_count_with_robo_santa(data))
