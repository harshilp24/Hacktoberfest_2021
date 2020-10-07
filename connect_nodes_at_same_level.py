def connect(root):
    q=[]
    q.append(root)
    while q:
        cur_len=len(q)
        for i in range(cur_len):
            ele=q[0]
            if i!=cur_len-1:
                ele.nextRight=q[1]
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)
            q.pop(0)
