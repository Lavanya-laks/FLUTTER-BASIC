def update(data):
    query = f'updata students set name ={data["name"]}where rollno = "{data["roll no"]}"';
    cur = con.cursor();
    cur.execute(query);
    con.commit();
    