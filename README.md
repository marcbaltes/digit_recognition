# Digit Recognition
Uses an SVM model to train the MNIST data set and predict a number that was drawn by the user. The model has already been trained, tuned,
and saved in /data as rbf_model.joblib.pkl so no training is needed. All that is needed is an input from the user via the canvas

# Installation
Clone the repo: ```git clone https://github.com/marcbaltes/digit_recognition.git```

Go to the directory: ```cd digit_recognition```

Install dependencies: ```python -m pip install -r requirements.txt```

Once everything is installed run the program using ```python digit.py```. This will pull up a blank canvas to draw on.

# Inputting and Receiving data
Once the blank canvas is opened these are the keyboard commands to use it:
- 's': tells the canvas you are about to draw a number. Once pressed, hold down the left mouse button to draw and write the 
number in the canvas. Make sure to fill the canvas as much as possible with the number for the most accurate prediciton.
- 'c': clears the canvas
- 'p': takes the image on the canvas and uses the classifer to predict the number you have drawn. The predicted number will
be shown in the terminal
- 'q': closes the canvas and quits the program

# Credits and Notes
The .csv files of the MNIST dataset are not included in the repo so running model.py will not work. They were
not included because their file size was too large. However, if you wish to train the model yourself you can download
the dataset from here: [https://www.kaggle.com/oddrationale/mnist-in-csv](https://www.google.com). Place them in the /data directory and now model.py
will run and train the classifer.

The file for converting an image to a MNIST image and array was taken from [https://repl.it/@donovanchan/demo](https://repl.it/@donovanchan/demo)
so big thanks to him for allowing that code to be open source.

The file tuning.txt shows the small tuning experiments that were done on the model to achieve the highest accuracy on the test dataset. 
From these experiments, a gaussian kernel was used along with a C parameter of 10.
