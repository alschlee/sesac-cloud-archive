from fastapi import APIRouter, HTTPException, Path, Query
from model import Todo, TodoItem, TodoItems

todoRouter = APIRouter()

todoList = []

# 할 일 추가
@todoRouter.post("/todo", statusCode=201)
#async def addTodo(todo: dict) -> dict:
async def addTodo(todo: Todo) -> dict:
    todoList.append(todo)
    return {"message": "할 일을 추가합니다."}

# 할 일 목록 조회
@todoRouter.get("/todo", responseModel = TodoItems)
async def getTodos() -> dict:
    return {"todos": todoList}

# 할 일 조회
@todoRouter.get("/todo/{todoId}")
async def getTodo(todoId: int = Path(..., title = "조회할 할 일의 ID", ge = 1)) -> dict: # 숫자 검증: ge(이상), le(이하), gt(초과), lt(미만), min_length(문자열이나 리스트 최소 길이), max_length(문자열이나 리스트 최대 길이), regex(문자열이 정규표현식과 일치)
    for todo in todoList:
        if todo.id == todoId:
            return {"todo": todo}
    #return {"message": "일치하는 할 일이 없습니다."}
    raise HTTPException(
        statusCode=404,
        detail="일치하는 할 일이 없습니다."
    )

# 할 일 검색
@todoRouter.get("/todo/search")
async def searchTodos(item: str = Query(..., min_length = 2, max_length = 10)) -> dict:
    print(item)
    result = []
    for todo in todoList:
        if item in todo.item:
            print(todo)
            result.append(todo)
    return {"todos": result}

# 할 일 수정
@todoRouter.put("/todo/{todoId}")
#async def updateTodo(todo: Todo, todoId: int = Path(..., title = "수정할 할 일의 ID", ge = 1)) -> dict:
async def updateTodo(todo: TodoItem, todoId: int = Path(..., title = "수정할 할 일의 ID", ge = 1)) -> dict:
    for todo in todoList:
        if todo.id == todoId:
            todo.item = todo.item
            return {"message": "할 일을 수정합니다."}
    #return {"message": "일치하는 할 일이 없습니다."}
    raise HTTPException(
        statusCode=404,
        detail="일치하는 할 일이 없습니다."
    )

# 할 일 삭제
@todoRouter.delete("/todo/{todoId}")
async def deleteTodo(todoId: int = Path(..., title = "삭제할 할 일의 ID", ge = 1)) -> dict:
    for t in todoList:
        if t.id == todoId:
            todoList.remove(t)
            return {"message": "할 일을 삭제했습니다."}
    #return {"message": "일치하는 할 일이 없습니다."}
    raise HTTPException(
        statusCode=404,
        detail="일치하는 할 일이 없습니다."
    )