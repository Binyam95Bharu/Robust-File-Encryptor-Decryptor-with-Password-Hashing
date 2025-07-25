# Robust-File-Encryptor-Decryptor-with-Password-Hashing
ይህ ፕሮጀክት ፋይሎችን በይለፍ ቃል Encryptor/Decryptor ያደርጋል። ደህንነቱን ለማሻሻል የcryptography ላይብረሪን ለኢንክሪፕሽን እና bcrypt ላይብረሪን ለይለፍ ቃል ሃሺንግ ይጠቀማል።
 Robust File Encryptor/Decryptor with Password Hashing

ይህ የፓይዘን ፕሮጀክት ፋይሎችን በከፍተኛ ደህንነት ኢንክሪፕት እና ዲክሪፕት ለማድረግ የተሰራ ነው። የ`cryptography.fernet` ላይብረሪን ለኢንክሪፕሽን እና `bcrypt` ላይብረሪን ለይለፍ ቃል ሃሺንግ ይጠቀማል፣ ይህም የይለፍ ቃል ደህንነትን ያጠናክራል።

# ባህሪያት

ጠንካራ ኢንክሪፕሽን: ፋይሎችን በFerNet (AES-128 CBC + HMAC-SHA256) በመጠቀም ኢንክሪፕት ያደርጋል።
 የይለፍ ቃል ሃሺንግ: የይለፍ ቃሎች በቀጥታ እንደ ቁልፍ ከመጠቀም ይልቅ በ`bcrypt` Hash ይደረጋሉ፣ ይህም Rainbow Table ጥቃቶችን ለመከላከል እና የይለፍ ቃሉ ቢጋለጥም የኢንክሪፕሽን ቁልፉን እንዳይገኝ ይከላከላል።
 Salt አጠቃቀም: ለእያንዳንዱ ኢንክሪፕሽን አዲስ Salt ይፈጠራል፣ ይህም የይለፍ ቃል ሃሺንግን የበለጠ ደህንነቱ የተጠበቀ ያደርገዋል።
 ቀላል CLI: ፋይሎችን ለማስገባት እና የይለፍ ቃሎችን ለማስገባት የሚያስችል ቀላል የትዕዛዝ መስመር በይነገጽ (Command Line Interface)።

# የደህንነት ማብራሪያ

`cryptography.fernet`: FerNet በCryptography ላይብረሪ የሚቀርብ የSymmetric encryption ስታንዳርድ ነው። AES-128 CBC Modeን ለኢንክሪፕሽን እና HMAC-SHA256ን ለአድማጭነት (authentication) ይጠቀማል፣ ይህም ለ Confidentiality እና Integrity ያረጋግጣል።
 `bcrypt` ለይለፍ ቃል ሃሺንግ: bcrypt ቀርፋፋ እና ለ brute-force ጥቃቶች አስቸጋሪ እንዲሆን የተነደፈ የሃሺንግ አልጎሪዝም። በቀጥታ የይለፍ ቃልን እንደ ኢንክሪፕሽን ቁልፍ ከመጠቀም ይልቅ፣ የይለፍ ቃሉን Hash አድርጎ ከዚያ ቁልፍ ማመንጨት (Key Derivation) የበለጠ ደህንነቱ የተጠበቀ ነው።
 Salt: ለእያንዳንዱ የይለፍ ቃል Hash ልዩ የሆነ Salt በመጨመር፣ ተመሳሳይ የይለፍ ቃል ያላቸው ሰዎች እንኳን የተለያየ Hash እንዲኖራቸው ይደረጋል፣ ይህም Rainbow Table Attackን ይከላከላል። Saltው ከ encrypted data ጋር አብሮ ይከማቻል።

# እንዴት መጠቀም ይቻላል

1.  የሚያስፈልጉ ላይብረሪዎችን ጫን:
    ```bash
    pip install cryptography bcrypt
    ```
2.  ስክሪፕቱን procces:
    ```bash
    python encryptor.py
    ```
3.  የሚፈልጉትን ተግባር ምረጥ:
    * `e` ለኢንክሪፕት
    * `d` ለዲክሪፕት
    * `q` ለመውጣት
4.  ስክሪፕቱ ሲጠይቅ የፋይሉን መንገድ እና የይለፍ ቃል አስገባ። ኢንክሪፕት የተደረገው ፋይል በ`.encrypted` ቅጥያ ይቀመጣል (ለምሳሌ `my_file.txt.encrypted`)።

# የደህንነት ማስጠንቀቂያ

ይህ ፕሮጀክት ለትምህርታዊ ዓላማ የተዘጋጀ ነው። ምንም እንኳን ደህንነታቸው የተጠበቁ ላይብረሪዎችን ቢጠቀምም፣ ውስብስብ ለሆኑ የንግድ አፕሊኬሽኖች ተጨማሪ የደህንነት ምርመራዎች እና ምርጥ ልምዶች (best practices) መከተል አለባቸው። የኢንክሪፕሽን ቁልፍ የይለፍ ቃልህን በመጠቀም ስለሚመነጭ የይለፍ ቃልህን መርሳት ማለት ፋይሎችህን ማግኘት አለመቻል ማለት ነው።
