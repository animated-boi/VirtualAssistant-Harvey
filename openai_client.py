from openai import OpenAI
import creds

def aiProcessing(command):
    
    client = OpenAI(api_key = creds.key_openapi)

    response = client.responses.create(
        model="gpt-4.1-nano",
        input=command
    )
    
    return(response.output_text)
