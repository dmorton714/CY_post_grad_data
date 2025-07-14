# Social Posts

The goal of this project is to introduce you to working with a mix of technologies. It includes a small Go script that you’ll need to build and run, so part of the exercise is learning how to install and use Go.

In real-world data pipelines, it’s common to use different languages within the same stack because some are better suited, or faster, for specific tasks. In this example, we’re using Go to convert a CSV file to JSON. While this may seem unnecessary for a small dataset, the performance benefits become significant when working with large volumes of data, so this could very well be something you run into. 


Run the project in order: 
- import_data.py
  - imports the data 
- database_setup.py
  - Makes the SQLite database 
- Build & run main.go
  - This will make the .json file you need.
- data_agg.py
  - Write the code to answer the questions.
  - Answers in the Answers folder.  
- main.py 
  - **Bonus:** 
  - Fix this file so that it runs on your computer! 
  - No answers are provided for this step. 