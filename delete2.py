def delete(rollno):
    query = f'delete from students where rollno = "{rollno}"';
    cur = con.cursor();
    cur.execute(query);
    con.commit();
















                      
                        