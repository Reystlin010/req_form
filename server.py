import uvicorn
from fastapi import FastAPI, Form
from standarting_phone import unify_phone
from fastapi.responses import Response


app = FastAPI()


@app.post("/unify_phone_from_form")
def return_the_phone(phone: str = Form(...)):
    # content_type = .headers.get('Content-Type')

    # if content_type is None:
        # return 'No content-type provided'
    # elif content_type == "multipart/form-data":
        try:
            unified_phone = unify_phone(phone) 
            response = Response(
                f"{unified_phone}",
                media_type = "text/html"
            )
            return response
        except ValueError:
            return "Invalid data"
    # else:
        # return "Content-Type not supported"
    
if __name__ == "__main__":
    uvicorn.run(app, host="195.135.253.40", port=8000)