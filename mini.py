@app.patch("/upd")
def update():
    data = request.get_json();
    update(data);
    return("update");