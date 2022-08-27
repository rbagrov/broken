import fastapi, pydantic

app = fastapi.FastAPI()



class _data(pydantic.BaseModel):
    text: str


    class Config:
        schema_extra = {
            "example": {
                "test": "secret text with password",
            }
        }


@app.post("/parser/")
async def parserHandler(data: _data):
    r = await parser(data)
    return r

async def parser(d: _data) -> str:
    import json

    with open('words.json') as j:
        data = json.load(j)
        data = data["words"]
        count = 0
        response = d.text.split(" ")
        for i in d.text.split(" "):
            for j in data:
                if i == j:
                    response[count] = "*****"
                else:
                    response[count] = i
            count += 1
    return " ".join(response)
