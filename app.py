import streamlit as st
import pickle
import numpy as np

# Load the saved model
with open('crop_prediction_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def predict_crop(protein, carbs, fat, minerals, fiber, calcium, phosphorus, iron, energy, thiamin, niacin):
    input_data = np.array([[protein, carbs, fat, minerals, fiber, calcium, phosphorus, iron, energy, thiamin, niacin]])
    prediction = model.predict(input_data)
    return prediction[0]

def main():
    st.title("Crop Prediction App")
    st.markdown("---")
    st.write("Welcome to the Crop Prediction App! Enter the nutrient intake values to predict the crop.")
    
    protein = st.number_input("Protein (g)", min_value=0.0, step=0.1)
    carbs = st.number_input("Carbs (g)", min_value=0.0, step=0.1)
    fat = st.number_input("Fat (g)", min_value=0.0, step=0.1)
    minerals = st.number_input("Minerals (g)", min_value=0.0, step=0.1)
    fiber = st.number_input("Fiber (g)", min_value=0.0, step=0.1)
    calcium = st.number_input("Calcium (mg)", min_value=0.0, step=0.1)
    phosphorus = st.number_input("Phosphorus (mg)", min_value=0.0, step=0.1)
    iron = st.number_input("Iron (g)", min_value=0.0, step=0.01)
    energy = st.number_input("Energy (kcal)", min_value=0.0, step=1.0)
    thiamin = st.number_input("Thiamin (mg)", min_value=0.0, step=0.01)
    niacin = st.number_input("Niacin (mg)", min_value=0.0, step=0.01)

    if st.button("Predict"):
        predicted_crop = predict_crop(protein, carbs, fat, minerals, fiber, calcium, phosphorus, iron, energy, thiamin, niacin)
        st.write("### Predicted Crop:")
        #st.image(f'crop_images/{predicted_crop}.jpg', width=300)
        st.write(f"The predicted crop is: {predicted_crop}")

if __name__ == '__main__':
    main()
