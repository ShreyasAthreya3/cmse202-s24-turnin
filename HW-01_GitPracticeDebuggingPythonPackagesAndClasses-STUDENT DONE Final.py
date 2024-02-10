#!/usr/bin/env python
# coding: utf-8

# # Homework Assignment 1
# ## Git practice, debugging practice, and new Python packages, and Python classes

# ### <p style="text-align: right;"> &#9989; Shreyas Athreya</p>
# ### <p style="text-align: right;"> &#9989; ShreyasAthreya3</p>

# ### Goals for this homework assignment
# By the end of this assignment, you should be able to:
# * Use Git to create a repository, track changes to the files within the repository, and push those changes to a remote repository.
# * Debug some basic Python code that involves Pandas.
# * Read documentation and example code to use a new Python package
# * Modify and use a simple Python class
# 
# Work through the following assignment, making sure to follow all of the directions and answer all of the questions.
# 
# There are **62 points** possible on this assignment. Point values for each part are included in the section headers and question prompts.
# 
# **This assignment is due at 11:59 pm on Friday, February 9.** It should be uploaded into the "Homework Assignments" submission folder for Homework #1 on D2L.  Submission instructions can be found at the end of the notebook. **You must also fill out a survey regarding this assignment.** The link to this survey can also be found at the end of the notebook.

# 
# <a id="toc"></a>
# 
# ## Table of contents
# 
# 0. [Part 0: Office Hours and Help Room](#ofhrs) (6 points) 
# 
# 1. [Part 1: Git and CLI](#gits) (14 points)
# 
# 2. [Part 2: Debugging](#debugging) (6 points)
# 
# 3. [Part 3: Downloading and analyzing unfamiliar data](#unfamiliar) (7 points)
# 
# 4. [Part 4: Using documentation to use a new Python package](#folium) (10 points)
# 
# 5. [Part 5: Practice with using Python classes](#classes) (13 points)
# 
# 6. [Part 6: Finishing](#conclusion) (6 points)

# In[1]:


# Calculate total points possible and print it
print("Total number of points possible on this assignment is %i." %(6+14+6+7+10+13+6))


# ---
# <a id="ofhrs"></a>
# [Back to ToC](#toc)
# 
# 
# ## Part 0: Visiting Office Hours or Help Room (6 points)
# 

# ### Going to Office Hours or Help Room
# 
# #### Why are we doing this?
# We want to make sure that everyone knows how to access the resources available to you. One of the best resources you have at your disposal is office hours and help room.
# 
# #### What will you do?
# (At minimum) Go to one office hour or help room session ​(it doesn’t matter which one you go to). Come with one question that you would like to talk about. It can be big or small. It can be about the homework, but it doesn't have to be. It can be anything about the course or about computational modeling and data analysis in general.
# 
# Once you get to office hours or help room, ask your question. All of the instructors for CMSE 202 (Professors, TAs, and LAs) will be adding to a running list of folks that we see during office hours; as long as your name appears on the list, you’ll get credit for this part of Homework 1.
# 
# **NOTE:** The day when the homework is due (**Friday, February 9 at 11:59pm**) will be the busiest time for folks to go to office hours or help room. You are **STRONGLY** encouraged to go to office hours or help room before Friday to get credit for this part of this assignment. (You should still feel free to go to office hours or helproom on Friday for help, though!)
# 
# You can find the office hours calendar on the [course website](https://cmse.msu.edu/cmse202).
# 
# **FINAL NOTE:** If you are unable to attend office hours or help room, please contact the instructor to make alternative arrangements and explain why you are unable to attend.

# **&#9989; **Question 0.1 (6 points)****
# 
# Type below the question you asked and **who you asked it to** (make sure you know who you're talking to!). Make sure you double-check that the instructor made note of this.
# 
# If you did not attend office hours or help room, please explain why.

