# CheckPoint Script Builder
A Python Flask web GUI to create mgmt_cli scripts to automate CheckPoint firewall tasks.

Current functionality is limited to creating new hosts (which in turn creates a group object for each host). The page then allows you to download the script you can use to import into SmartConsole via the SmartConsole command line widget.

![Page Screenshot](/images/site_image.jpg)

The CSS is mostly copied from the w3schools.com css boilerplate template. Most of it is unused but left alone for now in case something becomes useful.

Currently there is only the base html page with no extends. 

TODO:
- Add CSV import funcationality
- Break HTML into pages using extends
- Add component to create other objects
- Add delete functionality
- Add ability for rule creation
