# Problem Set 4A
# Name: Ali Kalaycı

# This problem was taken from MIT 6.0001 Fall 2016 course
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/ 
# Function names and instructions to write functions are given.
# I wrote code according to them.

def get_permutations(seqn):
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
    if len(seqn)<=1: 
        return [seqn]
    else:
        perm= []
        for a in get_permutations(seqn[1:]):
            for i in range(len(a)+1):
                perm.append(a[:i]+ seqn[0]+ a[i:])
        return perm

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

