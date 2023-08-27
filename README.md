**Title: Defense Meteorological Satellite Program DMSP - Particle Precipitate Flux-Prediction Mesoscale**

Kaggle Notebook:- https://www.kaggle.com/code/shirshmall/particle-precipitate-flux-prediction/notebook

Kaggle Outputs(Saved Model, Callbacks Files and Sampled Data): https://www.kaggle.com/code/shirshmall/particle-precipitate-flux-prediction/data

Research Paper Manuscript for Reference - https://www.researchgate.net/publication/350946002_Toward_a_Next_Generation_Particle_Precipitation_Model_Mesoscale_Prediction_Through_Machine_Learning_a_Case_Study_and_Framework_for_Progress

📊Dataset:https://zenodo.org/record/4281122/files/AI_Ready_DMSP_Data.csv?download=1
Sampled Data (ReadyToTrainModel): https://www.kaggle.com/datasets/shirshmall/dmspparticleprecipitatefluxprediction


**Description:**
In this project, we aim to enhance the modeling capabilities of electron particle precipitation from the magnetosphere to the ionosphere by leveraging a newly curated database and harnessing the potential of deep learning tools. Our efforts are directed towards improving the accuracy of electron particle precipitation predictions using innovative techniques.

One of the core components of our project involves the creation of an advanced database of particle precipitation data. We have meticulously compiled, curated, and analyzed a comprehensive dataset that spans 51 satellite years of observations from the Defense Meteorological Satellite Program (DMSP). This dataset is temporally aligned with critical solar wind and geomagnetic activity data. This alignment ensures a robust representation of temporal correlations, allowing for more accurate predictions.

The cornerstone of our predictive model is the novel neural network named "PrecipNet." This model leverages the strengths of machine learning approaches to effectively utilize diverse information from solar wind and geomagnetic activity data, including their historical patterns. PrecipNet demonstrates a substantial improvement over the current state-of-the-art model, OVATION Prime. It achieves a remarkable >50% reduction in errors, enhancing our ability to predict oval variations, track intensity, assess auroral flux dynamics, and provide real-time nowcasting.

Moreover, our model captures dynamic changes in auroral flux with greater fidelity, while also showcasing its potential to reconstruct mesoscale phenomena. We have introduced a pioneering framework for evaluating space weather models, aligning with guidance from the solar-terrestrial research community. This framework enhances the credibility of our predictions and bolsters our model's performance assessment.

**Model Preparation:**
1. Our dataset consists of an impressive 1,945,887 rows and 154 columns, providing a substantial foundation for training and validation.
2. To streamline our dataset, we have excluded unnecessary time-related features denoted in minutes and seconds.
3. We adopted a systematic approach to data sampling, ensuring a consistent step of 7 throughout the dataset.
4. Thorough inspection revealed no presence of null values in our dataset.
5. Our target variable, the energy flux, exhibited significant skewness. We applied thresholding and outlier removal techniques to enhance its suitability for modeling.
6. Employing the Standard Scaler, we normalized the data for improved training performance.
7. To streamline our DMSP data, we removed the steradian feature prior to model training.
8. To better align with regression tasks, we performed a log transformation on the target variable.
9. Our neural network architecture for regression tasks involved a meticulous selection of hyperparameters. We utilized the Keras Tuner to identify optimal settings.
10. We embarked on training our best Deep Neural Network (DNN) model, employing an extensive 125 epochs. This intensive training regimen aimed to refine our model's accuracy and performance.
   - During training, we observed promising results, with epoch 29 achieving a loss of 0.4764, root mean squared error of 0.6902, mean squared logarithmic error of 0.0055, and an impressive R2 score of 0.6680.
   - The validation phase further substantiated our model's capabilities, showcasing a validation loss of 0.4726, root mean squared error of 0.6875, mean squared logarithmic error of 0.0053, and a validation R2 score of 0.6727.
11. Additionally, we explored the effectiveness of the Long Short-Term Memory (LSTM) model. This variant exhibited potential, achieving compelling results during training.
   - By the 18th epoch, the LSTM model demonstrated a loss of 0.3370, root mean squared error of 0.5805, mean squared logarithmic error of 0.0049, and an impressive R2 score of 0.7648.
   - During validation, the LSTM model maintained its promise with a validation loss of 0.4958, root mean squared error of 0.7041, mean squared logarithmic error of 0.0048, and a validation R2 score of 0.6559.
12. Our models, trained to perfection, were meticulously saved, and we preserved essential data samples and callback files to ensure reproducibility and further analysis.
