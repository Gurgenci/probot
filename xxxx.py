from openai import OpenAI

client = OpenAI(api_key="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")

# Set your API key


def text_complete(prompt):
    # Use the GPT-3 language model to generate text
    model_engine = "text-davinci-002"
    completions = client.completions.create(engine=model_engine, 
    prompt=prompt, 
    max_tokens=2048,
    temperature=0,
    top_p=0,
    logprobs=10)
    return completions;
if False:
    z=text_complete("The capital city of Queensland is Brisbane, of NSW ")
    print(z.choices[0].text)

def image_gen(prompt, n=1, size="1024x1024"):
    response=client.images.generate(prompt=prompt,n=n,size=size)
    return response
if True:
    z=image_gen("A pet rainbow lorikeet scared by a raven and flying away from the garden with its lady owner watching in desperation and anguish")
    print(z['data'][0]['url'])