# <font size=6 color="#009600">&#9998;</font> *I'm sorry due to family circumstances I've had to go up north in a place where the wifi isn't usable, due to that I've been unable to use data, or access the internet due to unforseen circumstances.*
# 
# <font size=6 color="#009600">&#9998;</font> 

# ---
# <a id="gits"></a>
# [Back to ToC](#toc)
# 
# ## Part 1: CLI and Git (14 points)
# 
# ### Setting up a git repository to track your progress on your assignments 
# 
# `git` is a very important professional tool and we want you to get plenty of practice using it. The following set of questions prompt you to create a (private) Git repo for storing, updating, and turning in your homework assignments. You will **share this repo with your course lead instructor and TA** so that they can pull your completed assignments for grading.

# &#9989; **Question 1.1 (2 points)**:
# 1. On [GitHub](https://github.com) make sure you are logged into your account and then, if you haven't already, create a new <font color="red">**_private_**</font> GitHub repository called `cmse202-s24-turnin`. <font color="red">**Important note**</font>: you may have already created repository in a PCA, if you have, please use that one. If you have not, please create a new one.
# 2. Once you've initialized the repository on GitHub, **clone a copy of it onto JupyterHub or your computer**.

# ``` bash
# git clone https://github.com/ShreyasAthreya3/cmse202-s24-turnin.git
# ```

# &#9989; **Question 1.2 (1 point)**: Using the command line interface, move inside the repository folder
# 
# What command did you use to enter into the folder?

# ```bash
# cd repository
# ```

# &#9989; **Question 1.3 (1 point)**: Once inside the `cmse202-s24-turnin` repository, create a new folder called `hw-01`.
# 
# What is the command to create the new folder ?

# ```bash
# # Put the command to create the folder/directory here
# ```

# &#9989; **Question 1.4 (1 point)**: Move this notebook into that **new directory** in your repository then check the **_status_** of the repository
# 
# <font color="red">**This is an important step**</font>: you'll want to make sure you **save and close** the notebook before you do this step and then re-open it once you've added it to your repository. If you don't do this, you could end up working on the wrong version of the notebook! Once you've moved the notebook correctly, re-open it and continue working on it.
# 

# ```bash
# # Put the command you used to check the status of your repository here.
# ```

# &#9989; **Question 1.5 (1 point)**: Copy and paste below the output of the status command.

# 
# ``` bash
# # Paste it here
# ```

# &#9989; **Question 1.6 (1 point)**: What is the name of the current branch of the repository that you are in? (*Hint*: There should only be one branch at this time. We'll learn more about branches in git later in the semester.)

# ```bash
# # Put your answer here
# ```

# &#9989; **Question 1.7 (3 points)**:
# If you haven't already, add your name and GitHub username to the top of the notebook, then add and commit **ONLY** the notebook.
# 
# 

# ``` bash
# # Put the command(s) to add and commit here 
# ```

# What is the commit message you used ?

# ``` bash
# # Copy your commit message here
# ```

# &#9989; **Question 1.8 (1 point):** Before moving on. Check that the notebook you are working on is the correct one. Run the following cell. **Are you in the new folder you just created?** If not close this notebook and open the one in the `hw-01` folder. You'll likely need to copy of over the work you did on the above questions if you were working on the wrong notebook.
# 

# In[ ]:


get_ipython().system('pwd')


# &#9989; **Question 1.9 (3 points):** Assuming that you notebook is in the right place and committed to your repository, **push your changes to GitHub.**
# 
# What command did you use to push your changes to GitHub?

# ``` bash
# # Put the command you used to push your changes to GitHub here
# ```

