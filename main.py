import datetime
import uuid
from typing import *

import fastapi
from fastapi import FastAPI

from database import tel_col
from models import TelmeteringLogDb, TelmeteringLogIn

app = fastapi.FastAPI(title='ItsWA 遥测程序')


@app.get('/', name='获取自己的遥测记录', response_model=List[TelmeteringLogDb])
async def get_telemetry(client_id: str):
    return await tel_col().find({"client_id": client_id}).to_list(None)


@app.post('/', name='上传自己的遥测记录', response_model=TelmeteringLogDb)
async def post_telemetry(telemetry_in: TelmeteringLogIn, request: fastapi.Request):
    telemetry_db = TelmeteringLogDb(**telemetry_in.model_dump(),
                                    ip=request.client.host, time=datetime.datetime.now(), id=uuid.uuid4())
    await tel_col().insert_one(telemetry_db.model_dump(mode='json'))

    return await tel_col().find_one({'id': telemetry_db.id.__str__()})


@app.delete('/{id}', name='删除自己的遥测记录', response_model=TelmeteringLogDb)
async def delete_telemetry(id: uuid.UUID):
    deleted_telemetry = await tel_col().find_one({'id': id.__str__()})
    await tel_col().delete_one({'id': id.__str__()})

    return deleted_telemetry
