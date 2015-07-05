l=[];addItem=lambda i:l.append(i);deleteItem=lambda i:None if i not in l else l.remove(i);n=lambda s:None;viewList=lambda:n([print(i)for i in l]);
# or
l=[];addItem=l.append;deleteItem=l.remove;viewList=lambda:print('\n'.join(l))
