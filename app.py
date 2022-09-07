import fastapi, pydantic  # import libraries

app = fastapi.FastAPI() # Initialize application



class _data(pydantic.BaseModel): # create data model
    text: str


    class Config:
        schema_extra = {
            "example": {
                "test": "secret text with password",
            }
        }


@app.post("/parser/") # define endpoint name
async def parserHandler(data: _data): # Handler to handle data
    r = await parser(data)
    return r

async def parser(d: _data) -> str:
    """_summary_
    Takes data and returns formated response
    Args:
        d (_data): _description_

    Returns:
        str: _description_
    """
    import json
    try:
        with open('words.json') as j: # parse file
            data = json.load(j)
            data = data["words"]
            count = 0
            response = d.text.split(" ")
            for i in d.text.split(" "):
                for j in data:
                    if i == j: # business logic
                        response[count] = "*****"
                    else:
                        response[count] = i
                count += 1
        return " ".join(response)
    except Exception as e:
        return " "
