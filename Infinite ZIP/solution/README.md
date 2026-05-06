# Solution: Infinite ZIP

First, I unzipped the first couple of archives manually. I observed that the initial archive was named `Layer-master-v3204.zip` and it contained `layer_0002.zip`. I assumed the sequence would continue up to `layer_1000.zip`.

So, I wrote a Python script to automate the extraction process. My script first unzipped the master archive using a bash command via a subprocess. Then, using a `while` loop, it built each subsequent zip file name by adding zero-padding up to 4 digits (like `layer_0002.zip`) and unzipped them sequentially. 

After the loop finished extracting all the layers, my script opened the resulting `flag.txt` file, decoded the text from base64, and printed the final flag to the console.

**Base64:** `VVZUSUNTe0QzM3BfRDF2M180MjB9`  
**Flag:** `UVTICS{D33p_D1v3_420}` 