# ### Before moving on...
# 
# **Important**: Make sure you've added your Professor and your TA as collaborators to your new "turnin" respository with "Read" access so that they can see your assignment. **You should check the Slack channel _for your section of the course_ to get this information.**
# 
# **Double-check the following**: Make sure that the version of this notebook that you are working on is the same one that you just added to your repository! If you are working on a different copy of the notebook, **none of your changes will be tracked**.
# 
# If everything went as intended, **the file should now show up on your GitHub account** in the "`cmse202-s24-turnin`" repository inside the `hw-01` directory that you just created.  Periodically, **you'll be asked to commit your changes to the repository. By the end of the assignment you should have multiple commits that correspond to your completion of each section (as specified below)**. Of course, you can always commit your changes more often than that, if you wish.  It can be good to get into a habit of committing your changes any time you make a significant modification, or when you stop working on the project for a bit.
# 

# ---
# <a id="debugging"></a>
# [Back to ToC](#toc)
# 
# ## Part 2: Debugging Pandas code (6 points)
# 
# ### Reading Python and Pandas code and understanding errors and error messages 
# 
# In this section, you will practice reading and debugging code, specially examples that use Pandas (since we'll be regularly using Pandas in the course and we spent some time reviewing Pandas in class). Debugging can be one of the most frustrating and time consuming part of a computational project, hence, it's worth spending time parsing and debugging error messages. 
# 
# Review the following code. Make sure to read the comments to understand what the code is _supposed_ to do. Then run the code and see what it outputs and/or the error message. Finally, **make a copy of the code in the provided cell and then fix the code**. When you fix the code **add a comment to explain what was wrong with the original code**.
# 
# **IMPORTANT NOTE #1:** not every block of code will result in an error message, but it won't produce the desired output. Even if there is no error, there is something you need to fix within the code.
# 
# **IMPORTANT NOTE #2:** In some cases, the example may use a bit of Pandas code that you're not familiar with yet, in these cases, you'll need to consult the internet (or the Pandas documentation) to figure out what the code is doing. This is a very common practice in computational modeling and data analysis.

# ### Import Pandas before moving on!

# In[ ]:


# Import Pandas and matplotlib
import pandas as pd 


# &#9989; **Questions 2.1 (2 points)**: Review the following piece of Pandas code, read the comments to understand what it is supposed to do, then run the code to see what the output is. **DO NOT MODIFY THIS CODE CELL**. (so that you can remember what the bug was)

# In[ ]:


## DO NOT CHANGE THIS CELL ##

# Group df by column 'Subject' and take the mean 

df = pd.DataFrame({'Subject': ['Physics', 'Math',
                              'Math', 'Physics'],
                   'Scores': [88, 76, 92, 82]})

df.group('Subject').mean()


# If you need to write any code to explore the nature of the bug, please do so in the cell below.

# In[ ]:


# Put exploratory code here, if needed


# **DO THIS**: Now that you understand what the bug is, fix it in the cell below and **add a comment** explaining what the bug was and how you fixed it.

# In[ ]:


# Put your non-buggy code here


# &#9989; **Questions 2.2 (2 points)**: Review the following piece of Pandas code, read the comments to understand what it is supposed to do, then run the code to see what the output is. **DO NOT MODIFY THIS CODE CELL**. (so that you can remember what the bug was)
# 
# **Hint**: Since the error might be a little confusing on this one, you may want to look up some examples of how the `apply` function works in Pandas.

# In[ ]:


## DO NOT CHANGE THIS CELL ##

# Define a "square" function
# Apply the square function to every value in DataFrame 
# Store the result as a new DataFrame
def square(x):
  return x * x
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
new_df = df.apply(square())
new_df


# If you need to write any code to explore the nature of the bug, please do so in the cell below.

# In[ ]:


# Put exploratory code here, if needed


# **DO THIS**: Now that you understand what the bug is, fix it in the cell below and **add a comment** explaining what the bug was and how you fixed it.

# In[ ]:


# Put your non-buggy code here


# &#9989; **Questions 2.3 (2 points)**: Review the following piece of Pandas code, read the comments to understand what it is supposed to do, then run the code to see what the output is. **DO NOT MODIFY THIS CODE CELL**. (so that you can remember what the bug was)
# 
# **Note**: The resulting dataframe should look like this, but the values in the "A" column should be strings, not integers:
# 
# |    |   A |   B | 
# |---:|----:|----:|
# |  0 |   1 |   3 |
# |  1 |   2 |   4 |
# 

