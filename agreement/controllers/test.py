from agreement import app


@app.route('/')
def test():
    return "hello world"
