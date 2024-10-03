import os
from dotenv import load_dotenv
from farcaster import Warpcast
from openai import OpenAI
import requests
import json

load_dotenv()
#url = 'https://pathna-bot-nextjs.vercel.app/api/openai'

warpcastClient = Warpcast(mnemonic=os.environ.get("MNEMONIC_ENV_VAR"))
openaiClient = OpenAI(api_key=os.environ.get("OPENAI_ENV_VAR"))
contextA = 'You are a system algorithm that filters out some key components from a given text and return with a json file containing those key components. Only respond with the context of the text that contains: Title - Make an instructional summary of the entire message as a short title, Claims - Number of claims stated for rewards, Deadline - Must give the stated deadline in hours, days or months format - use 14 days as default if deadline is not stated, Reward - The reward from the text, make it the total prize pool. Respond with a json structure.'


contextB = '''Confirmed! On your bounty page, you can pay users and view their bounty completion history

🤖 commands
- @pathnabot cancel
- @pathnabot in progress
- @pathnabot complete (optional: tag winners)
- @pathnabot shoutout (optional: tag winner and write a positive review)'''

for cast in warpcastClient.stream_casts():
    # If it's a question about the bot's capabilities call FLock, else use OpenAI
    #if cast and "@pathnabot what" in cast.text:
    #    if cast.parent_hash is not None:
    #        questionToApi = {'question': cast.text[11:]}
    #        answer = requests.post(url=url, json=questionToApi)
    #        response = warpcastClient.post_cast(text=answer.json()['answer'], parent={
    #            "fid": 397823,
    #            "hash": cast.hash
    #         }) 
    #elif 
    
    if cast and "@pathnabot" in cast.text and cast.author.fid != 397823:
        if cast.parent_hash is not None:
            parentCastText = warpcastClient.get_cast(cast.parent_hash).cast.text
            completion = openaiClient.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": contextA},
                    {"role": "user", "content": parentCastText}
                ])
            translatedText = completion.choices[0].message.content
            #TODO: parse or export the json text/file: 'translatedText' here 
            if len(translatedText) != 0:
                response = warpcastClient.post_cast(text=contextB, parent={
                "fid": 397823,
                "hash": cast.hash
                })