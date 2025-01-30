#--------------------------------------------------------------------------------------------------------------
#?    Dependancies + Globals
#--------------------------------------------------------------------------------------------------------------

import json                             # For context demonstration. This isn't important for AI.
import ollama
MODEL = "llama3.2:3B"                   # The model we'll be using.

from simplify import clear, wait        # Not important either. This just clears the terminal.

#---------------------------------------------------------------------------------------------------------------
#?    A working chatbot!
#--------------------------------------------------------------------------------------------------------------

#* You don't need to load the model like this. It just feel a little more seamless.
print("Loading model...")
output = ollama.generate(MODEL, 'Output just the word "done"')
input("Done. (Press any button to continue)")
clear()

current_context = []

while True:
    user_input = input("\n> ")
    output = ollama.generate(MODEL, user_input, context=current_context, stream=True)
    full_text = ''                                 #* Start with an empty string
    for chunk in output:                           #  This takes over the main thread, stopping any other execution.
        text_from_data = chunk.response            #  This is where the text is stored, .response
        full_text += text_from_data                #* Add to the empty string
        print(chunk.response, end='', flush=True)  #* Print the new text to the same line, not a new one
        try:
            current_context = chunk.context # Only the last chunk has context. This is how you would store it.
        except:
            ""
    print()

#--------------------------------------------------------------------------------------------------------------
#     End of
#--------------------------------------------------------------------------------------------------------------
