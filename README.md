# AgeFilter
## The Problem
Modern age filter systems, such as the ones used by roblox, completely prohibitted users of different age groups of talking to each other. I did not like this, so I created my own chat moderation system.

## My Solution
What if all the age groups could chat together, but they all had different filters. Like the kids that are insie the 5-8 group have really strong filters, but the adults in the MA group had the weakest filters. This means that they can all talk to each other, but with different filters.

## Implementation
So to create the different filters, I made 4 data sets for training the model(one for each group).
To create a filter, I trained a machine learning model using pytorch on the corresponding data set to age. 
Then I saved it along with the configurations and stuff like that. 

## Testing
To test this out, I actually had to create my own chat application. I used flask for the backend for speed, and I used ajax on the frontend with javascript, html, and css for sending and recieving messages. The concept worked, but the models did not have a high accuracy.

## How you can help
The reason why the models did not have a high accuracy was because of the lack of training data. If everyone who sees this can gather training data to help train the model instead of me using ai generated slop data, then the model will be much more accuracte. 

# #FREEDOM OF SPEECH WHILE KEEPING PEOPLE SAFE IS POSSILBE
