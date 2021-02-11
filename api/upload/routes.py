from fastapi import APIRouter, HTTPException, Body, File, UploadFile
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from .models import Data, File_Upload

from api.authentication.models import User
from api.database import get_session
from .depends import get_user

import csv
import os
import aiofiles


router = APIRouter()


@router.post('/upload')
async def upload_csv(
    file: UploadFile = File(...),
    user: User = Depends(get_user),
    session: Session = Depends(get_session)
):
    if file.content_type == "text/csv":

        file_content = await file.read()
        file_location = "tmp"

        if not os.path.exists(file_location):
            os.makedirs(file_location)

        async with aiofiles.open(
            f'{file_location}/{file.filename}',
            'wb'
        ) as out_file:

            global file_id

            await out_file.write(file_content)  # async write

            file_database = File_Upload(
                id_user=user.id,
                nom=file.filename
            )

            session.add(file_database)
            session.commit()

            file_id = file_database.id

        nb_line = 0

        with open(f'{file_location}/{file.filename}', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                if nb_line > 0:
                    print(row)
                    data = Data(
                        id_file=file_id,
                        information=row[1],
                        valeur=row[2]
                    )
                    session.add(data)
                    session.commit()

                nb_line += 1

    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid file MIME type"
        )
