# URL image scraper

Testing github co-pilot.

Local I was using python with anaconda (python version: Python 3.8.8)

    env vars in Path:

    ```
        C:\ProgramData\Anaconda3
        C:\ProgramData\Anaconda3\Scripts
        C:\ProgramData\Anaconda3\Library\bin
    ```

## inspired by

https://www.youtube.com/watch?v=s0664d-ko3w&ab_channel=TristanBehrens

# Problems 

## file name problem

```
    Error: [Errno 22] Invalid argument:
```

I had to change the filename to something like this:

```
    filename = image_url.split("?")[0].split("/")[-1]
```

before I was only calling open like this:

```
    open(image_url.split("/")[-1], "wb")
```

Found the solution here: https://stackoverflow.com/questions/63159112/download-image-using-requests-that-contains-a-query-string

## SSL problem    

```
    requests.get urllib3.exceptions.SSLError: Can't connect to HTTPS URL because the SSL module is not available
```

### Solution

Copy this files:

libcrypto-1_1-x64.dll
libssl-1_1-x64.dll

from C:\ProgramData\Anaconda3\Library\bin to C:\ProgramData\Anaconda3\DLLs.

Found the solution here: https://exerror.com/caused-by-sslerrorcant-connect-to-https-url-because-the-ssl-module-is-not-available/