import openai

# openai.api_key = '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'

openai.organization = "Personal"

openai.api_key = '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'

def generate_blog(topic):
    response = openai.Completion.create(
    model = 'text-ada-001',
    prompt = 'Write a paragraph about the following topic. ' + topic,
    max_tokens = 200,
    temperature = 0.5)

    paragraph = response.choices[0]

    return paragraph


print(generate_blog('What is addition?'))