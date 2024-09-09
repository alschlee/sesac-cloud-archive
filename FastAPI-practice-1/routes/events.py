from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, status

from auth.authenticate import authenticate
from database.connection import getSession
from models.events import Event, EventUpdate

eventRouter = APIRouter(
    tags=["Event"]
)

events = []

# 이벤트 전체 조회 /event/ => getAllEvents()
@eventRouter.get("/", response_model = List[Event])
async def getAllEvents() -> List[Event]:
    return events

# 이벤트 상세 조회 /event/{id} => getEvent()
@eventRouter.get("/{id}", response_model = Event)
async def getEvent(id: int, session = Depends(getSession)) -> Event:
    #for event in events:
    #    if event.id == id:
    #        return event
    event = session.get(Event, id) # db에서 해당 id 데이터 조회
    if event:
        return event
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "일치하는 이벤트가 존재하지 않습니다.")

# 이벤트 등록 /event/ => createEvent()
@eventRouter.post("/", status_code = status.HTTP_201_CREATED)
async def createEvent(data: Event = Body(...), user_id = Depends(authenticate), session = Depends(getSession)) -> dict:
    # events.append(data)
    data.user_id = user_id # 사용자 id 추가
    session.add(data) # db에 데이터 추가
    session.commit() # 변경사항 저장
    session.refresh(data) # 최신 데이터로 갱신
    return {"message": "이벤트가 정상적으로 등록되었습니다."}

# 이벤트 하나 삭제 /event/{id} => deleteEvent()
@eventRouter.delete("/{id}")
async def deleteEvent(id: int, session = Depends(getSession)) -> dict:
    #for event in events:
    #    if event.id == id:
    #        events.remove(event)
    #return {"message": "이벤트가 정상적으로 삭제되었습니다."}
    event = session.get(Event, id)
    if event:
        session.delete(event)
        session.commit()
        return {"message": "이벤트가 정상적으로 삭제되었습니다."}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="일치하는 이벤트가 존재하지 않습니다.")

# 이벤트 전체 삭제 /event/ => deleteAllEvents()
@eventRouter.delete("/")
async def deleteAllEvents(session = Depends(getSession)) -> dict:
    #events.clear()
    statement = select(Event)
    events = session.exec(statement)

    for event in events:
        session.delete(event)

    session.commit()
    
    return {"message": "모든 이벤트가 정상적으로 삭제되었습니다."}

# 이벤트 수정 PUT /event/{id} => updateEvent()
@eventRouter.put("/{id}", response_model = Event)
async def updateEvent(id: int, data: EventUpdate, session = Depends(getSession)) -> Event:
    event = session.get(Event, id) # db에서 해당 id의 데이터 조회
    if event:
        event_data = data.dict(exclude_unset = True) # 전달된 데이터 중 값이 없는 부분은 제외
        for key, value in event_data.items():
            setattr(event, key, value) # 데이터 수정
        
        session.add(event)
        session.commit()
        session.refresh(event)

        return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "일치하는 이벤트가 존재하지 않습니다.")