import sys
assert(len(sys.argv) == 2)
fn = sys.argv[1]

def insertFriendship(filename):
    rows = []
    knows = None
    lines = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            print (lines)
            arr = line.split(" ")
            if(knows != None and len(arr) >= 3 and arr[1] == 'snvoc:hasPerson'):
                friend = arr[2]
                edge1 = [knows, 'snvoc:knows', friend, '.', '\n']
                rows.append(' '.join(edge1))
                knows =None
            
            if(len(arr) >= 3 and arr[1] == 'snvoc:knows'):
                knows = arr[0]
            else:
                knows = None
            
            rows.append(line)
    
    with open(filename + ".friendship", 'w') as f:
        for r in rows:
            f.write(r)
insertFriendship(fn)
