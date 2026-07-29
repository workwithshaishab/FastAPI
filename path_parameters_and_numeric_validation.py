from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(item_id: Annotated[int, Path(title= "ID of the item to get", gt=0, le=1000)],
                     q: Annotated[str | None, Query(alias= "item-query")]= None):
# Order the parameter as you need, it doesn't matter whether item_id comes first or q comes first.
    results={"item_id": item_id}
    if q:
        results.update({"q":q})
    return results


# Number validations also work for float values.