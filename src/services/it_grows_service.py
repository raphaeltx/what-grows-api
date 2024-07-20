from datetime import datetime
from src.models.coordenates_dto import CoordenatesDTO
from src.repositories.openai_repository import OpenAIRepository

class ItGrowsService:
  def __init__(self):
    self.openai_repository = OpenAIRepository()

  def what_grows(self, dto: CoordenatesDTO):
    now = self.get_current_date()

    prompt = """Return to me a list of objects in json with 5 items (only the json list, nothing more), 
      with suggestions of what are the best vegetables to grow given my location: latitude %s and longitude %s and the date %s. 
      Each object of the list must contain the property soil_humidity with the recommended percentage soil humidity and 
      the property name with the value of the name of the vegetable.""" % (dto.latitude, dto.longitude, now)
    
    output = self.openai_repository.what_grows(prompt)
    output_json_str = output.choices[0].text

    return output_json_str
  
  def get_current_date(self):
    now = datetime.now()
    formatted_date = now.strftime("%m/%d/%Y")

    return formatted_date