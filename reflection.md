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



- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
