# start-jarjargone
Web tool for medical definition and reliability scoring - Find out in real-time, all in one window.
Tired of medical jargon all over the place? Well, jargon is now jargone.

## Description
### Problem space: 
Helping patients or the layperson to quickly access the definition of medical terminology without leaving the page, just with a simple selection of the word, and handling misinformation by providing reliability scores.

### Impact: 
By having the tool as a browser extension, we can eliminate the steps of uploading the document onto a separate app - this also means that the patient does not need to leave their screen when reading quickly across sources. With further design this could improve accessibility,  ease to use, and user-friendliness to all groups of people (i.e. our design is much easier to explain to less tech-savvy people). The SumMed.org platform also does not process URLs which are not open-access (e.g. institutional log in methods, account based html document). Our tool also aims to handle misinformation and improve the decision making processes for patients by providing suggested reading material from trusted sources.

### Features
The Python back-end processes JSON data sent from chrome extension and returns the definition of the highlighted phrase, or the reliability of longer blocks of highlighted text using a neural network model.

### Demo:
<img src="demo/demo1b.png" alt="drawing" width="650"/>
<br/>
Definition
<br/>
<img src="demo/demo2.png" alt="drawing" width="650"/>
<br/>
Article suggestion (to be improved)

---
**Status: under development** 

To test out our project, please follow the below instructions:
### FRONTEND 
1. Go to chrome://extensions/
2. Click 'Load unpacked'
3. Navigate to project folder and select 'extension' directory

### BACKEND 
1. Follow instructions at https://flask.palletsprojects.com/en/1.1.x/installation/ for setting up virtual environment for Windows or Mac
2. Install requirements
```
$ pip install -r requirements.txt
```
3. Run flask app locally
```
$ export FLASK_APP=py-script/main.py
$ flask run
```

Note: 2 more important requirements are needed to run this extension
 * Neural network model file (d2v.model) which is too large to be pushed to Github. Please contact the developers directly. The new directory containing the model should be /py-script/model/d2v.model

 * Merriam webster API key to replace keyword 'hidden' in content.js on line 90
