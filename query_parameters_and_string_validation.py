from fastapi import FastAPI, Query
from typing import Annotated
app= FastAPI()

@app.get("/items/")

# async def read_items(q: str | None = None)

# Without annotated
# async def read_items(q: str | None= Query(default= None, max_length= 50)):

# With annotated
async def read_items(q: Annotated[list[str] | None, Query(min_length= 3, max_length= 50)]= None):   # Both of these versions mean the same thing, q is a parameter that can be a str or None, and by default, it is None.
    results={"items":[{"itemn1": "Mouse"}, {"item2": "Keyboard"}]}
    if q:
        results.update({"q": q})
    return results


# Can add default value in annotated as "Electronics", can add None as default too.

# Added more validation- min_length

# Added regular expressions with pattern of "item-" as pattern="^item-" inside  Query.
# pattern is a validation rule for a single string, not for a list of strings.

# When you need to declare a value as required while using Query, you can simply not declare a default value.

# You can declare that a parameter can accept None, but that it's still required. This would force clients to send a value, even if the value is None.
# To do that, you can declare that None is a valid type but simply do not declare a default value

# The main reason to use list[str] in a query parameter is to allow the client to send multiple values for the same parameter.

# min_length=3 so we have to provide atleast 3 values in list.


@app.get("/items2/")
# Query paramater list with defaults
async def read_items2(q: Annotated[list[str], Query(include_in_schema= False)]= ["Laptop", "Mobile", "Camera"]):
    query_items= {"q": q}
    return query_items

# You can also use list directly instead of list[str]
# async def read_items(q: Annotated[list, Query()] = []):

# You can add more information about the parameter like title, description inside Query()

# alias in Query() lets you give a query parameter a different name in the URL while keeping a 
# different variable name in your Python code.

# deprecated= True means parameter that still works, but should no longer be used. It is kept only for compatibility with older clients.

# include_in_schema= True in Query() controls whether a parameter appears in the API documentation (Swagger UI/OpenAPI schema)
# shows no parameter in UI.