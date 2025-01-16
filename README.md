# RedTrace-Ransomware

**RedTrace-Ransomware** is an educational project designed to demonstrate how ransomware operates and to help developers and security enthusiasts better understand its mechanisms. This project is strictly intended for ethical purposes, such as learning about ransomware behavior and improving cybersecurity defenses.

---

## ⚠️ Disclaimer

**This project is for educational purposes only.** 

The code in this repository should never be used for malicious or illegal activities. The author, Hector, takes no responsibility for any misuse of this code. By using this repository, you agree to use it ethically and in compliance with applicable laws and regulations.

---

## 🔍 Features

- Demonstrates file encryption techniques typically used in ransomware.
- Provides insights into how malicious actors design such software.
- A tool for cybersecurity students and professionals to study ransomware behavior in a controlled and safe environment.

---

## 🛠️ Setup and Usage

### Prerequisites

- Python 3.7 or higher
- Required Python libraries (see `requirements.txt`)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/HectorsGrav3/RedTrace-Ransomware.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd RedTrace-Ransomware
   ```

3. **Install dependencies**
   Install the required Python libraries listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the script**
   Use the following command to run the ransomware script:
   ```bash
   python redtrace.py
   ```
   (you could use pyinstaller to make it an exe if needed)

5. **Testing environment**
   - Ensure you run this script in an isolated or virtualized environment (e.g., a virtual machine) to avoid unintended consequences.
   - Do **not** run this script on a system containing sensitive or important data.

6. **Outputs**
   - The script will scan the specified drives and encrypt files with defined extensions.
   - It will create a `README.txt` file on the desktop with instructions and a unique ID.
   - The desktop wallpaper will be changed as part of the demonstration.

### Note

- Also change the fields **your email** and **Bitcoin Adress** fiels in the code.
- Also please note that you will need to add the image link to the code for the wallpaper that you will need to upload somewhere. (the image is in the repository)
- The script sends encryption keys and unique IDs to a specified Telegram bot. Ensure that you configure the `bot_token` and `chat_ids` in the script if you wish to use this feature.
- Be aware of ethical and legal considerations before running this script.

---

## 🛡️ Ethical Usage

The purpose of this repository is to:

- Educate developers and IT professionals about the dangers of ransomware.
- Help cybersecurity professionals develop defenses against such threats.
- Provide insights into encryption techniques.

This repository is **not** intended for:

- Unauthorized use against individuals, organizations, or systems.
- Deploying malicious software or violating any laws.

---

## 👨‍💻 Author

**Hector**  
Developer and cybersecurity enthusiast  

Feel free to connect or reach out for questions and discussions.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). By using this code, you agree to adhere to the terms of the license.

---

## 🤝 Contributions

Contributions are welcome! If you have ideas to improve this project or enhance its educational value, feel free to submit a pull request.

---

## 🧠 Learn More

To learn more about ransomware and how to protect against it, check out these resources:

- [OWASP Top Ten Security Risks](https://owasp.org/www-project-top-ten/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [How to Defend Against Ransomware](https://www.cisa.gov/stopransomware)

---

### 🚨 Use Responsibly

This project is a tool for learning and awareness. Always use responsibly and report any misuse to the appropriate authorities.

