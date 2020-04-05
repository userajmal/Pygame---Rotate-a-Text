#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pygame


# In[3]:


pygame.init()


# In[6]:


black=(0,0,0)
red=(255,255,255)
yellow=(0,0,255)
rose=(0,255,0)
blue=(255,0,0)
pi=3.14


# In[7]:


size=(400,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Rotate text")


# In[8]:


done=False
clock=pygame.time.Clock()
text_rotate_degree=0


# In[9]:


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


# In[ ]:


screen.fill(red)


# In[ ]:


pygame.draw.line(screen,black,[100,50],[200,50])
pygame.draw.line(screen,black,[100,50],[100,150])


# In[ ]:


font=pygame.font.SysFont('Calibri',25,True,False)


# In[ ]:


text=font.render("Sideways test",True,black)
text=pygame.transform.rotate(text,90)
screen.blit(text,[0,0])


# In[ ]:


text = font.render("Upside down text", True, black)
text = pygame.transform.rotate(text, 180)
screen.blit(text, [30, 0])


# In[ ]:


text = font.render("Flipped text", True, black)
text = pygame.transform.flip(text, False, True)
screen.blit(text, [30, 20])


# In[ ]:


text = font.render("Rotating text", True, black)
text = pygame.transform.rotate(text, text_rotate_degree)
text_rotate_degree += 1
screen.blit(text, [100, 50])


# In[38]:


pygame.display.flip()


# In[ ]:


clock.tick(60)


# In[12]:


pygame.quit()


# In[ ]:





# In[ ]:





# In[ ]:




