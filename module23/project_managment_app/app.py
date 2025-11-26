import streamlit as st
import requests
import pandas as pd

st.title("Project Management App")
dev_name = st.text_input("Developer Name")
dev_experience = st.number_input("Experience (Years)" , min_value=0, max_value=50,value=0)

if st.button("Create Developer"):
    dev_data = {"name": dev_name, "experience": dev_experience }
    response = requests.post("http://127.0.0.1:8000", json=dev_data)

st.header("Create Project")
proj_title = st.text_input("Project Title")
proj_desc = st.text_area("Project Description")
proj_lang = st.text_area("languages used (comma-separated)")
lead_dev_name = st.text_input("Lead Developer Name")
lead_dev_data= st.number_input("lead Developer Experience(Years)" , min_value=0, max_value=50,value=0)

if st.button("Create Project"):
    lead_dev_experience = {"name": lead_dev_name,"experience": lead_dev_exp}
    proj_data = {
        "title": proj_title,
        "description": proj_desc,
        "languages":proj_lang.split(","),
        "lead_developer": lead_dev_data
    }

response = requests.post("http://127.0.0.1:8000", json=projects)
st.json(response.json())

# Display Projects in a Dashboard Format
st.header("Project Dashboard")

if st.button("Get Projects"):
    response = requests.get("http://127.0.0.1:8000/projects")
    project_data = response.json()["projects"]

    if project_data:
        projects_df = pd.DataFrame(project_data)

        st.subheader("Projects Overview")
        st.dataframe(projects_df)

        st.subheader("Project Details")
        for projects in project_data:
            st.markdown(f"### **{projects['title']}**")
            st.markdown(f"**Description:** {projects['description']}")
            st.markdown(f"**Languages Used:** {', '.join(projects['languages'])}")
            st.markdown(
                f"**Lead Developer:** {projects['lead_developer']['name']} "
                f"with {projects['lead_developer']['experience']}"
            )
            st.markdown("---")
    else:
        st.warning("No Projects Found")
