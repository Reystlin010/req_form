import uvicorn
from fastapi import FastAPI, Request
from typing import Annotated
from standarting_phone import unify_phone
from fastapi.responses import Response


app = FastAPI()


@app.get("/unify_phone_from_cookies")
async def return_the_phone(request: Request):
    phone_data = request.headers.get('Cookie')
    if phone_data:
        unified_phone = unify_phone(phone_data.split("=")[1]) 
        response = Response(
            f"{unified_phone}",
            media_type = "text/html"
        )
        return response
    else:
        return Response("not ok")

    
if __name__ == "__main__":
    uvicorn.run(app, host="195.135.253.40", port=8000)

# 195.135.253.40