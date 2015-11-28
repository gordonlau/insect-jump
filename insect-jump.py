#!/usr/bin/python




def iterate_count(step_set,target):
    ''' Count the possible combination for insect jump problem
    >>> iterate_count([1,2,3],5)
    13
    >>> iterate_count([],5)
    0
    >>> iterate_count([1,2,3],0)
    0
    >>> iterate_count([1,2,3],-1)
    0
    '''
    if target < 0:
        return 0
    count = 0
    for step in step_set:
        if target - step == 0:
            count += 1
        else:
            count += iterate_count(step_set,target-step)
    return count



def iterate_jump(step_set,target,step_sequence=[]):
    ''' Display all the possible combination in a list of result
    >>> iterate_jump([1,2,3],3)
    [[1, 1, 1], [1, 2], [2, 1], [3]]
    >>> iterate_jump([],3)
    []
    >>> iterate_jump([1,2,3],0)
    []
    >>> iterate_jump([1,2,3],-1)
    []
    '''
    if target < 0:
        return []
    results = []
    for step in step_set:
        if target - step == 0:
            results += [step_sequence + [step]]
        else:
            results += iterate_jump(step_set, target-step,step_sequence +[step])
    return results



if __name__ == "__main__":
    import doctest
    doctest.testmod()