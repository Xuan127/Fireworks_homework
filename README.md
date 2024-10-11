[Deployed Web App](https://fireworkshomework-bmyqvkvmdbcfa4fcuzywyj.streamlit.app/)

Justification:
1. This is a MVP that demonstrates the ability to extract information from an image
2. Used LLAMA 90B as it has the highest ranking on MMMU leaderboard and accuracy should be important
  for this task, hence higher cost per million token is justified. Further more, information extraction
  is not done frequently, likely once per potential customer, so cost is not a major concern.
3. Output is in JSON format, which is easy to parse and use in other applications.
4. Essential information such as name and DOB are extracted, and additional information can be added.
5. Misidentification is an issue, did not fine-tune the model as there is not enough data to do so.
6. Played around with some of the parameters (temperature, n), but did not find any significant improvements.
7. Used Streamlit to create a simple web app to upload an image and display the extracted information.