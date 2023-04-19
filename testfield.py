import uvicorn
from fastapi import FastAPI
from standarting_phone import unify_phone
from fastapi.responses import Response


app = FastAPI()


@app.get("/unify_phone_from_query")
def return_the_phone(phone = str):
    unified_phone = unify_phone(phone) 
    response = Response(
        f"{unified_phone}",
        media_type = "text/html"
    )
    return response

    
if __name__ == "__main__":
    uvicorn.run(app, host="195.135.253.40", port=8000)