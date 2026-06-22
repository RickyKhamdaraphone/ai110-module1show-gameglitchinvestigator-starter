# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  On the first glance, the game seems to be perfectly functional. However, as mentioned, the hints were backwards. The new game button also did not seem to work, forcing me to refresh the page in order to play again. The score system is also set to -5 for some reason that I am not currently sure of. And lastly, the attempts seem to be inaccurate as the game ends up ending before I use them all up.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of 67 | Go lower    | Go higher       | none |
| 7 guesses entered | 7 attempts used | 8 attempts used | none |
| New game started | Able to play a new game | Unable to play a new game, history and score remain the same as before. | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

Copilot

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

Copilot suggested that the cause of the New Game button not working was that the status is never reset, causing the new game to not start. I first accepted the proposed fix and opened up the game to see if the button would work correctly, and it did without much issue. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

When asking about the High/Low logic error, Copilot suggested that it was because the texts are swapped and recommended swapping the two hint strings. However, this is not true since I should instead modify each string rather than swap them. Copilot's suggestion however aligned with my thinking, so it seemed to be a phrasing issue than a mistake by the AI.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I opened the game and manually ran several test cases. Different inputs for each test case, or a different approach (e.g. new game in the middle of a game rather than a finished one).

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I started up a game and entered a non-integer value to see if the program would break. However, I got an output that states it is not an integer but still logs in the guess as an attempt. This seems like acceptable logic so I left it as is.

- Did AI help you design or understand any tests? How?

Yes, I asked Copilot to create and run pytest rests for me. Since I was using a virtual environment, the command that is ran for these tests is slightly different and Copilot helped with that. These tests were fairly simple however and was something I could do manually.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would say that Streamlit reruns is very similar to refreshing a page, but only refreshes the program. It goes back to the first line as if entering a fresh state. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  I am a fan of accepting AI suggestions and then running the program to see if it works. If it doesn't I can always reset the changes. If it does, then I move forward.

- What is one thing you would do differently next time you work with AI on a coding task?

I think my prompting was a bit too broad and didn't go step by step. This lead to some misleading responses and caused me to go back. I would definitely focus more on figuring out what is a good prompt that returns concise and exact responses.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This was my first time using an AI Agent rather than referencing a chat model like ChatGPT or Gemini. I learned that this is a very powerful tool that is able to look directly into my code and modify it as needed. Using AI for coding is more than just asking an LLM about what's wrong and how to fix it.
