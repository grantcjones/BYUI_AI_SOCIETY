#--------------------------------------------------------------------------------------------------------------------------------------------
#?    Dependancies + Globals
#--------------------------------------------------------------------------------------------------------------------------------------------

import json                             # For context demonstration. This isn't important for AI.
import ollama
MODEL = "llama3.2:3B"                   # The model we'll be using.
PROMPT = "write a very short story"     # The prompt we'll be giving the AI.

from simplify import clear              # Not important either. This just clears the terminal.

#--------------------------------------------------------------------------------------------------------------------------------------------
#?    Loading a model
#--------------------------------------------------------------------------------------------------------------------------------------------

#! The AI will take a bit to initialize before it actually starts generating something. It only has to do this
#! once, but it'll turn off after about five minutes of no activity and have to be initialized again.

#* This is for demonstating how long model loading takes.
print("Loading model...")
output = ollama.generate(MODEL, 'Output just the word "done"')
input("Done.")
clear()

#--------------------------------------------------------------------------------------------------------------------------------------------
#?    Just the text. You won't see anything happen until all text has been generated.
#--------------------------------------------------------------------------------------------------------------------------------------------

# A token is the way the language model stores and computes text. Each token is a set of numbers, as demonstrated later.

input("Press any key to start generating a story (just the text).")
clear()

print("--------------------------------------------------------------------------------------------------------")

output = ollama.generate(MODEL, PROMPT) # This takes over the main thread, stopping the program until it's done.
print(output.response)

input("--------------------------------------------------------------------------------------------------------")
clear()

#--------------------------------------------------------------------------------------------------------------------------------------------
#?    Streamed text (to process it word by word as it generates)
#--------------------------------------------------------------------------------------------------------------------------------------------

# A data stream is a type of data in Python where information is given piece by piece as it comes in.
# This is used for things like microphone input or something being broadcasted from the internet.
# These "pieces" are called chunks.

input("Press any key to start generating a story (as a stream).")
clear()

# "stream = True" makes the output a datastream instead of a string. 
# This means Ollama is going to give you tokens as they generate instead of a piece of text all at once.

output = ollama.generate(MODEL, PROMPT, stream = True)

# You'll notice that even though the output is labeled as "stream", code can still execute.
# This is the case until you set it up to start reading the stream.

print("This can still happen even though generation has started.")

print("--------------------------------------------------------------------------------------------------------")

context = []                                         #* Declare the context variable
full_text = ''                                       #* Start with an empty string

for chunk in output:                           #  This takes over the main thread, stopping any other execution.
    text_from_data = chunk.response            #  This is where the text is stored, .response
    full_text += text_from_data                      #* Add to the empty string
    print(chunk.response, end='', flush=True)  #* Print the new text to the same line, not a new one
    try:
        context = chunk.context # Only the last chunk has context. This is how you would store it.
    except:
        ""

print("\n--------------------------------------------------------------------------------------------------------")


input("This executes when the stream doesn't have any data to give the loop. Once you start the for loop, nothing else can happen until generation is done..")
clear()

#---------------------------------------------------
#?    What you captured with "full_text"
#---------------------------------------------------

input('Press any key to see what the empty "full_text" string has become.')
clear()

print("--------------------------------------------------------------------------------------------------------")
print(full_text)
input("--------------------------------------------------------------------------------------------------------")
clear()

#--------------------------------------------------------------------------------------------------------------------------------------------
#?    What context looks like
#--------------------------------------------------------------------------------------------------------------------------------------------

input("Press any key to save the context from earlier saved to context.json ")
with open('Week 1 - Demonstration/context.json', 'w') as f:
    json.dump(context, f)

#--------------------------------------------------------------------------------------------------------------------------------------------
#?   End of
#--------------------------------------------------------------------------------------------------------------------------------------------
