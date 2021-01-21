class My_sort:
    
    @classmethod
    def merge_sort(cls, lst):
        
        if len(lst) <= 1 :
            return lst
        else :
            sub_lst1 = lst[:len(lst)//2]
            sub_lst2 = lst[len(lst)//2:]

            sblst1 = cls.merge_sort(sub_lst1)
            sblst2 = cls.merge_sort(sub_lst2)

            return cls.merging(sblst1, sblst2)
    
    @classmethod
    def merging(cls, lst1, lst2):
        
        fidx = tidx = 0
        tmp = []
        while fidx < len(lst1) and tidx < len(lst2):
            if lst1[fidx] < lst2[tidx]:
                tmp.append(lst1[fidx])
                fidx += 1
            else:
                tmp.append(lst2[tidx])
                tidx += 1
            
        if fidx == len(lst1):
            while tidx != len(lst2):
                tmp.append(lst2[tidx])
                tidx += 1
        else:
            while fidx != len(lst1):
                tmp.append(lst1[fidx])
                fidx += 1
    
        return tmp

    @classmethod
    def quick_sort(cls, lst):

        if len(lst) <= 1:
            return lst
        else:
            pivot = len(lst)//2
            pivot_num = lst[pivot]
            small_lst = []
            big_lst = []
            pivot_lst = [pivot_num]
            for i in lst:
                if i == pivot_num:
                    continue
                if i <= pivot_num:
                    small_lst.append(i)
                else:
                    big_lst.append(i)
                
            small_lst = cls.quick_sort(small_lst)
            big_lst = cls.quick_sort(big_lst)

            return small_lst + pivot_lst + big_lst
            

my_lst = [9, 17, 5, 28, 24, 37, 48, 1, 19]
sorted_lst = My_sort.quick_sort(my_lst)
# print(sorted_lst)
    