# In[ ]:


## DO NOT CHANGE THIS CELL ##

# Create a DataFrame with two columns of numbers
# Convert the first column to a string
# Check the data types of the DataFrame
# Display the DataFrame
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df['A'] = 'string'
print(df.dtypes)
df


# If you need to write any code to explore the nature of the bug, please do so in the cell below.

# In[ ]:


# Put exploratory code here, if needed


# **DO THIS**: Now that you understand what the bug is, fix it in the cell below and **add a comment** explaining what the bug was and how you fixed it.

# In[ ]:


# Put your non-buggy code here


# ---
# ## &#128721; STOP
# **Pause to add and commit your changes to your Git repository!**
# 
# Take a moment to save your notebook, commit the changes to your Git repository using the commit message **"Committing Part 2"**, no need to push the changes to GitHub, but you can if you want.
# 
# 

# ---
# <a id="unfamiliar"></a>
# [Back to ToC](#toc)
# 
# ## Part 3: Downloading and analyzing unfamiliar data (7 points)
# 
# For this part of the homework assignment, you're to download and analyze a dataset known as the Iris dataset. This is one of the most famous datasets for multivariate analysis and machine learning.
# More information about this dataset can be found on this Wikipedia page [https://en.wikipedia.org/wiki/Iris_flower_data_set]. You'll perform some simple, exploratory analysis and create basic visualizations.

# &#9989; **Question 3.1 (1 point)**: **Do this now:** Using the command line interface, save the following file in the same directory as your notebook so you can load it directly. 
# 
# https://raw.githubusercontent.com/yangy5/HWFiles/main/Iris.csv
# 
# **Then, in the cell below, put the command you used to download the file.**

# ```bash
# # Put the command you used for downloading the data files here!
# ```

# &#9989; **Question 3.2 (2 points)**: To get started, **read in the `Iris.csv` dataset and then display it using Pandas**. This dataset contains 150 samples of flowers, each with four features: sepal_length, sepal_width, petal_length, petal_width. 

# In[1]:


import pandas as pd

df = pd.read_csv("Iris.csv")
print(df)


# &#9989; **Question 3.3 (2 points)**: **Construct a new data frame named "df_versi" that consists only of samples from the species "versicolor". How many samples do you see in this new data frame?** You can most easily do this with a mask, but you can use whatever method that works.

# In[4]:


import pandas as pd

df = pd.read_csv("Iris.csv")
mask = df['species'] == 'versicolor'
df_versi = df[mask]
print(df_versi.head())
value = (len(df_versi))
print("number of samples is", value)


# &#9989; **Question 3.4 (2 points)**: **Construct a new data frame named "df_versi_sepal" that consists only of the columns "sepal_length" and "sepal_width" in your data frame "df_versi" and display it again**. We will not work with the other two features "petal_length" and "petal_width". 

# In[5]:


df_versi_sepal = df_versi[["sepal_length", "sepal_width"]]
print(df_versi_sepal)


# ---
# ## &#128721; STOP
# **Pause to commit your changes to your Git repository!**
# 
# Take a moment to save your notebook, commit the changes to your Git repository using the commit message "**Committing Part 3**", no need to push the changes to GitHub yet, but you can if you want.

# ---
# <a id="folium"></a>
# [Back to ToC](#toc)
# 
# ## Part 4: Working with a less familiar Python package (10 points)
# 
# In this part of the assignment you will need to review a bit of documentation from either a new Python package or a package that you've explored a bit previously this semester.

# We will use a new Python package `seaborn`. Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. As you work on this part of the assignment, you should take advantage of the [Seaborn documentation]((https://seaborn.pydata.org/index.html)) which contains some really useful examples!

