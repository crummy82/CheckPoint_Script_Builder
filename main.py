from flask import Flask, render_template, request, url_for, send_file, flash

# Create the Flask object for all this to work and have a key for passing data
app = Flask(__name__)
app.secret_key = b'ajfwo83jo83jfalfj((*DF(*^)(*&)'

# Primary / route for the site. Allow GET and POST methods.
@app.route('/', methods=['GET', 'POST'])
def index():
    hosts = []  # List to store hostnames
    ips = []    # List to store IPs
    comments = []   # List to store comments fields
    script_lines = []    # List to store lines of the script
    
    # Perform the following if the form is submitted
    if request.method == 'POST':
        hosts = request.form.get('new_hosts').splitlines()  # Retrieve each line of the 'new_hosts' text area and save in list 'hosts'
        ips = request.form.get('new_ips').splitlines()      # Retrieve each line of the 'new_ips' text area and save in list 'ips'
        comments = request.form.get('new_comments').splitlines()    # Retrieve each line of the 'new_comments' text area and save in list 'comments'
        file_name = request.form.get('file_name')   # Create string 'file_name' and store value from 'file_name' form field

        # Confirm there is an equal # of hosts, IPs, and comments.
        # If so, loop through the lists and append the hosts, IPs, and comments into the correct command to create the host object
        # Also append them into the command to create a group object
        if len(hosts) == len(ips) == len(comments):
            for count, host in enumerate(hosts):
                new_line = f'add host name "{host}" ipv4-address "{ips[count]}" comments "{comments[count]}"'
                script_lines.append(new_line)
                new_line = f'add group name "{host}-GO" members "{host}" comments "{comments[count]}"'
                script_lines.append(new_line)

            # Open a new file named in the 'file_name' form field
            # Loop through the saved script lines and dump them into the new file
            with open(file_name, "w") as output:
                for obj in script_lines: 
                    output.write(obj + "\n")

            return send_file(file_name, as_attachment=True) # Prompt the user to download the newly created file

        # If the # of hosts, IPS, and comments aren't the same, display an error and reload
        else:
            flash("Number of items in the boxes do not match!")

    # Load the base page for the site
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug='True')
