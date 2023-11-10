from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
import models
from database import get_db
from schemas import Details,ShowDetails
from typing import List


router=APIRouter(
    tags=['details']
)

@router.post('/',status_code=status.HTTP_201_CREATED)
async def post_details(request:Details,db:Session=Depends(get_db)):
    new_details=models.Details(lastname=request.lastname,firstname=request.firstname,email=request.email)
    db.add(new_details)
    db.commit()
    db.refresh(new_details)
    return new_details

@router.get('/',response_model=List[ShowDetails])
def get_all_blogs(db:Session=Depends(get_db)):
    all_details=db.query(models.Details).all()
    return all_details

