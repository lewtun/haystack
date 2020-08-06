from transformers import pipeline

nlp = pipeline("question-answering",model="deepset/roberta-base-squad2",
                                  tokenizer="deepset/roberta-base-squad2",
                                  device=-1)

nlp(question="Who is the father of Sansa Stark?", context="===''A Game of Thrones''===\
Sansa Stark begins the novel by being betrothed to Crown Prince Joffrey Baratheon, believing Joffrey to be a gallant prince. While Joffrey and Sansa are walking through the woods, Joffrey notices Arya sparring with the butcher's boy, Mycah. A fight breaks out and Joffrey is attacked by Nymeria (Arya's direwolf) after Joffrey threatens to hurt Arya. Sansa lies to King Robert about the circumstances of the fight in order to protect both Joffrey and her sister Arya.  Since Arya ran off with her wolf to save it, Sansa's wolf is killed instead, estranging the Stark daughters.\
During the Tourney of the Hand to honour her father Lord Eddard Stark, Sansa Stark is enchanted by the knights performing in the event.  At the request of his mother, Queen Cersei Lannister, Joffrey spends a portion of the tourney with Sansa, but near the end he commands his guard Sandor Clegane, better known as The Hound, to take her back to her quarters. Sandor explains how his older brother, Gregor, aka "Mountain that Rides" pushed his face into a brazier of hot coals, for playing with one of his wooden toys.\
After Eddard discovers the truth of Joffrey's paternity, he tells Sansa that they will be heading back to Winterfell. Sansa is devastated and wishes to stay in King's Landing, so she runs off to inform Queen Cersei of her father's plans, unwittingly providing Cersei with the information needed to arrest her father. After Robert dies, Sansa begs Joffrey to show mercy on her father and he agrees, if Ned will swear an oath of loyalty, but executes him anyway, in front of Sansa.  Sansa is now effectively a hostage in King's Landing and finally sees Joffrey's true nature, after he forces her to look at the tarred head of her now-deceased father.")