# Use the official OWASP ZAP Docker image
FROM owasp/zap2docker-stable

# Copy the scan and report generation script into the container
COPY zap-scan.sh /zap/zap-scan.sh

# Make the script executable
RUN chmod +x /zap/zap-scan.sh

# Default command to run the script
CMD ["/zap/zap-scan.sh"]
