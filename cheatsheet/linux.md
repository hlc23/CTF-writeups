# linux

## find
```bash
find [path] -name [name]
```

## ps
列出系統上的所有進程，包括用戶進程和系統進程，以及與它們相關的詳細信息。
```bash
ps aux
```

## netstat
列出系統上所有的網路連接，包括 TCP 和 UDP 連接。
```bash
netstat [OPTIONS]
```
```bash
-a # 列出所有連接
-n # 以數字形式顯示地址和端口
```

## curl
```bash
curl [OPTIONS] [URL]
```
```bash
-o # 將輸出保存到文件
-v # 詳細模式
-X # 指定請求方法
    [OPTIONS]
    GET
    HEAD
    POST
    PUT
    DELETE
-H # 指定請求頭

```
request method
```bash
-X GET
-X POST
-X PUT
-X DELETE
```


## tar
```bash
tar [OPTIONS] [FILE]
```
```bash
-c # 建立壓縮檔案
-x # 解壓縮檔案
-z # 透過 gzip 壓縮/解壓縮檔案
-j # 透過 bzip2 壓縮/解壓縮檔案
-v # 詳細模式
-f # 指定壓縮檔案名稱
```

## dd
```bash
dd if=[INPUT] of=[OUTPUT] [OPTIONS]
```
```bash
dd if=image.png of=flag skip=100 bs=1
```
