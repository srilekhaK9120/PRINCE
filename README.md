## **Team ILLUMINATI**

![price cipher core](core.png)

### **SBox Analysis**

#### <code>sbox_analysis.ipynb</code> contains the code for prince cipher implementation.

- This file contains the code for sbox analysis both using inbuilt sage functions and in pure python.

### **Software Implementation**

#### <code>software_implementation.ipynb</code> contains the code for prince cipher implementation.

- This file contains the code for encryption and decription using prince cipher.
  -There are two main functions: <code>prince_encrypter</code> and <code>prince_decrypter</code>
- Both take an input of 64bit (16 hex) message string along with 128bit (32 hex) key string.
### **Cryptanalysis**
<code>integral_cryptanalysis.ipynb</code> file contains the code for integral attack cryptanalysis. 


### **Software Application**

> **FrontEnd :** NextJS (Javascript, React)

#### **How to run front-end:**

#### Go to <code>Software Application @ Crypto/frontend/crypto_cs553</code> folder and run <code>"npm run dev"</code> in the terminal, then go to <code>http://localhost:3000</code>.

> **Backend :** FastAPI (Python framework)

#### **How to run back-end:**

#### Go to <code>Software Application @ Crypto/backend/FastApi</code>" folder and run <code>"uvicorn main:app --reload"</code> in the terminal, then go to <code>http://localhost:3000</code>.

#### To access the visual interface of backend, go to <code>http://127.0.0.1:8000/docs</code>.

> **Requirements : (dependencies)**

python 3.x

- pip3 install fastapi uvicorn

node 16.x or greater

- run <code>npm init</code> in <code>Software Application @ Crypto/frontend/crypto_cs553</code>
