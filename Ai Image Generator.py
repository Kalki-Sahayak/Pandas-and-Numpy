from openai import  OpenAI
openai = OpenAI(
    api_key="AIzaSyBr99tkDS9RQX_lTHdr1RmDu-E2i43ACBo")

r = openai.images.generate(
    model= "dall-e-3",
    prompt ="An Astronaut eating a burger in Space"
)

print (r.data[0].url)