# &#9989; **Question 4.1 (1 point)**: If you don't already have the `seaborn` package installed, what command could you use to install it? (you should run this command on the command line, if you need to).
# 
# If you do already have it installed, what command did you use to install it?

# ```bash
# pip install seaborn
# ```

# &#9989; **Question 4.2 (4 point)**: Seaborn has a method to plot pairwise relations between features. For this problem, use the full Iris dataset with 150 samples. **Make a pairwise plot where different species are marked with different colors and explain what the figures mean.**

# In[6]:


import seaborn as sns
import pandas as pd


df = pd.read_csv("Iris.csv")
sns.pairplot(df, hue="species")
# The scatterplots show the relationship between the variables in most cases it's a positive correlation
# The species plots with overlapping data in the shape of triangles show the overlap giving us more information on the range and distribution of values


# &#9989; **Question 4.3 (2 points)**: For this problem, use the full Iris dataset with 150 samples. **For each species, compute the mean features of all samples and display them as a data frame, with each row representing a species and each column representing the mean value of a feature.** As we have 4 features for each species, you should expect to get a data frame with (# of species) rows and 4 columns. Hint: see **Question 2.1**.

# In[8]:


### Put your code here
import pandas as pd

df = pd.read_csv("Iris.csv")
mean_features = df.groupby('species').mean()
print(mean_features)


# &#9989; **Question 4.4 (3 points)**: For this problem, use the full Iris dataset with 150 samples. **For each feature, draw a box plot to show distribution of samples with respect to species.** Always use "species" as the horizontal axis. Use one feature as the vertical axis at a time. How are the median values reflected in these box plots? 

# In[10]:


### Put your code here
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Iris.csv")
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
for feature in features:
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='species', y=feature)
    plt.title(f'Box Plot of {feature} by Species')
    plt.xlabel('Species')
    plt.ylabel(feature)
    plt.show()
# the median value is reflected by the horizontal line in each of the species box plots


# ---
# ## &#128721; STOP
# **Pause to commit your changes to your Git repository!**
# 
# Take a moment to save your notebook, commit the changes to your Git repository using the commit message "**Committing Part 4**", no need to push the changes to GitHub yet, but you can if you want.

# ---
# <a id="classes"></a>
# [Back to ToC](#toc)
# 
# ## Part 5: Practice with using Python classes (13 points)
# 
# For this part of the assignment, you're going to work on fleshing out a partially constructed Python class and then experiment with using it to see if it works as intended.
# 
# ### The background
# 
# Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables by fitting a linear equation to observed data. It aims to find the best-fit line that minimizes the sum of squared differences between the predicted and actual values. In this part, we will write a Python class to implement linear regression. The following code is generated by the generative AI tool [Claude](https://claude.ai/). We will use it as a starting point. **Review the code and try running it. Make sure you understand what this code is doing.**

# In[ ]:


import numpy as np
import scipy.stats as st


class ModelData:

    def __init__(xdata, ydata):
        self.xdata = xdata
        self.ydata = ydata
        
    def summary_stats(self):
        return {
            "mean_x": np.mean(self.xdata), 
            "std_x": np.std(self.xdata),
            "mean_y": np.mean(self.ydata),
            "std_y": np.std(self.ydata)
        }

    def fit_linear_model(self):
        slope, intercept, r_value, p_value, std_err = st.linregress(self.xdata, self.ydata)
        return {
            "slope": slope,
            "intercept": intercept, 
            "r_value": r_value,
            "p_value": p_value,
            "std_err": std_err
        }


# ### Modifying the class to alter its behavior and add new functionality
# 
# In the code cell below, you're provided with a second copy of this new Python class, `ModelData`. For the remainder of this section of the assignment, **you will be modifying this version of the class** to add new functionality and alter its behavior. You will then be provided with snippets of code designed to test your modifications and confirm that you've implemented them as intended.
# 
# **When you make edits to the class provided below, make sure to run the cell to save your changes before running the included tests!**
# 
# _<font color="red">Note</font>_: Feel free to experiment with using one of the generative AI tools out there to help you expand upon and modify the initial starting point for this new Python class. If you do this, **make sure to include a link to the tool you used in the markdown cell below along with the prompt you used to generate the code and the date you accessed the tool.** Additionally, it is important to make sure that you understand the code you're working with, so make sure to review the code that is generated and make sure you understand what it is doing!

