file=open("�צאט WhatsApp עם יום הולדת בנות לנויה.txt",encoding='utf8')       
def partychat (file):
    import json
    lst = []
    user_dict = dict()
    user_id = 0
    full_info = dict()
    for line in file:
            flag = None
            try:
                if ("<המדיה לא נכללה>" in line or "הוסיף/ה" in line
                        or "ההודעות והשיחות מוצפנות מקצה-לקצה" in line or "נוצרה על ידי" in line):
                    continue
                message = dict()
                date_index = line.index('-')
                date = line[0:date_index]
                tele = line[date_index + 1:line.index(':', date_index)]
                text = line[line.index(':', date_index) + 1:]
                for key, value in user_dict.items():
                    if value == tele:
                        flag = key
                if flag is not None:
                    tele = flag
                else:
                    user_dict[user_id] = tele
                    tele = user_id
                    user_id += 1
                message['datetime'] = date
                message['id'] = tele
                message['text'] = text
                lst.append(message)
            except:
                lst[-1]['text'] += line


    file=open("�צאט WhatsApp עם יום הולדת בנות לנויה.txt",encoding='utf8')       
    for line in file:
        if not  "נוצרה על ידי"  in line:
            continue
        metadata = dict()
        chatname_index = line.split('"')
        chatname = chatname_index[1]
        metadata["chat_name"] = chatname
        creationdate = line.split('-')
        metadata["creation_date"]=creationdate[0]
        metadata["num_of_participants"]=user_id+1
        creator_index=line.index('ידי')
        metadata["creator"]=line[creator_index+6:creator_index+22]

    full_info["messages"] = lst 
    full_info["metadata"] = metadata
    file_in_json = chatname+".txt"
    outputfile = open(file_in_json, 'w', encoding='utf8')
    outputfile.write(json.dumps(full_info, indent=4, ensure_ascii=False))
    outputfile.close()
    return(full_info)
partychat(file)