
existing_keys = {}

def try_to_add_key(key):
    if existing_keys.has_key(key) == False:
        existing_keys[key] = 1
        return True
    return False

def find_next_key(ans_key):
    for j1 in range(0,10):
        new_str = ans_key[-3:] + str(j1)
        if try_to_add_key(new_str):
            ans_key += str(j1)
            return ans_key

        for j2 in range(0,10):
            new_str = ans_key[-2:] + str(j1) + str(j2)
            if try_to_add_key(new_str):
                ans_key += (str(j1) + str(j2))
                return ans_key

            for j3 in range(0,10):
                new_str = ans_key[-1:] + str(j1) + str(j2) + str(j3)
                if try_to_add_key(new_str):
                    ans_key += (str(j1) +  str(j2) + str(j3))
                    return ans_key

                for j4 in range(0,10):
                    new_str = str(j1) + str(j2) + str(j3) + str(j4)
                    if try_to_add_key(new_str):
                        ans_key += (str(j1) +  str(j2) + str(j3) + str(j4))
                        return ans_key 
    assert(2>3)

def main():
    ans_key = '0123456789'
    for i in range(0,10000):
        ans_key = find_next_key(ans_key)

    return ans_key

if __name__ == '__main__':
    ans_key = main()
    print(existing_keys)
    print(len(existing_keys))
    print(len(ans_key))