# In[ ]:


import numpy as np
import scipy.stats as st

class ModelData:

    def __init__(self, xdata, ydata):
        self.xdata = xdata
        self.ydata = ydata
        
    def summary_stats(self):
        return {
            "mean_x": np.mean(self.xdata), 
            "std_x": np.std(self.xdata),
            "mean_y": np.mean(self.ydata),
            "std_y": np.std(self.ydata)
        }

    def fit_linear_model(self):
        slope, intercept, r_value, p_value, std_err = st.linregress(self.xdata, self.ydata)
        return {
            "slope": slope,
            "intercept": intercept, 
            "r_value": r_value,
            "p_value": p_value,
            "std_err": std_err
        }
#Used Chatgpt, pasted the original code and the question above- Modifying the class to alter its behavior and add new functionality
#In the code cell below, you're provided with a second copy of this new Python class, ModelData. For the remainder of this section of the assignment, you will be modifying this version of the class to add new functionality and alter its behavior. You will then be provided with snippets of code designed to test your modifications and confirm that you've implemented them as intended.

#When you make edits to the class provided below, make sure to run the cell to save your changes before running the included tests!


# &#9989; **Questions 5.1 (2 points)**: **Debug the `ModelData` class, then run the following code to see what the output is.** **DO NOT MODIFY THIS CODE CELL**. (so that you can remember what the bug was)

# In[14]:


## DO NOT CHANGE THIS CELL ##

# This is an example usage of the class "ModelData" If it doesn't work, you need to make changes to the class.
import matplotlib.pyplot as plt

x = np.random.randn(100) 
y = 2*x + 5 + np.random.normal(0, 0.5, 100)

data = ModelData(x, y)
stats = data.summary_stats()
model = data.fit_linear_model()

print(stats)
print(model)


# If you need to write any code to explore the nature of the bug, please do so in the cell below.

# In[15]:


import numpy as np
import scipy.stats as st  

import matplotlib.pyplot as plt

class ModelData:
    def __init__(self, xdata, ydata):
        self.xdata = xdata
        self.ydata = ydata
        
    def summary_stats(self):
        return {
            "mean_x": np.mean(self.xdata),
            "std_x": np.std(self.xdata),
            "mean_y": np.mean(self.ydata),
            "std_y": np.std(self.ydata)
        }

    def fit_linear_model(self):
        slope, intercept, r_value, p_value, std_err = st.linregress(self.xdata, self.ydata)
        return {
            "slope": slope,
            "intercept": intercept, 
            "r_value": r_value,
            "p_value": p_value,
            "std_err": std_err
        }

x = np.random.randn(100) 
y = 2*x + 5 + np.random.normal(0, 0.5, 100)

data = ModelData(x, y)
stats = data.summary_stats()
model = data.fit_linear_model()

print(stats)
print(model)


# **DO THIS**: Now that you understand what the bug is, fix it in the cell below and **add a comment** explaining what the bug was and how you fixed it.

# In[17]:


import numpy as np
import scipy.stats as st  

import matplotlib.pyplot as plt

class ModelData:
    def __init__(self, xdata, ydata):
        self.xdata = xdata
        self.ydata = ydata
        
    def summary_stats(self):
        return {
            "mean_x": np.mean(self.xdata),
            "std_x": np.std(self.xdata),
            "mean_y": np.mean(self.ydata),
            "std_y": np.std(self.ydata)
        }
#Function wasn't defined previously, now it was
#Imported right functions
    def fit_linear_model(self):
        slope, intercept, r_value, p_value, std_err = st.linregress(self.xdata, self.ydata)
        return {
            "slope": slope,
            "intercept": intercept, 
            "r_value": r_value,
            "p_value": p_value,
            "std_err": std_err
        }

