# Sentiment-Analysis-App
This web based application takes a user input and shows the sentiment and polarity scores of the user's input.

### Almost done, waiting to be deployed to the cloud

The application interface on the home page, when opened, looks like this: 

![App-Home](https://github.com/ritvik-chebolu/Sentiment-Analysis-App/blob/main/app_home.png)

The text box takes user input sequences and classifies them using TextBlob library (an inbuilt python library) which is built on NLTK library to classify a set of predefined words in the dictionary as positive, negative and neutral along with a score associated with the extend of attitude the word expresses. 

The user inputs could be words, paragraphs or a couple of paragraphs. The algorithms can tokenize each sentence/paragraph into individual token and tries to analyze and reflect if the set of sequences try to make a positive, negative or neutral sense.


A simple example of how this app functions is shown below when the user inputs a sentence "I love Emma's cat. I wish I could take him home.":

![App-Example](https://github.com/ritvik-chebolu/Sentiment-Analysis-App/blob/main/app_example.png)


The application also has an about page that describes all the tools used while developing the program. The about page is shown below: 

![App_About](https://github.com/ritvik-chebolu/Sentiment-Analysis-App/blob/main/app_about.png)

Got some cool feature suggestions or improvements? 

Feel free to create a pull request on GitHub to report it to me :)
