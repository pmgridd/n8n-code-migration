# Use the official n8n image as the base
FROM n8nio/n8n:latest

# Switch to the root user to gain permission to install packages
USER root

# Install your desired npm packages globally
# Use the --global (-g) flag
RUN npm install --global axios

RUN mkdir -p /git_projects
RUN chmod -R 777 /git_projects

# # Switch back to the non-root 'node' user for security
USER node
