from app.models.tracking import InputTracking, OutPutTracking, Position


def track_logic(input : InputTracking) -> OutPutTracking :
    return OutPutTracking(fullname="abolfazl andalib" , positions=[
        Position(location='bushehr , jam',datetime='2022-02-12 13:50')
    ])
