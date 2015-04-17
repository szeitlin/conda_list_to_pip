#script to convert conda list of requirements to format that pip likes

with open('requirements.txt','r') as conda_list:
    for row in conda_list:
        if row[0]=='#':
            continue
        else:
            item = ','.join(row.split())
            itemlist = item.split(',')
            with open('pip_requirements.txt','a') as pip_req: 
                pip_req.write(itemlist[0]+'=='+itemlist[1]+'\n')
