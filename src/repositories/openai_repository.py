import os
from openai import OpenAI
from logging_config import logger
from src.models.coordenates_dto import CoordenatesDTO

class OpenAIRepository:
  def __init__(self):
    try:
      openai_api_key = os.getenv('OPENAI_API_KEY')
      logger.info('OpenAI Api Key loaded! ', openai_api_key)
      
      self.openaai_client = OpenAI(
        api_key=openai_api_key,
      )

      logger.info('OpenAI Client created!')
    except KeyError:
      logger.error('Error when trying to creat an OpenAI client: ', KeyError)

  def what_grows(self, prompt: str):
    try:
      logger.info('Executing OpenAI assistant with the prompt: ', prompt)

      output = self.openaai_client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=600
      )

      return output
    except KeyError:
      logger.error('OpenApi assistant failed with the error: ', KeyError)