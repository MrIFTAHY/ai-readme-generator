
import streamlit as st

st.set_page_config(
    page_title="AI README Generator",
    page_icon="📄",
    layout="centered"
)

st.title("AI README Generator")
st.write("Generate a professional GitHub README file in seconds.")

project_name = st.text_input("Project Name")
description = st.text_area("Project Description")
tech_stack = st.text_input("Tech Stack")
features = st.text_area("Main Features")
installation = st.text_area("Installation Steps")
usage = st.text_area("Usage Instructions")

license_type = st.selectbox(
    "License Type",
    ["MIT", "Apache 2.0", "GPL v3", "BSD 3-Clause", "No License"]
)

template_type = st.selectbox(
    "Project Type",
    ["General Project", "AI Project", "Web App", "Python Package"]
)

if st.button("Generate README"):
    if project_name and description:

        readme = f"""# {project_name}

              
## Project Type

{template_type}

## Description

{description}

## Features

{features}

## Tech Stack

{tech_stack}

## Installation

{installation}

## Usage

{usage}

## License

{license_type}
"""

        st.subheader("Generated README")
        st.code(readme, language="markdown")
        st.download_button(
    label="📥 Download README.md",
    data=readme,
    file_name="README.md",
    mime="text/markdown"
)