import streamlit as st

# Function to be called when the "Find Matches" button is clicked
def find_matches():
    st.write("Finding matches...")

# Main function to create Streamlit UI
def main():
    st.title("Resume Shortlisting")

    # Create two columns for button layout
    col1, col2 = st.columns(2)

    # First column: Job details
    with col1:
        # st.header("Job Details")
        job_title = st.text_input("Job Title:")
        job_description = st.text_area("Job Description:")
        key_skills = st.text_input("Key Skills (comma-separated):").split(", ")
        work_experience = st.selectbox("Work Experience:", ["Fresher", "1-3 years", "3-5 years", "5+ years"])
        industry = st.text_input("Industry:")

    # Second column: Additional details
    with col2:
        # st.header("")
        min_qualification = st.text_input("Minimum Qualification:")
        status = st.text_input("Status:")
        nature_of_job = st.text_input("Nature of Job:")
        location_of_job = st.text_input("Location of Job:")
        sector = st.text_input("Sector:")

    # Button to find matches
    if st.button("Find Matches"):
        find_matches()

if __name__ == "__main__":
    main()
