maximum=99999999999999
def ClosestPair(list, no_el, key):
    res_1, res_r=0, 0
    l, r, diff=0, no_el-1, maximum
    while r>1:
        if abs(list[l]+list[r]-key)<diff:
            res_l=l
            res_r=r
            diff=abs(list[l]+list[r]-key)
        if list[l]+list[r]>key:
            r-=1
        else:
            l+=1


    print('The closest pair is {} and {}'.format(list[res_l], list[res_r]))

if  __name__=='__main__':
    list=[7, 18, 65, 84, 87, 91, 99, 113]
    no_el=len(list)
    key=150
    ClosestPair(list, no_el, key)