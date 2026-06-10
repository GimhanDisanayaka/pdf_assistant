🔮 **CHAKRA - Complete Installation & User Guide (සම්පූර්ණ ස්ථාපන සහ පරිශීලක මාර්ගෝපදේශය)**

This guide provides everything you need to set up, launch via CMD, and fully utilize the **CHAKRA** application. It is written in both English and Sinhala.

---

# 🇬🇧 ENGLISH VERSION

## 🛠️ Section 1: Installation & How to Run via CMD

### 📋 Prerequisites

* Make sure **Python 3.8+** is installed on your operating system. If not, download it from [python.org](https://www.python.org/).
* **Crucial:** During the Python installation process, make sure to check the box that says **"Add Python to PATH"**.

### 💻 Step-by-Step Execution

1. **Locate the Project Folder:** Open the directory on your computer where your project files, specifically the `app.py` script, are located.


2. **Open Command Prompt (CMD):** Click on the File Explorer address bar at the top of that window, type `cmd`, and press **Enter** to open the Command Prompt directly inside your project directory.
3. **Install Required Libraries:** Copy, paste, and execute the following command in your CMD window to install all necessary dependencies:


```bash

```



pip install streamlit pdfplumber reportlab pillow

```
   *(Optional: If you wish to enable PNG exports for your generated mind maps, you can also install `cairosvg` by running `pip install cairosvg`)*[cite: 1].
4. **Launch CHAKRA:** Start the application server by executing this exact command[cite: 1]:
   ```bash
streamlit run app.py

```

5. **Access the Interface:** Your default web browser will automatically load the local URL (typically `http://localhost:8501`). If it does not, manually copy and paste that address into your web browser.


* *To terminate the server, press `Ctrl + C` inside your CMD window.*



---

## 🔮 Section 2: Step-by-Step App Usage Guide

### ⚙️ Step 1: Sidebar API Configurations

When you open the app, look at the left sidebar panel to set up your AI environment:

* **AI Provider:** Select your provider, choosing either **OpenAI** or **Google Gemini**.


* **API Key:** Safely paste your secret credentials (`sk-...` for OpenAI or `AIza...` for Gemini). Your key is handled temporarily in your active session state and is never saved or logged.


* **Model Selection:** Use the dropdown menu to choose your preferred processing model flavor (e.g., `gpt-4o-mini`, `gemini-2.0-flash`, or `gemini-2.5-pro`).



### 📋 Step 2: Output Preferences Optimization

Customize how you want your study materials structured using the sidebar control elements:

* **Output Mode:** Pick one of the four core modules:


* *📝 Short Notes:* To convert a document into structured bullet-point summaries.


* *🧠 Quiz:* To build interactive multiple-choice testing materials.


* *💬 Q&A Pairs:* To extract targeted question-and-answer tracking components.


* *🗺️ Mind Map:* To create hierarchical layout visual breakdowns.




* **Max Pages Slider:** Determine how many pages the app processes (set from 1 to 100 pages; default is 15).


* **Number of Items Slider:** Decide how many items, questions, or entries you want generated (set from 3 to 20 items; default is 10).


* **Quiz Settings:** If you chose "Quiz", customize the response window using the **Seconds per question** slider (set from 10 to 60 seconds).


* **Sinhala Mode Toggle:** Check the **Show Sinhala meanings** box if you want the AI to automatically place Sinhala translations in parentheses right next to important technical terms.



### 📄 Step 3: Document Uploading

* Drag and drop your targeted academic **PDF file** into the designated dark layout upload zone, or click to browse files from your storage drives.


* Once uploaded, look at the interactive metric panels displaying **Total pages**, **Pages processed**, and the total number of **Characters extracted**.


* *(Optional)* Click the **Preview extracted text** expander to examine a quick snippet of the raw text reading data before processing.



### 🚀 Step 4: Generation and Interaction

Click the large **🚀 Generate [Your Selected Type]** button to send your parameters to the active AI engine.

* **If Short Notes:** Review the formatted layout notes on your dashboard. You can download them instantly using the action buttons underneath to save them as a plain text file (**Download as .txt**), a print-ready document (**Download as PDF**), or a convenient graphic layout (**Download as Image**).


* **If Interactive Quiz:** Test your knowledge against the questions while keeping an eye on the live red **⏱ Countdown Timer**. Click **📊 Submit Quiz** to instantly process your inputs and display your comprehensive **Score Box** percentage alongside correct/incorrect feedback (✅/❌) and written explanations (`💡`).


* **If Mind Map:** Review the glowing neon structural visualization chart. You can export it directly using the **Download SVG** or **Download as Image (PNG)** tools.


* **If Q&A Pairs:** Read through the direct problem-solution pairs and save them offline via the integrated **Download as .txt** channel.



---

---

# 🇱🇰 සිංහල අනුවාදය

## 🛠️ 1 වන කොටස: CMD හරහා ඇප් එක ඉන්ස්ටෝල් කර ක්‍රියාත්මක කරන ආකාරය

### 📋 පූර්ව අවශ්‍යතා

* ඔයාගේ පරිගණකයේ **Python 3.8+** සංස්කරණය ඉන්ස්ටෝල් කර තිබිය යුතුය. නැතහොත් [python.org](https://www.python.org/) වෙතින් එය බාගත කරගන්න.
* **மிக වැදගත්:** Python ඉන්ස්ටෝල් කරන අවස්ථාවේදී එහි ඇති **"Add Python to PATH"** කියන check box එකට tick එකක් දැමීමට අමතක නොකරන්න.

### 💻 පියවරෙන් පියවර ක්‍රියාත්මක කිරීමේ ක්‍රියාවලිය

1. **Project Folder එක වෙත යන්න:** ඔයාගේ පරිගණකයේ CHAKRA ඇප් එකට අදාළ කේත (විශේෂයෙන්ම `app.py` ෆයිල් එක) ගබඩා කර ඇති ෆෝල්ඩරය විවෘත කරන්න.


2. **Command Prompt (CMD) විවෘත කරන්න:** එම ෆෝල්ඩරයේ ඉහළින්ම ඇති Address bar එක මත click කර, එහි `cmd` ලෙස type කර **Enter** කරන්න. එවිට CMD තිරය කෙලින්ම එම ෆෝල්ඩරය තුළ විවෘත වේ.
3. **අවශ්‍ය Packages ඉන්ස්ටෝල් කිරීම:** ඇප් එක ක්‍රියාත්මක වීමට අවශ්‍ය වන Python පුස්තකාල (Libraries) ඉන්ස්ටෝල් කරගැනීම සඳහා පහත command එක CMD එක තුළ රන් (Run) කරන්න:


```bash

```



pip install streamlit pdfplumber reportlab pillow

```
   *(සටහන: ඔයා Mind Maps, PNG පින්තූර ලෙස බාගත කරගැනීමට කැමති නම්, `pip install cairosvg` command එක මඟින් එම package එකද ඉන්ස්ටෝල් කරගන්න)*[cite: 1].
4. **ඇප් එක සක්‍රීය කිරීම:** ඉන්ස්ටෝල් වීම අවසන් වූ පසු, සර්වර් එක ආරම්භ කිරීමට මෙම command එක ලබා දී **Enter** කරන්න[cite: 1]:
   ```bash
streamlit run app.py

```

5. **ඇප් එක භාවිතා කිරීම:** සර්වර් එක සක්‍රීය වූ සැනින් ඔයාගේ පරිගණකයේ ඇති Web Browser එක (Chrome/Edge) ස්වයංක්‍රීයව open වී ඇප් එක දර්ශනය වනු ඇත. එසේ නොවුවහොත් CMD එකෙහි දිස්වන `http://localhost:8501` යන ලින්ක් එක copy කර බ්‍රවුසරයට ඇතුළත් කරන්න.


* *ඇප් එක ක්‍රියාවිරහිත කිරීමට අවශ්‍ය නම් CMD window එක තුළ `Ctrl + C` ඔබන්න.*



---

## 🔮 2 වන කොටස: ඇප් එක පාවිච්චි කරන ආකාරය පියවරෙන් පියවර

### ⚙️ පියවර 1: Sidebar එකෙහි API සැකසුම් සකස් කිරීම

ඇප් එක විවෘත වූ පසු, එහි වම්පස ඇති Sidebar panel එක මඟින් ඔයාගේ AI සැකසුම් සකස් කරගන්න:

* **AI Provider:** ඔයා භාවිතා කිරීමට බලාපොරොත්තු වන AI සේවාව තෝරන්න (**OpenAI** හෝ **Google Gemini**).


* **API Key:** ඔයා සතු පෞද්ගලික API Key එක (`sk-...` හෝ `AIza...`) මෙහි ඇති text box එකට ආරක්ෂිතව ඇතුළත් කරන්න. ඔයාගේ key එක කිසිම විටක වෙනත් තැනක සුරැකීමක් හෝ සටහන් කරගැනීමක් සිදු නොවේ.


* **Model Selection:** Dropdown මෙනුව භාවිතා කර ඔයා කැමති Model සංස්කරණයක් (උදා: `gpt-4o-mini`, `gemini-2.0-flash`, හෝ `gemini-2.5-pro`) තෝරාගන්න.



### 📋 පියවර 2: Output Preferences සකස් කරගැනීම

ඔයාට අවශ්‍ය අධ්‍යයන ද්‍රව්‍ය සකස් විය යුතු ආකාරය Sidebar එකෙහි ඇති මෙවලම් මඟින් පාලනය කරන්න:

* **What do you want to generate?:** පද්ධතිය තුළ ඇති ප්‍රධාන මෙවලම් 4න් ඔයාට අවශ්‍ය එකක් තෝරන්න:


* *📝 Short Notes:* PDF එකෙහි අඩංගු කරුණු පැහැදිලි කෙටි සටහන් බවට පත් කිරීමට.


* *🧠 Quiz:* ස්වයංක්‍රීයව MCQ ප්‍රශ්නාවලියක් සකස් කර ගැනීමට.


* *💬 Q&A Pairs:* කෙලින්ම ප්‍රශ්න සහ පිළිතුරු මාලාවක් සකසා ගැනීමට.


* *🗺️ Mind Map:* පාඩමේ ව්‍යුහය දෘශ්‍ය රූප සිතියමක් ලෙස වෙන් කර ගැනීමට.




* **Max Pages Slider:** ඇප් එක මඟින් කියවිය යුතු උපරිම පිටු ගණන Slider එක මඟින් සකසන්න (පිටු 1 සිට 100 දක්වා සැකසිය හැක, සාමාන්‍යයෙන් පිටු 15 කි).


* **Number of Items Slider:** ප්‍රශ්න කීයක් හෝ කරුණු කීයක් අවශ්‍යද යන්න Slider එකෙන් තෝරන්න (ප්‍රශ්න/කරුණු 3 සිට 20 දක්වා සැකසිය හැක, සාමාන්‍යයෙන් 10 කි).


* **Quiz Settings:** ඔයා "Quiz" එකක් තේරුවේ නම්, එක් ප්‍රශ්නයකට පිළිතුරු දීමට ලැබෙන කාලය **Seconds per question** slider එකෙන් (තත්පර 10 සිට 60 දක්වා) තෝරන්න.


* **Sinhala Mode Checkbox:** වැදගත් ඉංග්‍රීසි තාක්ෂණික වචන අසලින්ම ඒවායේ සිංහල තේරුම වරහන් ඇතුළත දැක්වීමට අවශ්‍ය නම් **Show Sinhala meanings** යන්න සක්‍රීය (Check) කරන්න.



### 📄 පියවර 3: PDF ලේඛනය ඇතුළත් කිරීම

* ඔයාට සාරාංශ කරගත යුතු පාඩම් පොත හෝ Lecture සටහන අඩංගු **PDF file** එක මැද ඇති කොටස වෙත ඇද දමන්න (Drag & Drop), නැතහොත් ක්ලික් කර පරිගණකයෙන් තෝරන්න.


* Upload වූ සැණින් එහි පිටු ගණන (**Total pages**), කියවන පිටු ගණන (**Pages processed**) සහ හඳුනාගත් අකුරු ප්‍රමාණය (**Characters extracted**) Metrics මඟින් තිරය මත පෙන්වනු ඇත.


* අවශ්‍ය නම් **Preview extracted text** expander එක ක්ලික් කර PDF එකෙන් කියවාගත් දත්තවල පෙරදසුනක් පරීක්ෂා කළ හැක.



### 🚀 පියවර 4: ප්‍රතිඵල ලබාගැනීම සහ භාවිතය

සියල්ල නිවැරදිව සැකසූ පසු, මැද ඇති විශාල **🚀 Generate** බොත්තම ක්ලික් කර AI ක්‍රියාවලිය ආරම්භ කරන්න.

* **Short Notes තේරුවේ නම්:** තිරය මත දිස්වන සටහන් කියවා බලා, ඒවා පරිගණකයට සුරැකීමට පහළ ඇති බොත්තම් මඟින් **.txt**, **PDF** ලේඛනයක් ලෙස හෝ ජංගම දුරකථනයට පහසු **PNG Image** එකක් ලෙස භාගත (Download) කරගත හැක.


* **Quiz තේරුවේ නම්:** රතු පැහැයෙන් දිවෙන **⏱ Countdown Timer** එක අවසන් වීමට පෙර ප්‍රශ්න වලට පිළිතුරු සපයා **📊 Submit Quiz** බොත්තම ඔබන්න. එවිට ඔයාගේ ලකුණු මට්ටම (Score Box) සමඟ නිවැරදි (✅) සහ වැරදි (❌) පිළිතුරු මෙන්ම ඒ සඳහා වන AI පැහැදිලි කිරීම් (`💡`) සහ ලබාගත් කාලය ද බලාගත හැක.


* **Mind Map තේරුවේ නම්:** පාඩමේ ව්‍යුහය දෘශ්‍යමය වශයෙන් පෙන්වන අලංකාර වීදුරු මෝස්තරයේ (Glassmorphic) සිතියමක් දිස්වන අතර, එය **Download SVG** හෝ **Download PNG** බොත්තම් මඟින් පරිගණකයට සුරැකිය හැක.


* **Q&A Pairs තේරුවේ නම්:** සකස් වූ ප්‍රශ්න සහ පිළිතුරු මාලාව කියවා බලා **Download as .txt** බොත්තමෙන් text file එකක් ලෙස සුරැකිය හැක.




# 🚀 CHAKRA - Feedback, Bug Reporting & File Structure

[English Description]
Since **CHAKRA** is currently in its **Beta Version**, community feedback and bug reporting are essential for its development. Below is the guide for users to contribute or report issues, followed by the repository's file structure.

[සිංහල විස්තරය]
**CHAKRA** ඇප් එක දැනට පවතින්නේ **Beta Version** එකක බැවින්, එහි අඩුපාඩු සකසා ගැනීමට පරිශීලකයන්ගේ අදහස් සහ Bugs වාර්තා කිරීම ඉතා වැදගත් වේ. ඒ සඳහා වන මාර්ගෝපදේශය සහ ප්‍රොජෙක්ට් එකෙහි ඇති ගොනු ව්‍යුහය (File Structure) පහතින් දක්වා ඇත.

---

## 🐛 Part 1: Feedback & Bug Reporting (අදහස් සහ දෝෂ වාර්තා කිරීම)

### 🇬🇧 English Guide

If you encounter any bugs, glitches, or have feature suggestions during the Beta phase, please let us know:

1. **GitHub Issues:** Navigate to the **Issues** tab in this repository, click **New Issue**, and describe the bug along with screenshots if possible.
2. **Feature Requests:** If you want to see a specific feature added (e.g., more AI models or export formats), open a feature request in the Issues section.
3. **Contact:** You can reach out directly via LinkedIn or email for collaboration queries under **GIMA VERSE** branding.



### 🇱🇰 සිංහල මාර්ගෝපදේශය

මෙම Beta කාලසීමාව තුළදී ඇප් එකෙහි කිසියම් දෝෂයක් (Bug/Glitch) වුවහොත් හෝ අලුත් අදහස් අප වෙත දැනුම් දීමට කැමති නම්:

1. **GitHub Issues:** මෙම repository එකෙහි ඇති **Issues** tab එක වෙත ගොස්, **New Issue** ක්ලික් කර ඔයාට මුහුණ දීමට සිදු වූ දෝෂය පැහැදිලි කරන්න (හැකි නම් Screenshot එකක් ද ඇතුළත් කරන්න).
2. **Feature Requests:** ඇප් එකට අලුතින් එකතු විය යුතු මෙවලම් (උදා: තවත් AI Models) පිළිබඳ යෝජනා Issues section එකෙහි සටහන් කරන්න.
3. **සංවර්ධකයා සම්බන්ධ කරගැනීම:** වැඩිදුර සහයෝගීතාවයන් සඳහා **GIMA VERSE** නාමය යටතේ LinkedIn හෝ විද්‍යුත් තැපෑල (Email) හරහා කෙලින්ම සම්බන්ධ විය හැක.



---

## 📁 Part 2: Project File Structure (ප්‍රොජෙක්ට් ගොනු ව්‍යුහය)

### 🇬🇧 English Layout

To help developers navigate the codebase, here is the official directory mapping for CHAKRA:

```text
CHAKRA/
│
├── app.py                 # The main application script containing UI layout & AI logic
├── requirements.txt       # List of dependency libraries required to run the tool
├── README.md              # Complete documentation and user manuals
└── Assets/                # Repository graphics, icons, and screenshots

```

* **`app.py`:** This is the core Python script powered by Streamlit that manages page configurations, applies glassmorphic CSS animations, handles PDF text extractions, and interfaces with OpenAI or Google Gemini APIs.



### 🇱🇰 සිංහල සැකැස්ම

වෙනත් සංවර්ධකයන්ට (Developers) කේතය (Code) තේරුම් ගැනීමට පහසු වීම සඳහා CHAKRA හි ගොනු පෙළගැස්ම මෙසේය:

```text
CHAKRA/
│
├── app.py                 # UI සැලසුම සහ AI තර්කනය අඩංගු ප්‍රධාන Python ගොනුව
├── requirements.txt       # ඇප් එක ක්‍රියාත්මක වීමට අවශ්‍ය වන පරිබාහිර පුස්තකාල ලැයිස්තුව
├── README.md              # සම්පූර්ණ පරිශීලක මාර්ගෝපදේශය සහ ලේඛනගත කිරීම්
└── Assets/                # ඇප් එකට අදාළ පින්තූර, අයිකන සහ Screenshots

```

* **`app.py`:** මෙය Streamlit තාක්ෂණයෙන් ක්‍රියාත්මක වන ප්‍රධාන Python ගොනුව වන අතර, මෙයට පිටුවේ සැකසුම්, Glassmorphism CSS මෝස්තර, PDF කියවීමේ මෙවලම් සහ OpenAI / Google Gemini API සම්බන්ධතා සියල්ල ඇතුළත් වේ.



---

## 📜 Part 3: Disclaimer & License (වගකීම් ප්‍රකාශය සහ බලපත්‍රය)

### 🇬🇧 English

* **Disclaimer:** This software is provided "as-is" during its Beta release cycle. Users are responsible for managing their personal API keys; CHAKRA does not store, share, or log any user keys or private operational metadata.


* **License:** MIT License. Feel free to fork, modify, and utilize this tool for personal or educational upgrades.

### 🇱🇰 සිංහල

* **වගකීම් ප්‍රකාශය:** මෙම මෘදුකාංගය Beta අදියරේ පවතින බැවින් පවතින තත්වයෙන්ම ("as-is") භාවිතයට ලබා දී ඇත. පරිශීලකයන් තමන්ගේ පෞද්ගලික API Keys කළමනාකරණය කරගත යුතු අතර, CHAKRA ඇප් එක මඟින් කිසිදු අයුරකින් Keys සුරැකීමක් හෝ සටහන් කරගැනීමක් සිදු නොකරයි.


* **බලපත්‍රය:** MIT License. මෙම කේතය පුද්ගලික හෝ අධ්‍යාපනික කටයුතු සඳහා වෙනස් කර භාවිත කිරීමට සම්පූර්ණ නිදහස ඇත.

*Developed under the branding of **GIMA VERSE** (Premium Beta Build)*