x = np.random.randn(100) 
y = 2*x + 5 + np.random.normal(0, 0.5, 100)

data = ModelData(x, y)
stats = data.summary_stats()
model = data.fit_linear_model()

print(stats)
print(model)


# &#9989; **Question 5.2 (4 points)**: Now, **create a new class method named `plot_model`.** It takes two input arguments: `slope` and `intercept`. For the output, it generates two plots on the same figure: one is the line with the input slope and intercept, the other is a scatter plot of the dataset points {(xdata, ydata)}.

# In[18]:


import numpy as np
import scipy.stats as st  
import matplotlib.pyplot as plt

class ModelData:
    def __init__(self, xdata, ydata):
        self.xdata = xdata
        self.ydata = ydata
        
    def summary_stats(self):
        return {
            "mean_x": np.mean(self.xdata),
            "std_x": np.std(self.xdata),
            "mean_y": np.mean(self.ydata),
            "std_y": np.std(self.ydata)
        }

    def fit_linear_model(self):
        slope, intercept, r_value, p_value, std_err = st.linregress(self.xdata, self.ydata)
        return {
            "slope": slope,
            "intercept": intercept, 
            "r_value": r_value,
            "p_value": p_value,
            "std_err": std_err
        }
    
    def plot_model(self, slope, intercept):
        plt.figure(figsize=(10, 5))
        
        # Plotting the line with the input slope and intercept
        x_values = np.linspace(min(self.xdata), max(self.xdata), 100)
        y_values = slope * x_values + intercept
        plt.plot(x_values, y_values, color='red', label='Fitted Line')
        
        # Plotting the scatter plot of the dataset points
        plt.scatter(self.xdata, self.ydata, color='blue', label='Data Points')
        
        plt.xlabel('xdata')
        plt.ylabel('ydata')
        plt.title('Fitted Line and Data Points')
        plt.legend()
        plt.grid(True)
        plt.show()


x = np.random.randn(100) 
y = 2*x + 5 + np.random.normal(0, 0.5, 100)

data = ModelData(x, y)
stats = data.summary_stats()
model = data.fit_linear_model()

print(stats)
print(model)


data.plot_model(model['slope'], model['intercept'])


# &#9989; **Question 5.3 (3 points)**: Create a new class method called `predict` that predicts and returns the model prediction for a given input value $x$. You should be able to use the `fit_linear_model` method and the keys `slope` and `intercept` in the dictionary to help you with this.
# 
# Once you've defined the new method, you should be able to execute the cell below to see if the new method works as intended.

# In[ ]:


## DO NOT CHANGE THIS CELL ##

# This is an example usage of the "predict" method. If it doesn't work, you need to make changes to your method.

x_new = np.array([1.5, 3.2, -2.7]) 
y_pred = data.predict(x_new)

y_pred


# In[19]:


import numpy as np
import scipy.stats as st  
import matplotlib.pyplot as plt

class ModelData:
    def __init__(self, xdata, ydata):
        self.xdata = xdata
        self.ydata = ydata
        
    def summary_stats(self):
        return {
            "mean_x": np.mean(self.xdata),
            "std_x": np.std(self.xdata),
            "mean_y": np.mean(self.ydata),
            "std_y": np.std(self.ydata)
        }

    def fit_linear_model(self):
        slope, intercept, r_value, p_value, std_err = st.linregress(self.xdata, self.ydata)
        return {
            "slope": slope,
            "intercept": intercept, 
            "r_value": r_value,
            "p_value": p_value,
            "std_err": std_err
        }
    
    def plot_model(self, slope, intercept):
        plt.figure(figsize=(10, 5))
        
        x_values = np.linspace(min(self.xdata), max(self.xdata), 100)
        y_values = slope * x_values + intercept
        plt.plot(x_values, y_values, color='red', label='Fitted Line')
        
        plt.scatter(self.xdata, self.ydata, color='blue', label='Data Points')
        
        plt.xlabel('xdata')
        plt.ylabel('ydata')
        plt.title('Fitted Line and Data Points')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def predict(self, x_new):
        model = self.fit_linear_model()
        return model['slope'] * x_new + model['intercept']


