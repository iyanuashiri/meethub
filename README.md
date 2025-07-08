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

### Explore Page
![explore page](https://res.cloudinary.com/iyanuashiri/image/upload/v1526323111/Screenshot-2018-5-14_Find_Your_Events_6.png)

### Event Creation
![create event](https://res.cloudinary.com/iyanuashiri/image/upload/v1526323111/Screenshot-2018-5-14_Find_Your_Events_5.png)

### Notifications
![notifications](https://res.cloudinary.com/iyanuashiri/image/upload/v1526323232/Screenshot-2018-5-14_Find_Your_Events_1.png)

### User Profile
![profile](https://res.cloudinary.com/iyanuashiri/image/upload/v1526323111/Screenshot-2018-5-14_Find_Your_Events_7.png)

### Login Page
![login](https://res.cloudinary.com/iyanuashiri/image/upload/v1526323111/Screenshot-2018-5-14_MeetHub.png)
</details>

## Installation

### Prerequisites
- Python 3.6+
- pip
- virtualenv (recommended)

### Setup
1. Clone the repository
```bash
git clone https://github.com/iyanuashiri/meethub.git
cd config
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Run migrations
```bash
python manage.py migrate
```

6. Start the development server
```bash
python manage.py runserver
```

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
