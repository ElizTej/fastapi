from pyexpat import model
from fastapi import APIRouter, Depends, status, HTTPException, Response, APIRouter
from requests import Session
from .. import schemas, database, models, oath2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oath2.get_current_user)):
    
    searched_vote = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not searched_vote:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post {vote.post_id} not found!')

    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
   
    found_vote = vote_query.first()
    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f'Users {current_user.id} has alredy voted for {vote.post_id}')
        new_vote = models.Vote(post_id = vote.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {"Message": "Succesfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Vote does not exist!')
        
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"Message": "Succesfully deleted vote"}
