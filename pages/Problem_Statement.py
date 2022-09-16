import streamlit as st
from io import BytesIO
import base64



st.title("Voting Database Design")
st.header("We want that the system should be made keeping in mind the following things:")
st.header("• The vote of each member is equally weighed.")
st.header("• Voting should be anonymous, and no one should be able to see who voted for what.")
st.header("• An admin would monitor the entire election process.")
st.header("• The admin should be able to appoint some person to assist him during some election process.")
st.header("• Admin and candidates should have a vote for themselves.")
st.header("• Admin should be able to take voting for making some decision or electing some person.")
st.header("• The list of all candidates should be visible to everyone in the organization.")
st.header("• The candidates should be able to withdraw their names up to a specific time limit.")
st.header("• Only the members of the organization should be able to vote.")
st.header("• The system should be easy to use for adding and removing members from the organization.")
st.header("• Only the admin should be able to modify the details of a voter.")
st.header("• Only the admin should be able to monitor live voting.")
st.header("• The admin should be able to remove candidates from ongoing elections if they are caught using unfair means.")
st.header("• The system should also allow voters to make some decisions.")
st.header("• Once the voting is done, everyone in the organization should be able to see the results.")