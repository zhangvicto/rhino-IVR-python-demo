import json
import logging
import asyncio
import websockets
import pvrhino
import base64
import pywav
from twilio.twiml.voice_response import VoiceResponse

access_key = "lRAuK76mw3Np9qn4zxydMlis0cWQ7tsctynI4xRIHzkDYFWePeA1XA==" # AccessKey obtained from Picovoice Console (https://console.picovoice.ai/)
handle = pvrhino.create(access_key=access_key, context_path=r'C:\Users\Victor Zhang\Documents\GitHub\picovoice-rhino-twilio\context.rhn')

# websocket
async def handler(websocket):
    while True:
        message_count = 0

        message = await websocket.recv() # JSON data 
        if message is None:
            print("No message received...")
            continue

        data = json.loads(message)

        if data['event'] == "connected":
            print("Connected Message received: {}".format(message))
        if data['event'] == "start":
            print("Start Message received: {}".format(message))
        if data['event'] == "media":
                #print("Media message: {}".format(message))
                payload = data['media']['payload']

                

                # if firsst message then we create last audio data
                # audio_data = data['media']['payload']

                # print("Payload is: {}".format(payload))
                # print("size is", 3*((len(data['media']['payload'])/4)))

                # Decode base64
                chunk = base64.b64decode(payload)
                
                # xulaw to wav
                wave_write = pywav.WavWrite("sample.wav", 1, 8000, 8, 7)
                wave_write.write(chunk)
                wave_write.close()

                print(wave_read = pywav.WavRead("sample.wav").getparas())
                # 8khz x-mulaw to 16khz pcm
                # pcm = 

                # 

                # Rhino
                # is_finalized = handle.process(pcm)

                # if is_finalized:
                #     inference = handle.get_inference()
                #     if not inference.is_understood:
                #         # add code to handle unsupported commands
                #         print("Hi! How may I help you?")
                #         pass
                #     else:
                #         intent = inference.intent
                # 
                #         if intent == "orderInquiry": 
                #           print("What is your order number?")
                #         else if intent == "orderNumber": 
                #           print("What items did you order?")
                #         else if intent == "orderItem": 
                #           if slots[item1] == "screwdriver": 
                #                print("Your order will arrive in 5 days.")
                #           if slots[item1] == "drill":  # change to if it includes
                #                print("Your order will arrive in 6 days.")
                #           print("Do you want to cancel this order?")  
                #         else if intent == "cancelOrder"        
                #         slots = inference.slots
                #         print(intent)


        if data['event'] == "closed":
            print("Closed Message received: {}".format(message))
            handle.delete()
            break

        message_count += 1

        
async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())


#base64_length

# data = {"event":"media",
#         "sequenceNumber":"1006",
#         "media": 
#             {
#               "track":"inbound",
#               "chunk":"1005",
#               "timestamp":"20177",
#               "payload":"//5+fv7+/n5+fnx8fHl5eXV6dXd3eX19+373+/b2+PL88375/X36ef15fX16/nr+ff5+//9+/Xx+fP58/31+/X37ffv9+vz8/P//fXx6enJ6cnV3dntz+nf2e/j5/PD+8H7y/Pv6/vt7/Ht+eHx2e354/H34///6efl6/Hp7fnr/dP94fn1+/n74//n8fvv9/X7+fnn6dP55fXx7/Xr7ew=="},"streamSid":"MZ3468756a85e12d386c099a5b0af8eeca"
#             },
#         "streamSid":"MZ3468756a85e12d386c099a5b0af8eeca"
#         }