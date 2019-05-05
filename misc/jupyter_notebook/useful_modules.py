
# coding: utf-8

# ## Useful modules in jupyter notebook
# - This notebook includes some basic tools in notebook

# ### module path, file path
# - add your module path (different from where the notebook is)
# - change your base path

# In[1]:


import os
import sys
# add your module path
module_path = os.path.abspath(os.path.join('..')) # '.'
if module_path not in sys.path:
    sys.path.append(module_path)
# change your base path
os.chdir('./') # '../'
print(os.getcwd())


# ### auto-reload
# - when you change anything in python files, the notebook will reload automatically.

# In[2]:


get_ipython().magic('load_ext autoreload')
get_ipython().magic('autoreload 2')


# ### Display
# - fit your notebook as wide as the browser

# In[3]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# ### Others

# In[4]:


import numpy as np
import matplotlib.pyplot as plt


# ## Debug with python file

# In[6]:


# import function and run
from utils import print_words
words = {'ucsd': 'ece', 'ntu': 'ee'}
print_words(words)


# In[7]:


# import function and visualize
from utils import get_rand_img
img = get_rand_img(20, 30)
plt.imshow(img)
plt.show()

