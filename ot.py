def main():
    stale = "I love you ok"
    print("OT!")
    stale = stale[:0] + "weird insertion" + stale[0:]
    print(stale)
    valid = isValid(
        'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
        'Repl.it uses operational transformations.',
        [{"op": "skip", "count": 40}, {"op": "delete", "count": 47}]
    )
    print(valid)
# def test():
#     return "sf"+"fsdf"
# def OT(stale, pos, operations):
#     if operations:      
#         for op in operations:
#             if(op == 'insert'):
#                 insert(stale, operations["chars"])
#             elif(op == 'delete'):
#                 delete(stale, pos, operations["count"])
#             else:
#                 skip(pos, operations["count"])
#     return stale

# def insert(stale, newString):
#     return stale+newString

# def delete(stale, cursor, count):
#     return stale.replace(stale[cursor:count], '')

# def skip(cursor, count):
#     return cursor + count - 1

def isValid(stale, latest, otjson): 
    if not otjson:
        return True
    cursor = 0
    for ot in otjson:
            if(ot['op'] == 'insert'):
                # insert(stale, operations["chars"])
                stale = stale[:cursor] + ot['chars'] + stale[cursor:]
            elif(ot['op']== 'delete'):
                # delete(stale, pos, operations["count"])
                if(len(stale) - cursor < ot['count']):
                    return False
                stale = stale.replace(stale[cursor:ot['count']], '')
            else:
                # skip(pos, operations["count"])
                if cursor + ot['count'] > len(stale):
                    return False
                else:
                    cursor += ot['count']
    
    return latest == stale

if __name__ == "__main__":
    main()