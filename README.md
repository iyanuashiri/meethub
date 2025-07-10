# MeetHub

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b0d1d86ada1848968faf19b9904f1382)](https://app.codacy.com/app/iyanuashiri/meethub?utm_source=github.com&utm_medium=referral&utm_content=iyanuashiri/meethub&utm_campaign=badger)

MeetHub is an open source event management system built with Python and Django web framework. It helps users create, discover, and manage events easily.

## Features
* 📅 Event Creation and Management
* 🔔 Real-time Notifications System
* 💬 Event Comments and Discussions
* 👥 User Profiles
* 🔍 Event Discovery
* 📱 Responsive Design

## Screenshots

<details>
<summary>Click to view screenshots</summary>

### Landing Page
![landing page](https://res.cloudinary.com/iyanuashiri/image/upload/v1752105312/MeetHub-Connect-Meet-Grow-07-10-2025_12_23_AM_zdofem.png)

### Explore Page
![explore page](https://res.cloudinary.com/iyanuashiri/image/upload/v1752105309/Discover-Amazing-Events-MeetHub-07-10-2025_12_25_AM_xtot9e.png)

### Event Creation
![create event](https://res.cloudinary.com/iyanuashiri/image/upload/v1752105309/Create-Amazing-Event-MeetHub-07-10-2025_12_25_AM_gz7fik.png)

### Notifications
![notifications](https://res.cloudinary.com/iyanuashiri/image/upload/v1752105309/MeetHub-Connect-Meet-Experience-07-10-2025_12_26_AM_vjrflb.png)

### User Profile
![profile](https://res.cloudinary.com/iyanuashiri/image/upload/v1752105310/MeetHub-Connect-Meet-Experience-07-10-2025_12_27_AM_hohgpo.png)

### Login Page
![login](https://res.cloudinary.com/iyanuashiri/image/upload/v1752105726/Sign-In-MeetHub-07-10-2025_01_01_AM_f5jvkb.png)

### Signup Page
![signup](https://res.cloudinary.com/iyanuashiri/image/upload/v1752105727/Join-MeetHub-Create-Your-Account-07-10-2025_01_01_AM_uwg9od.png)

</details>

## Installation

### Prerequisites
- Python 3.6+
- pip
- virtualenv (recommended)


## Setup

virtual environment 
1. Clone the repository `git clone https://github.com/iyanuashiri/meethub.git`
2. Create a virtual environment `python -m venv venv`
3. Activate the virtual environment `venv\Scripts\activate` on windows or `source venv/bin/activate` on linux
4. Install the requirements `pip install -r requirements.txt`
5. Run the migrations `python manage.py migrate`
6. Run the server `python manage.py runserver`

uv
1. Clone the repository `git clone https://github.com/iyanuashiri/meethub.git`
2. uv sync
3. uv run python manage.py migrate
4. uv run python manage.py runserver

docker
1. Clone the repository `git clone https://github.com/iyanuashiri/meethub.git`
2. docker build -t meethub .
3. docker run -p 8000:8000 meethub



## Cloud services 

1. Cloudinary
2. SendGrid
3. Render
4. NeonDB
5. Redis.io

## Environment variables

1. SECRET_KEY
2. DATABASE_NAME=
3. DATABASE_USER=
4. DATABASE_PASSWORD=
5. DATABASE_HOST=
6. DATABASE_PORT=
7. DEBUG=True
8. CLOUDINARY_NAME=
9. CLOUDINARY_API_KEY=
10. CLOUDINARY_API_SECRET=


Visit `http://localhost:8000` in your browser.

## Roadmap
- [ ] Add comprehensive test suite
- [ ] Implement REST API
- [ ] Add threaded comments
- [ ] Add location-based event exploration
- [ ] Implement social authentication
- [ ] Add event categories and tags
- [ ] Enable event sharing on social media

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
