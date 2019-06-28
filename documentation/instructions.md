# Instructions for use

You can access the application by [Heroku](https://tsoha-golem.herokuapp.com/) or building it locally and connecting to it by [http://localhost:5000/](http://localhost:5000/). The instructions for installing and running the app locally can be found at [installing](https://google.com/).

## The anonymous index page

When you first open the application you will be greeted by an index page. When not logged in you should only see the 'List campaigns' option in the top bar and the 'Login' option at the top right corner. The index page has a link from where you can register a new account.
	
## Registration

The registration view asks for your new account's username and password along with a confirmatory 'repeat password' box. The username can't already exist in the database and it has to be at least 3 characters long, the password has to be atleast 7 characters long and it must match the 'repeat password' field. If you want to create the admin account you just have to name your accout 'admin'.

## The login page

The login page is quite self-explanatory, you need to have an existing account to log in, and if you do not you can make one by clicking the registration link on the page.

## The user index view

When you have logged in to a regular user account, your index view gains more functionality. The top bar now lets you list your existing characters and create new campaigns and the page itself lists all your campaigns and active characters. You can also log out using the link at the top right corner.

## The admin index view

The admin index view is otherwise similar to the user one, but it has the admin view as one of it's top bar links.

## The campaign list view

This view simply lists all existing campaigns and gives you an option to create new ones if you are logged in.

## The character list view

This view lists all characters in all campaigns that are linked to the current user. It separates active an inactive characters for clarity.

## The campaign creation view

Here you can create new campaigns that you can then manage. It asks you for the campaign's name and the starting point total for the campaign's characters. At the moment the campaign name must be between 3 and 40 characters long and the starting point total must be between 0-300.

## The campaign player index view

This view lists all of your active and inactive characters in this campaign and it also gives you the option to create new chraters for this campaign.

## The campaign owner index view

This view lists and lets you access all active and inactive characters in the campaign.

## The character creation view

Here you can create new characters to the selected campaign. At the moment the only information it asks for is the character's name, which must be between 1 and 30 characters long.

## The character index view

Here you can see an overview of the selected character. It gives you the options of deactivating/reactivating and deleting the character, and the deletion option will ask for confirmation before deleting your charater. Only the character's owner of the owner of the campaign the characters belongs to can use any if this view's functionality. You can also modify your characters stats, which will either cost or gain you points. The stats have stat-specific modification costs, minimums and maximums.

## The admin view

At the moment the only admin-specific functionality is the creation of skills, which you can do in the admin view. The view also lists all the existing skills. The skill are not currently related to anything, but in the future campaign configuration will let you pick which skills exist in your campaign, and characters can then learn those skills. 
