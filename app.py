import streamlit as st
import pickle
import numpy as np

def predict_top_3_millets(protein, carbs, fat, minerals, fiber, calcium, phosphorus, iron, energy, thiamin, niacin):
    # Load the saved model
    with open('crop_prediction_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    input_data = np.array([[protein, carbs, fat, minerals, fiber, calcium, phosphorus, iron, energy, thiamin, niacin]])
    predicted_probabilities = model.predict_proba(input_data)

    # Get the indices of the top three predicted classes
    top_3_indices = predicted_probabilities.argsort()[0][-3:][::-1]

    top_3_millets = [model.classes_[index] for index in top_3_indices]
    top_3_probabilities = [predicted_probabilities[0][index] * 100 for index in top_3_indices]

    return top_3_millets, top_3_probabilities

def main():
    st.title("Crop Recommendation App")
    st.write(
        "This app recommends the top 3 millets based on nutrient intake values. "
        "Enter the nutrient intake values in the fields below and click the 'Recommend' button."
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        protein = st.number_input("Protein (g)", min_value=0.0, step=0.1)
    with col2:
        carbs = st.number_input("Carbs (g)", min_value=0.0, step=0.1)
    with col3:
        fat = st.number_input("Fat (g)", min_value=0.0, step=0.1)

    col4, col5, col6 = st.columns(3)
    with col4:
        minerals = st.number_input("Minerals (g)", min_value=0.0, step=0.1)
    with col5:
        fiber = st.number_input("Fiber (g)", min_value=0.0, step=0.1)
    with col6:
        calcium = st.number_input("Calcium (mg)", min_value=0.0, step=0.1)

    col7, col8, col9 = st.columns(3)
    with col7:
        phosphorus = st.number_input("Phosphorus (mg)", min_value=0.0, step=0.1)
    with col8:
        iron = st.number_input("Iron (g)", min_value=0.0, step=0.01)
    with col9:
        energy = st.number_input("Energy (kcal)", min_value=0.0, step=1.0)

    col10, col11 = st.columns([2, 1])
    with col10:
        thiamin = st.number_input("Thiamin (mg)", min_value=0.0, step=0.01)
    with col11:
        niacin = st.number_input("Niacin (mg)", min_value=0.0, step=0.01)

    if st.button("Recommend"):
        top_3_millets, top_3_probabilities = predict_top_3_millets(protein, carbs, fat, minerals, fiber, calcium, phosphorus, iron, energy, thiamin, niacin)

        st.write("Top 3 recommended millets:")
        for i in range(3):
            st.markdown(f"<div style='font-size: 24px; color:white;'>{top_3_millets[i]}: {top_3_probabilities[i]:.2f}% probability</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    #st.set_page_config(layout="wide")
    main()
