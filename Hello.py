import streamlit as st
import requests
import json

# Set page title and favicon
st.set_page_config(
    page_title="InternetDB IP Lookup", page_icon=":globe_with_meridians:"
)


# App title and description
st.title("InternetDB IP Lookup :globe_with_meridians:")
st.markdown(
    """
    This tool allows you to quickly lookup information about open ports, vulnerabilities, and other details for a given IP address using the InternetDB API.

    Enter an IP address below to get started!
    """
)

# IP input
ip_address = st.text_input("IP Address", placeholder="Enter an IP address")

if ip_address:
    try:
        # Make API request
        response = requests.get(f"https://internetdb.shodan.io/{ip_address}")
        data = response.json()
        if response.status_code == 200:
            # Display results
            st.markdown("## Results")

            # IP address
            st.markdown(f"**IP Address:** {ip_address}")

            # Open ports
            if "ports" in data:
                st.markdown("**Open Ports:**")
                st.write(data["ports"])

            # Hostnames
            if "hostnames" in data:
                st.markdown("**Hostnames:**")
                for hostname in data["hostnames"]:
                    st.markdown(f"- {hostname}")

            # Vulnerabilities
            if "vulns" in data:
                st.markdown("**Vulnerabilities:**")
                for vuln in data["vulns"]:
                    st.markdown(f"- {vuln}")

            # Tags
            if "tags" in data:
                st.markdown("**Tags:**")
                for tag in data["tags"]:
                    st.markdown(f"- {tag}")

        elif "detail" in data:
            st.warning(f"No Information found for IP Address: {ip_address}")

    except requests.exceptions.RequestException as e:
        st.error(f"Error occurred while making the API request: {str(e)}")