# RFID-based-Attendance-System-using-Arduino

# 📌 Overview
The **RFID-Based Attendance Generating System** is an automated system designed to track and record attendance using RFID (Radio Frequency Identification) technology. This project eliminates manual attendance processes and enhances security and efficiency in schools, offices, and other organizations.

# 🔧 Features
- **RFID Authentication:** Uses RFID tags for quick and secure attendance marking.
- **Real-time Data Logging:** Stores attendance records in a database.
- **LCD Display:** Provides real-time feedback when attendance is marked.
- **User-Friendly Interface:** Simple and intuitive design for easy operation.

# 🏗️ System Architecture
The system consists of the following components:
1. **RFID Reader (e.g., RC522/EM18):** Scans RFID tags.
2. **Microcontroller (e.g., Arduino uno ):** Processes RFID data and updates attendance records.
4. **Web Dashboard (Python):** Displays attendance records.

#🛠️ Installation & Setup
### Hardware Requirements
- RFID Reader (RC522/EM18)
- RFID Tags
- Microcontroller (Arduino uno)
- LCD Display (I2C lcd display)
- Power Supply
- Connecting Wires

### Software Requirements
- Arduino IDE / Python / Any microcontroller IDE
- MySQL / Firebase Database
- Web Technologies (Python)
- Libraries: `MFRC522`, `SPI`,, (if using Python)

# Steps to Setup
1. **Upload Code to Microcontroller**
   - Open Arduino IDE and upload the RFID reader code.
   - Ensure the necessary libraries are installed.
2. **Set Up the Database**
   - Create a MySQL/Firebase database.
   - Import the provided SQL script.
3. **Run the Web Dashboard**
   - Install required dependencies.
   - Start the server using:
     ```sh
     python app.py  # For Python
     php -S localhost:8000  # For PHP
     ```
4. **Connect Hardware and Test**
   - Power on the system.
   - Scan RFID tags to mark attendance.

## 📊 How It Works
1. An individual scans their RFID tag using the reader.
2. The microcontroller verifies the tag ID.
3. If authenticated, attendance is marked and logged in the database.
4. A notification is displayed on the LCD screen (if available).
5. The attendance record is accessible on the web dashboard.

## 🚀 Future Enhancements
- **Face Recognition Integration** for dual authentication.
- **SMS/Email Notifications** for absentee alerts.
- **Mobile App Support** for easy access.
- **Cloud-Based Database** for remote access.

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch.
3. Make improvements and submit a pull request.

## 📜 License
This project is licensed under the [MIT License](LICENSE).

## 📬 Contact
For queries, reach out via:
- Email: nishanthgowdars07@gmail.com
- GitHub: https://github.com/Nishanth262
---
**📢 Star this repository if you find it useful!** ⭐

