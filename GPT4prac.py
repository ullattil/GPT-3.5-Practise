import os
import openai

openai.api_key = "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"

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


## Practising with the messages array   
completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",

    # messages = [
    #     {"role" : "system", "content" : "You are a helpful Assitant." },
    #     {"role" : "user", "content": "Who won the football world cup in 2014?"},
    #     {"role" : "assistant", "content": "Germany won the football world cup in 2014"},
    #     {"role" : "user", "content" : "Where was it played?"}
    # ]

    ## Example differentiating explicit instructions from less clear instructions
    # messages = [
    #     {"role": "system", "content": "You are a helpful assistant."},
    #     {"role": "user", "content": "List the steps to make a cup of tea."}
    # ]

    messages = [
        {"role": "system", "content": "You are a helpful assistant that translates English to French."},
        {"role": "user", "content": 'Translate the following English text to French: "Hello, how are you?"'}
    ]
)

print(completion.choices[0].message.content)