x = np.random.randn(100) 
y = 2*x + 5 + np.random.normal(0, 0.5, 100)

data = ModelData(x, y)
stats = data.summary_stats()
model = data.fit_linear_model()

print(stats)
print(model)


data.plot_model(model['slope'], model['intercept'])


x_new = np.array([1.5, 3.2, -2.7]) 
y_pred = data.predict(x_new)
print("Predicted values:", y_pred)


# ### Testing your new `ModelData` class on real data
# 
# Now that you have an enhanced version of the initial `ModelData` class, let's see if it works as intended on some real data! Specifically, since you already spent some time getting familiar with the Iris data in Part 3 of this assignment, let's see if your new class produces results that makes sense based on your previous observations.
# 
# &#9989; **Question 5.4 (4 points)**: We will use the columns "sepal_length" and "sepal_width" in your data frame "df_versi_sepal" (see Question 3.4) as the xdata and ydata to fit a linear model. The model will tell us how sepal_width grows as a linear function of sepal_length. This is the idea of linear regression.
# 
# 
# **You will need to do this in the following steps:** First, extract the columns "sepal_length" and "sepal_width" in your data frame "df_versi_sepal" and save these values in two numpy arrays. Next, create a new instance of your `ModelData` class, then use these numpy arrays as data points to fit a linear model. Finally, use your `plot_model` method (see **Question 5.2**) to plot the line as well as all the data points. 
# 

# In[21]:


sepal_length = df_versi_sepal['sepal_length'].values
sepal_width = df_versi_sepal['sepal_width'].values


data = ModelData(sepal_length, sepal_width)


model = data.fit_linear_model()
data.plot_model(model['slope'], model['intercept'])


# ---
# ## &#128721; STOP
# **Pause to commit your changes to your Git repository!**
# 
# Take a moment to save your notebook, commit the changes to your Git repository using the commit message "**Committing Part 5**", no need to push the changes to GitHub yet, but you can if you want.

# ---
# <a id="conclusion"></a>
# [Back to ToC](#toc)
# 
# ## Part 6: Finishing (6 points)
# 
# 
# **Question 6.1 (2 points):** Have you put **your name** and **GitHub username** at the top of your notebook?
# 
# **Question 6.2 (2 points):** Have you added the **TA** and **Instructor** to your GitHub repository? (You should have done this in Part 1, and they should have shared this information via Slack)
# 
# **Question 6.3 (2 points):** Finally, push your repository to GitHub so that all of the commits that you have been making along the way show up on GitHub.
# 
# ```bash
# git init
# git add 
# ```
# 
# **NOTE:** The grader will be able to see your commit messages and whether you pushed the repo at this stage, if everything have gone as planned. Double-check that things look correct on GitHub before you submit this notebook to D2L.
# 

# ---
# ## Assignment wrap-up
# 
# Please fill out the form that appears when you run the code below.  **You must completely fill this out in order to receive credit for the assignment!**

# In[22]:


from IPython.display import HTML
HTML(
"""
<iframe 
	src="https://forms.office.com/r/DGuPxy8hjy" 
	width="800px" 
	height="600px" 
	frameborder="0" 
	marginheight="0" 
	marginwidth="0">
	Loading...
</iframe>
"""
)


# ### Congratulations, you're done!
# 
# Submit this assignment by uploading it to the course Desire2Learn web page.  Go to the **"Homework Assignments"** folder, find the dropbox link for Homework #1, and upload it there.

# &#169; Copyright 2023,  Department of Computational Mathematics, Science and Engineering at Michigan State University
