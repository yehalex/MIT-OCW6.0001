# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if (len(sequence) <= 1):
        return [sequence]
    else:
        a = sequence[0]
        l = get_permutations((sequence[1:]))
        perm_l = []
        for i in range (len(l)):
            for j in range(len(l[i])+1):
                perm_l.append(l[i][:j] + a + l[i][j:])
        return perm_l
            

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = 'c'
    print('Input:', example_input)
    print('Output:', get_permutations(example_input))

    example_input = 'aeiou'
    print('Input:', example_input)
    print('Output:', get_permutations(example_input))

    example_input = 'cdf'
    print('Input:', example_input)
    print('Output:', get_permutations(example_input))
    
    example_input = 'bust'
    print('Input:', example_input)
    print('Output:', get_permutations(example_input))
    
    example_input = 'abcd'
    print('Input:', example_input)
    print('Output:', get_permutations(example_input))

