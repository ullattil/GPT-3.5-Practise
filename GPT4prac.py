import os
import openai
import json
import time

openai.api_key = "OPENAI_API_KEY"

## Practising with response characteristics and quality
# completion = openai.ChatCompletion.create(
#     model = "gpt-3.5-turbo",
#     messages = [
#         {"role" : "user", "content" : "Tell me a Joke."},
#         {"role" : "assistant", "content": "Knock-Knock."},
#         {"role" : "user", "content" : "Who's There?"}
#     ],


#     ### Contols the Response Characteristics 

#     ## Temperature controls the randomness of the generated response
#     # temperature = .9

#     ## Top_p controls the randomness of the response using nucleous sampling
#     # top_p = 0.9

#     ## controls the length of the response
#     # max_tokens = 50

#     ### Controls the Response Quality

#     ## Presence Penalty: Controls the probability of new tokens based on whether they appear in the text already
#     # presence_penalty = 0.50

#     ## Frequency Penalty: Controls the probability of new tokens based on how often they appear in the text already
#     # frequency_penalty = 0.50

#     ## Logit Bias: modifly the likelihood of specific tokens appearing in the completion. Accepts JSON object with 
#     ## an associated bias which is number from -100 to 100. Bias is added to logits prior to sampling
#     # logit_bias = { tokeniser.encode("example_token")[0] : 2.0 }
# )
# # Print the message
# print(completion.choices[0].message.content)

# ## Practising with the messages array   
# completion = openai.ChatCompletion.create(
#     model = "gpt-3.5-turbo",

#     # example prompt
#     # messages = [
#     #     {"role" : "system", "content" : "You are a helpful Assitant." },
#     #     {"role" : "user", "content": "Who won the football world cup in 2014?"},
#     #     {"role" : "assistant", "content": "Germany won the football world cup in 2014"},
#     #     {"role" : "user", "content" : "Where was it played?"}
#     # ]

#     # # Model have no memory of previous conversations so it is better to use the messages array to build context.  
#     # # Models also perform much better with explicit instructions as it explains the context better.
#     # messages = [
#     #     {"role": "system", "content": "You are a helpful assistant."},
#     #     {"role": "user", "content": "List the steps to make a cup of tea."}
#     # ]

#     # messages = [
#     #     {"role": "system", "content": "You are a helpful assistant that translates English to French."},
#     #     {"role": "user", "content": 'Translate the following English text to French: "Hello, how are you?"'}
#     # ]


#     # ## How to generate multiple responses at once using n parameter
#     # messages=[
#     #     {"role": "system", "content": "You are a helpful assistant."},
#     #     {"role": "user", "content": "Give me three different ways to prepare eggs."}
#     # ],
#     # n=3
# )

# # Access and print each completion for multiple completions
# for index, choice in enumerate(completion.choices):
#     print(f"Completion {index + 1}: \n")
#     print(choice.message["content"])
#     print()

# # Accessing the n-th completion
# completion.choices[n].message["content"]
## Streaming responses instead of waiting for the API call to finish

response=openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages=[
        {"role":"user","content":"Count to a ten in Russian, with new line after each number while also displaying their indo-numberic alphabet. Eg: 1: Russianword for one (pronounciation)"}
    ],
    temperature=0,
    stream=True
)


collected_chunks=[]
collected_messages =[]

# # Open AI tutorial
# start_time=time.time()
# for chunk in response:
#     chunk_time = time.time() - start_time  # calculate the time delay of the chunk
#     collected_chunks.append(chunk)  # save the event response
#     chunk_message = chunk['choices'][0]['delta']  # extract the message
#     collected_messages.append(chunk_message)  # save the message
#     print(f"Message received {chunk_time:.2f} seconds after request: {chunk_message}")  # print the delay and text
#     # print(chunk_message.content,end="")

# # print the time delay and text received
# print(f"Full response received {chunk_time:.2f} seconds after request")
# full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
# print(f"Full conversation received: {full_reply_content}")

for chunk in response:
    collected_chunks.append(chunk)
    chunk_message=chunk['choices'][0]['delta']
    collected_messages.append(chunk_message)
    try:
       print(chunk_message.content,end="")
    except AttributeError:
        pass
            

