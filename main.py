import httpx
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks, Request
from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine
from fastapi import Header
from gerador_accesstoken import refresh_access_token


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/refresh_token")
async def get_new_acess_token():
    try:
        new_token = refresh_access_token()
        return {"new_access_token": new_token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("")
def read_root():
    return {"message": "Sua Mensagem para a API"}


@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db=Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db=Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: SessionLocal = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario nao encontrado")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: SessionLocal = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.put("/users/{user_id}")
def update_user(user_id: int, user):
    return {"user_id": user_id, "updated_user": user}


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "updated_item": item}


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks, write_notification=None):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"item_id": item_id, "message": "Item deletado com sucesso."}


# Mercado Livre PUB Produtos


@app.get("/items/{item_id}")
async def get_item_info(item_id: str):
    link = f"https://api.mercadolibre.com/items/{item_id}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(link)
            return {"status_code": response.status_code, "content": response.text}
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Erro ao fazer requisição: {str(e)}")


@app.post("/post_mercadolibre_items")
async def post_mercadolibre_items(data: dict, authorization: str = Header(refresh_access_token)):
    url = "https://api.mercadolibre.com/items"
    headers = {"Authorization": authorization}
    print(headers)
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=data, headers=headers)
            return {"status_code": response.status_code, "content": response.text}
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Erro ao fazer requisição: {str(e)}")


@app.get("/category")
async def category(category_id: str):
    url = f"https://api.mercadolibre.com/categories/{category_id}"
    async with httpx.AsyncClient() as client:
        try:
            await client.get(url)
            return "status_code"
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Erro ao fqazer requisição: {str(e)}")


# Detalhe Categoria
@app.get("/categories_detal")
async def categories_detal(category_id: str):
    url = f"https://api.mercadolibre.com/categories/{category_id}"
    async with httpx.AsyncClient() as client:
        try:
            await client.get(url)
            return "status_code"
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Erro ao fazer requisição: {str(e)}")


# Precos

@app.get("/get_sale_price/{item_id}")
async def get_sale_price(item_id: str):
    url = f"https://api.mercadolibre.com/items/{item_id}/sale_price"
    async with httpx.AsyncClient() as client:
        try:
            await client.get(url)
            return "status_code"
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Erro ao fazer requisição: {str(e)}")


# Criar descrição
@app.post("/update_description/{item_id}")
async def update_description(item_id: str, description: dict, authorization: str = Header(refresh_access_token)):
    url = f"https://api.mercadolibre.com/items/{item_id}/description"
    headers = {"Authorization": authorization}
    print(headers)
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=description, headers=headers)
            return {"status_code": response.status_code, "content": response.text}
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Erro ao fazer a requisição: {str(e)}")


@app.get("/consult_description/{item_id}")
async def consult_description(item_id: str):
    url = f"https://api.mercadolibre.com/items/{item_id}/description"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            return {"status_code": response.status_code, "content": response.text}
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Erro ao fazer a requisição: {str(e)}")


@app.put("/sub_desc_exist/{item_id}")
async def sub_desc_exist(item_id: str, authorization: str = Header(refresh_access_token)):
    url = f"https://api.mercadolibre.com/items/{item_id}/description?api_version=2"
    headers = {"Authorization": authorization}
    print(headers)
    async with httpx.AsyncClient() as client:
        try:
            await client.put(url, json=update_description, headers=headers)
            return "status_code"
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Erro ao fazer requisição com sucesso: {str(e)}")
