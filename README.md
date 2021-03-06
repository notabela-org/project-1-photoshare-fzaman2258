[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=4283653&assignment_repo_type=AssignmentRepo)
# Project 1 | **PhotoShare**

**PhotoShare** - A simple PhotoSharing Application
Time spent: **15** hours spent in total

## User Stories

The following **required** functionality is completed:

- [X] User can sign up to create a new account
- [X] User can log in and log out of her account
- [x] Each user has a profile page that shows her username, profile photo, short bio and all their posts
- [x] A Logged in user can edit her profile photo, her username and short bio (only hers but not others)
- [x] A Logged in User can create a new post by uploading a photo and adding a description
- [ ] A Logged in User can add a comment on a post
- [x] A Logged in User can view all the posts submitted on the platform, each posts shows the post's user's username and profile photo, when the post was created, the post's photo, the description and number of comments
- [x] Tapping on a post's user's username or profile photo goes to that user's profile page
- [ ] A Logged in user can view all the comments on a post, each comment shows the username and profile photo of the user who posted the comment and the date the comment was posted
- [x] Anonymous users (unathenticated users) can only access the sign up and login pages

The following **optional** features are implemented:

- [ ] A Logged In User can like and Unlike posts (might require some javascript to work properly)
- [x] Posts view is paginated
- [ ] A User can submit and accept friend requests
- [ ] A User cannot see another user's post unless they are friends
- [x] A user can reset their password if they forgot (will likely require adding email to sign up) 
**There is a caveat, that I didn't include my own gmail account as the one to send emails for password resets, but if included it will work**

## TESTING
Code Coverage: [insert_coverage_here]

A coverage report is included at: [insert coverage report path]

## Video Walkthrough

Here's a walkthrough of implemented user stories:

<img src='[insert_gif_source_here]' title='Video Walkthrough' alt='Video Walkthrough' />

GIF created with [LiceCap](http://www.cockos.com/licecap/).

## Notes

### Describe any challenges encountered while building the app.
I rebuilt the user login, logout functionality as I think it was a good experience to learn how that works. I spent a lot of time researching and reading documentation to learn how all parts fit together and works. I found that I slightly deviated from some of the requirements like if you click on a person's name I show you their post history. I found storing images and loading images wasn't the most obvious and had to tinker with settings.py. To set up a reset password I had to define a lot of variables in settings.py and I had to change the settings of my gmail account to test if it works.

## License

    Copyright [2021] [Farhan Zaman]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
