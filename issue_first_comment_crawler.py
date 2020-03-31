
# coding: utf-8

# In[1]:


#Import dependencies: HTTP library
import requests

#Import regular expressions library
import re


# In[2]:


# Call GitHub API to get json file of learn-github-action
# calls info on the issue and only the first comment of the issue
issues_json = requests.get('https://api.github.com/repos/dictybase-playground/learn-github-action/issues').json()


# In[3]:


# Ask user to input issue id
issue_id_input = int(input('Please enter issue id to receive first comment: '))     


# In[4]:


# Loop through json call for issue ids that match
# user input from user and print the body of the first comment
for data in issues_json:
    if issue_id_input == data['id']:
        comment_text = data['body']

print(f"This is the first comment of {issue_id_input}: {comment_text}")


# In[5]:


# Use re to find emails within first comment of issue
emails = re.findall('\S+@\S+', comment_text)

# Print list of emails
print(emails)

