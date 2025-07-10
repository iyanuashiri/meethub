# MeetHub

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b0d1d86ada1848968faf19b9904f1382)](https://app.codacy.com/app/iyanuashiri/meethub?utm_source=github.com&utm_medium=referral&utm_content=iyanuashiri/meethub&utm_campaign=badger)

MeetHub is an open-source event management system built with Python and the Django Web Framework. It's designed to help people create, discover, and manage events, fostering community and connection. Whether you're organizing a tech meetup, a book club, or a hiking trip, MeetHub provides the tools to bring people together. As a learning platform, it offers a practical, real-world codebase for developers looking to gain experience with Django, containerization, and modern web development practices.


## ✨ Features

*   **📅 Event Creation & Management:** Easily create, update, and manage your own events.
*   **🔍 Event Discovery:** Explore a list of upcoming events to join.
*   **👥 User Profiles:** Create a personal profile and see who's attending events.
*   **💬 Event Discussions:** Comment on events to ask questions and connect with attendees.
*   **🔔 Real-time Notifications:** Get notified about relevant activities.
*   **📱 Responsive Design:** A clean, modern UI that works on any device.

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

## 🚀 Why Contribute to MeetHub?

*   **Learn Django:** Get hands-on experience with a real-world Django application.
*   **Make an Impact:** Your contributions will directly improve a tool for community building.
*   **Join a Welcoming Community:** We are excited to help new contributors get started.

## 🛠️ Technology Stack

*   **Backend:** Python, Django
*   **Database:** PostgreSQL (production), SQLite3 (development)
*   **Frontend:** HTML, CSS, Bootstrap 5, JavaScript
*   **Deployment:** Docker, Gunicorn, Whitenoise
*   **Package Management:** `uv`
*   **Cloud Services:** Cloudinary (for media), NeonDB (for database), Render (for hosting)

## 🏁 Getting Started

You can run MeetHub using `uv` (recommended for development) or Docker or virtual environment. 

## Installation

### Prerequisites
- Python 3.12+
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
2. `uv sync`
3. `uv run python manage.py migrate`
4. `uv run python manage.py runserver`
5. Create a superuser (for admin access): `uv run python manage.py createsuperuser`

docker
1. Clone the repository `git clone https://github.com/iyanuashiri/meethub.git`
2. `docker build -t meethub .`
3. `docker run -p 8000:8000 --env-file .env meethub`
4. Create a superuser (for admin access): `docker exec -it meethub python manage.py createsuperuser`
5. The app will be available at http://localhost:8000. The entrypoint script will automatically run migrations.

Visit http://127.0.0.1:8000 in your browser!

## Cloud services 

1. Cloudinary
2. Render or any other hosting service
3. NeonDB or any other database service
4. 

## Environment variables

Before you start, copy the example environment file and fill in your details.
```bash
cp .env_example .env
```

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

You will need to set the SECRET_KEY. For local development, you can leave the database and Cloudinary variables blank to use SQLite and local media storage.

Visit `http://localhost:8000` in your browser.





Add threaded comments for better discussions
Add location-based event exploration (e.g., with a map)
Implement social authentication (Google, GitHub)
Add event categories and tags for better filtering (good first issue)
Enable event sharing on social media


## Roadmap
We have a lot of exciting features planned! Here are some ideas, many of which are great for first-time contributors.
- [ ] Add a comprehensive test suite (help wanted, sprint)
- [ ] Implement REST API for a mobile-friendly experience
- [ ] Add threaded comments for better discussions
- [ ] Add location-based event exploration (e.g., with a map)
- [ ] Implement social authentication (Google, GitHub)
- [ ] Add event categories and tags for better filtering (good first issue)
- [ ] Enable event sharing on social media

## Contributing
Contributions are welcome! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
Please feel free to submit a Pull Request. See our Contributing Guide for details on our code of conduct and the process for submitting pull requests to us.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
