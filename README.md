# ACM Discord Bot 

To extend the bot, create a class in ```handlers/``` that inherits ```handlers/message_handle.py``` and implements the ```handle_message()``` method. Then add the module name to config.json.

An example ```test.py``` can be found in the ```handlers/``` directory.

To contribute, please fork the project, make your changes, commit them, and create a pull request. Unfortunatly for security reasons we cannot provide an api token for the bot in source control so you will be unable to test the code yourself. As such the pull request will give us a chance to pull your code and make sure it works. When creating a pull request, please make sure to document what the extension does.

Robbot is built with [discord.py](https://github.com/Rapptz/discord.py)
