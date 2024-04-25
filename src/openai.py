from openai import OpenAI
import src.settings as settings

client = OpenAI(api_key=settings.OPEN_AI_KEY)


def generate_embeddings(text: str) -> list[float]:
    response = client.embeddings.create(model="text-embedding-ada-002", input=text)

    return response.data[0].embedding
