from app.config import apps

@apps.app.get("/hi")
async def hi():
    return {
        'msg':'hi'
    } 

