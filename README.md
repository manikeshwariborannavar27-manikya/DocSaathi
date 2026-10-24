# 📄 DocSaathi

**Government documents, made simple.**
A privacy-first guide that tells Indian citizens exactly which documents to carry, how to apply, and where the official portal is, *before* they stand in a queue.

> ⚠️ DocSaathi is an independent guidance tool. It is **not** affiliated with, or endorsed by, any government body. Always confirm final requirements on the official portal.

![DocSaathi home screen](docs/screenshots/home.png)
<img width="1887" height="938" alt="Screenshot 2026-10-22 224358" src="https://github.com/user-attachments/assets/a0e9eb27-1944-42dc-9891-f604990d66f2" />
<!-- Replace with a real screenshot, or embed your demo: [![Watch the demo](docs/screenshots/home.png)](YOUR_VIDEO_LINK) -->

---

## ✨ Why DocSaathi?

Most people get turned away from a government office for one boring reason: **a missing photocopy or an unaccepted proof.** DocSaathi removes that guesswork.

**Example:** Renewing a passport?

1. Search "Passport Renewal" (or pick it from *Popular Citizen Needs*).
2. Open the checklist: Proof of Identity, Proof of Address, Proof of Date of Birth *(Mandatory)*, Old Passport *(If Applicable)*.
3. Read the step-by-step procedure (fees, appointment booking, biometrics, police verification).
4. Tap **Go to Official Portal** to land directly on the verified `.gov.in` service.

---

## 🚀 Features

| Feature | What it does |
| --- | --- |
| **Find by Purpose** | Task-based cards (Passport appointment, Driving Licence & Renewal, Vehicle Registration / RC Transfer, Voter ID enrolment, Income/Caste/Domicile certificates, Ration Card). |
| **Smart Checklists** | Required proofs grouped as Identity (POI), Address (POA) and Date of Birth, with **Mandatory** and **If Applicable** tags and a tick-off checkbox for each item. |
| **Step-by-Step Procedures** | Plain-English walkthroughs with fees, timelines and warnings (e.g. never use unofficial touts or third-party agencies). |
| **Explore Government Documents** | A statutory directory (Aadhaar, PAN, Passport, and more) with category filters such as Identity & KYC, Financial & Tax, Transport & Mobility, Civil & Electoral, Civil & Welfare, Revenue & Welfare. Each entry shows common uses, a carry-list, validity period and official portal. |
| **Direct Official Links** | Every guide ends with a link to the relevant government portal (UIDAI, Parivahan Sarathi, NSDL/Protean, Election Commission, Passport Seva, etc.). |
| **Optional Renewal Tracker** | Save expiry dates for documents like Driving Licence, Vehicle Insurance, PUC, Passport, RC Fitness, Health Insurance and Income Certificate, and get clear *Expired* / *X days left* badges. |
| **Responsive UI** | Clean forest-green design that works on desktop and mobile. |

---

## 🔒 Privacy by Design

- **No sign-up, no login, no profile.**
- **Zero identity numbers collected.** No Aadhaar, PAN, EPIC, phone number or date of birth is ever requested.
- **Local-only tracker.** Renewal reminders live in your browser's `localStorage`. Nothing is uploaded or transmitted to a server.
- **No document uploads.** DocSaathi is purely a reference checklist.

---

## 🛠️ Tech Stack

- **Frontend:** React + Vite
- **Styling:** Custom CSS (forest green, cream and sage palette)
- **Storage:** Browser `localStorage` (tracker only)
- **Content:** Statically curated guidance sourced from official portals and gazettes

<!-- Add or remove lines here to match your final build (e.g. FastAPI / SQLite / Ollama if you ship them). -->

---

## ⚙️ Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/docsaathi.git
cd docsaathi

# 2. Install dependencies
npm install

# 3. Start the dev server
npm run dev
```

Then open the local URL printed in your terminal (usually `http://localhost:5173`).

To create a production build:

```bash
npm run build
npm run preview
```

---

## 🗂️ Project Structure

```text
docsaathi/
├── public/
├── src/
│   ├── components/     # Navbar, checklist modal, tracker, cards
│   ├── data/           # Document and procedure content
│   ├── pages/          # Home, Find by Purpose, Explore, How It Works
│   └── main.jsx
├── index.html
└── package.json
```
<!-- Adjust the tree to match your actual folders. -->

---

## 🗺️ Roadmap

- [ ] Kannada language support (and more Indian languages after that)
- [ ] State-specific guidance for more services
- [ ] Reminder notifications for upcoming expiries
- [ ] Printable checklists

---

## 🤝 Contributing

Contributions are welcome, especially corrections to document requirements and new state-specific guides.

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push and open a Pull Request

When updating guidance content, please cite the official source in your PR.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for details.

---

## 👩‍💻 Author

**Manikeshwari**
GitHub: [@your-username](https://github.com/manikeshwariborannavar27-manikya) · LinkedIn: [your-profile](https://linkedin.com/in/manikeshwari-borannavar-7a27123aa)

*Built so that no one is ever turned away from a counter again.*
