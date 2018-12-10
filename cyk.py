#placeholder

import sys

'''
This function takes in a filename, the contents of that file
being a context-free grammar on CNF, and returns a created dictionary
pertaining to that particular ruleset.
'''
def read_cfg(filename):
    cfg_dict = {}
    infile = open(filename, "r")
    for line in infile:
        line_split = line.split(':')
        cfg_dict[line_split[0]] = (line_split[1].strip().split('|'))
    return cfg_dict

def create_trellis(instr):
    return [[list() for i in range(len(instr))] for j in range(len(instr))]

def print_trellis(instr, trellis):
    print('{:>10}'.format(' '), end='')
    for letter in instr:
        print('{:>10}'.format(letter), end='')
    print()
    for i, row in enumerate(trellis):
        print('{:>10}'.format(instr[i]), end='')
        for item in row:
            print('{:>10}'.format(','.join(item)), end='')
        print()


def populate_trellis(cfg_dict, trellis, instr):
    # initial population of trellis
    # could incorporate into the main loop, but I'd rather not
    for i in range(len(instr)):
        curr_substr = instr[i]
        for lhs, rhs in cfg_dict.items():
            if curr_substr in rhs:
                trellis[i][i].append(lhs)
    print("INITIAL TRELLIS, ITER 1\n")
    print_trellis(instr, trellis)



    # for step 2 to n
    for length in range(2, len(instr)+1):
        # for i =1 to (n-step+1)
        for i in range(len(instr)+1-length):
            for k in range(i, i+length-1):
                # Gather rules found at given indices
                item_one = trellis[i][k]
                item_two = trellis[k+1][i+length-1]
                # Loop over sets of items found at trellis indices
                # this is safe since CNF requires each rule to nonterminals
                # be of the form A->BC, namely 2 RHS nonterminals
                for first_item in item_one:
                    for second_item in item_two:
                        # Loop over all rules
                        for lhs, rhs in cfg_dict.items():
                            # Loops over possible RHS'S, since there are OR's
                            for possible_rhs in rhs:
                                # If the concatonated items form RHS of a rule, it's a match
                                if first_item+second_item == possible_rhs or second_item+first_item == possible_rhs:
                                    trellis[i][i+length-1].append(lhs)
    print("FINAL TRELLIS, ITER N\n")
    print_trellis(instr, trellis)
    return trellis

if __name__ == "__main__":
    assert (len(sys.argv) > 2), "Insufficient arguments"
    cfg_filename = sys.argv[1]
    instr = sys.argv[2]
    cfg_dict = read_cfg(cfg_filename)
    print("YOUR INPUT CFG IS AS FOLLOWS")
    for key, value in cfg_dict.items():
        print('\t',key, value)
    init_trellis = create_trellis(instr)
    final_trellis = populate_trellis(cfg_dict, init_trellis, instr)
    print("YES" if "S" in final_trellis[0][len(instr)-1] else "NO")