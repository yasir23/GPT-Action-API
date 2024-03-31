
# BEST PRACTICES FOR MAKING STRUTURE OF PROMPTES TO GET RESULT:

https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api

# 1: Summarize the text below as a bullet point list of the most important points.

Text: """
{text input here}
"""

# 2: Be specific, descriptive and as detailed as possible about the desired context, outcome, length, format, style, etc 
Write a short inspiring poem about OpenAI, focusing on the recent DALL-E product launch (DALL-E is a text to image ML model) in the style of a {famous poet}

# 3: Articulate the desired output format through examples
Extract the important entities mentioned in the text below. First extract all company names, then extract all people names, then extract specific topics which fit the content and finally extract general overarching themes

Desired format:
Company names: <comma_separated_list_of_company_names>
People names: -||-
Specific topics: -||-
General themes: -||-

Text: {text}

# 4: Start with zero-shot, then few-shot, neither of them worked, then fine-tune

Extract keywords from the below text.

Text: {text}

Keywords:

# 5: ✅ Few-shot - provide a couple of examples

Extract keywords from the corresponding texts below.

Text 1: Stripe provides APIs that web developers can use to integrate payment processing into their websites and mobile applications.
Keywords 1: Stripe, payment processing, APIs, web developers, websites, mobile applications
##
Text 2: OpenAI has trained cutting-edge language models that are very good at understanding and generating text. Our API provides access to these models and can be used to solve virtually any task that involves processing language.
Keywords 2: OpenAI, language models, text processing, API.
##
Text 3: {text}
Keywords 3:

# 6: ✅Fine-tune: see fine-tune best practices here.

https://platform.openai.com/docs/guides/fine-tuning

# 7: Reduce “fluffy” and imprecise descriptions

Use a 3 to 5 sentence paragraph to describe this product.

# 8: Instead of just saying what not to do, say what to do instead

The following is a conversation between an Agent and a Customer. The agent will attempt to diagnose the problem and suggest a solution, whilst refraining from asking any questions related to PII. Instead of asking for PII, such as username or password, refer the user to the help article www.samplewebsite.com/help/faq

Customer: I can’t log in to my account.
Agent:


# 9: Code Generation Specific - Use “leading words” to nudge the model toward a particular pattern


# Write a simple python function that
# 1. Ask me for a number in mile
# 2. It converts miles to kilometers
 
import

# 10: Parameters 

Generally, we find that model and temperature are the most commonly used parameters to alter the model output.

model - Higher performance models are generally more expensive and may have higher latency.

temperature - A measure of how often the model outputs a less likely token. The higher the temperature, the more random (and usually creative) the output. This, however, is not the same as “truthfulness”. For most factual use cases such as data extraction, and truthful Q&A, the temperature of 0 is best.

max_tokens (maximum length) - Does not control the length of the output, but a hard cutoff limit for token generation. Ideally you won’t hit this limit often, as your model will stop either when it thinks it’s finished, or when it hits a stop sequence you defined.

stop (stop sequences) - A set of characters (tokens) that, when generated, will cause the text generation to stop.

For other parameter descriptions see the API reference. 

























