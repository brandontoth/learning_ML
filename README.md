# learning_ML   
   
### Setting up ssh keys  
You'll need to create a ssh key [instructions](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)    
Then add the ssh key to your github account [instructions](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)    
Then clone the repository
```bash
eval $(ssh-agent)
ssh-add ~/.ssh/KEY_NAME
git clone git@github.com:brandontoth/learning_ML.git
```   
   
     
     