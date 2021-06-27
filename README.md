# Diagnotica X Application for detecting COVID-19 in chest X-ray images
# Author: Jesus Ramseths Echeverría

- This project is designed for the Sigmahacks 3 hackathon.
- You need to have Python 3.7 or higher and PyQt5.

## Stage 1:
<p>First, a Jupyter Notebook is created with the algorithm to train the pre-trained model with ImageNet DenseNet-201. You can view it in the model/train_model folder.
It was trained with images from an external public access repository.</p>

## Stage 2:
<p>The interface is created in Qt Creator to achieve a more comfortable interaction for the user, in addition to maintaining the KISS principle. </p>

## Stage 3:
<p>The model is saved in the model folder and is used in the app.py script, in which the whole PyQt5 structure is implemented.</p>

## Stage 4:
<p>Finally, it is tested with two internet images, one of the chest with COVID-19 and the other of the normal chest, both of which are X-ray images, in addition to being images never seen before by our model, which successfully predicted both images.</p>

## About DenseNet-201
<p>It is a powerful 201-layer convolutional neural network that obtains a more minimal error compared to the human eye. This network was trained with ImageNet, so only in this project we did transfer learning for our two classes [Normal, Covid19].</p>



