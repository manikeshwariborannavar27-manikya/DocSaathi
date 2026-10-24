# DocSaathi (डॉक साथी) 🇮🇳
### Government Document Guidance & Preparation Platform for Indian Citizens

DocSaathi is an independent, privacy-first government document guidance and preparation assistant built for everyday citizens across India. It helps citizens understand which documents they need for public services, prepare accepted proofs of identity, address, and age before visiting a Seva Kendra or government office, and discover direct links to verified official application portals.

---

## 🌿 Aesthetics & Design Direction (Reference Match)
- **Palette:** Soothing Mint & Deep Teal (`#0F766E`, `#0D9488`, `#14B8A6`, `#2DD4BF`), Soft Sage / Mint Light (`#E6F7F5`, `#F0FDFA`), Warm Off-White (`#FBFBF9`, `#F8FAF9`, `#FFFFFF`), and subtle Saffron warm accents (`#E07A5F`, `#F59E0B`).
- **Typography:** Fraunces (Variable Editorial Serif) for trustworthy headings and Inter for crisp, accessible UI readability.
- **Fluid Organic Shapes:** Soft circular fluid teal backdrop curves matching the reference design.
- **Accessible & Responsive:** Pill-shaped accessible buttons, clear contrast, and fully responsive layouts for mobile, tablet, and desktop.

---

## 🔒 Privacy-First Architecture

- **No Mandatory Login or Account:** Citizens can access all document guides, preparation checklists, and official portal links without registration.
- **Zero Identity Numbers Collected:** We never ask for your 12-digit Aadhaar number, PAN, voter EPIC number, phone number, date of birth, or home address.
- **No Document Uploads or Scans:** No document files, scans, certificates, or photos are ever requested or uploaded to our servers.
- **Optional Client-Side Renewal Tracker:** If you choose to track renewal dates (e.g. driving licence or car insurance), data is stored strictly in your browser’s `localStorage`. Nothing is sent to any server or external cloud.
- **No Third-Party Tracking:** No personal data is sent to external AI services or advertising trackers.

---

## 📋 Core Platform Features

### 1. Find by Purpose (Citizen Tasks)
Step-by-step guidance and preparation checklists for 10+ essential citizen services:
- **Aadhaar Card:** Address Update & Mobile Linking
- **PAN Card:** Applying for New (Form 49A) / Correction (CSF) / Instant e-PAN
- **Indian Passport:** Fresh Normal / Tatkaal / Re-issue / Renewal
- **Driving Licence Services:** Learner's Licence (LL), Permanent DL, and Renewal
- **Vehicle Registration Services (RC):** Ownership Transfer, Hypothecation Removal, Duplicate RC
- **Voter ID (EPIC):** New Voter Registration (Form 6), Address Shift (Form 8)
- **State Revenue Certificates:** Income, Caste (SC/ST/OBC), and Domicile/Residence
- **Ration Card:** New Family Ration Card & Member Addition
- **Birth & Death Certificates:** Registration within 21 days & delayed issuance
- **Ayushman Bharat PM-JAY:** Cashless Health Card up to ₹5 Lakh

### 2. Interactive Preparation Checklist with Print Support
Citizens can check off items as they gather them at home (Proof of Identity, Proof of Address, Proof of Date of Birth, Photos, Application forms), and click **Print / Save Checklist** to take a physical copy to their local Seva Kendra or cyber cafe.

### 3. Explore Government Documents (Directory)
Authoritative catalog of Indian statutory documents with plain-English descriptions, common uses, accepted proofs list, validity rules, and issuing authorities.

### 4. Verified Official Government Portals Directory
Direct links to authorized government portals:
- **UIDAI MyAadhaar:** `https://myaadhaar.uidai.gov.in`
- **Parivahan Sarathi:** `https://sarathi.parivahan.gov.in`
- **Parivahan Vahan:** `https://vahan.parivahan.gov.in`
- **Passport Seva:** `https://www.passportindia.gov.in`
- **ECI Voters Portal:** `https://voters.eci.gov.in`
- **Income Tax e-Filing:** `https://www.incometax.gov.in/iec/foportal/`
- **NFSA Portal:** `https://nfsa.gov.in`
- **National Services Portal:** `https://services.india.gov.in`
- **Civil Registration System (CRS):** `https://crsorgi.gov.in`
- **DigiLocker:** `https://www.digilocker.gov.in`

### 5. Optional Renewal Tracker (LocalStorage Only)
A clean personal utility to track upcoming expiries (Driving Licence, Car Insurance, PUC, Passport) without entering any sensitive identity numbers or uploading documents.

---

## ⚖️ Statutory Disclaimer
DocSaathi is an independent informational guidance tool and is **NOT a government website or an official government service**. We are not affiliated with, authorized, or endorsed by the Government of India or any state government. All official applications must be accessed directly through respective government portals.

---

## 🏃 Running the Project Locally

### 1. Backend (FastAPI)
```bash
.\venv\Scripts\python.exe -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
```
API Documentation: `http://127.0.0.1:8000/docs`

### 2. Frontend (React + Vite)
```bash
npm run dev
```
Open in browser: `http://localhost:5173/`
