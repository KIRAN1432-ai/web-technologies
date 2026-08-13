student_records=[{'name':'keny','score':85},
                 {'name':'harry','score':87},
                 {'name':'joe','score':53},
                 {'name':'Marcus','score':48},
                 {'name':'Clara','score':90}]
filtered=list(filter(lambda x:x['score']>=60,student_records))
updated=list(map(lambda s:{**s,"grade":"pass"},filtered))
print(sorted(updated,key=lambda x:x['score'],reverse=True))