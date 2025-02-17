from fastapi import FastAPI, HTTPException, Response
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, ValidationError
from uuid import UUID, uuid4
from typing import List, Optional

app = FastAPI()

tanks = []  # List to store tank data

# Define the Tank model
class Tank(BaseModel):
    id: UUID = Field(default_factory=uuid4) #the applicationj will assign a value returned by the function as an ID
    location: str
    lat: float
    long: float

class TankUpdate(BaseModel):
    location: str | None = None
    lat: float | None = None
    long: float | None = None

@app.post("/tank", status_code=201)
async def create_tank(tank_request: Tank):
    if not tank_request.location or not tank_request.lat  or not tank_request.long :
        raise HTTPException(
            status_code=400,
            detail="400: Invalid request: Missing required fields"
        )
    
    tank_json = jsonable_encoder(tank_request) # Convert the object to a JSON-serializable format
    tanks.append(tank_json)# Store the tank in memory
    
    return {"success": True, "result": tank_json}


@app.get("/tank",status_code=200) #Retrieves data for all tanks
async def get_all_tanks():
    return tanks

@app.get("/tank/{id}", response_model=Tank,status_code=200) # Returns specific tank based on ID provided
async def get_tank(id: UUID):
    for tank in tanks:
        if tank["id"] == str(id):  # Ensure comparison with string ID
            return tank
    raise HTTPException(status_code=404, detail="Tank not found")

@app.patch("/tank/{id}", response_model=Tank)
async def update_tank(id: UUID, tank_update: TankUpdate):
    for i, tank in enumerate(tanks):
        if tank["id"] == str(id):
            tank_update_dict = tank_update.model_dump(exclude_unset=True)
            updated_tank = {**tank, **tank_update_dict}# Merge updates with existing tank data
            tanks[i] = jsonable_encoder(updated_tank)# Save updated tank
            return updated_tank
    raise HTTPException(status_code=404, detail="Tank not found")

@app.delete("/tank/{id}")
async def delete_tank(id: UUID):
    for tank in tanks:
        if tank["id"] == str(id):
            tanks.remove(tank)
            return Response(status_code=204)
    raise HTTPException(status_code=404, detail="Tank not found")
