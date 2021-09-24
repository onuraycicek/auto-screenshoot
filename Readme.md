
# Auto Screenshoot

Auto screenshoot with Python.

## Installation


```bash
  git clone https://github.com/onuraycicek/auto-screenshoot.git
```
```bash
  pip3 install requirements.txt
```
```bash
  python3 index.py
```
    
## Parameters

#### Set folder structure

```bash
  python3 index.py --day=%Y/%m/%d
```

| Parameter |  Default |
| :-------- |  :------------------------- |
| `day` | %Y/%m/%d |


  #### Set file name

```bash
  python3 index.py --filename=%H:%M:%S
```

| Parameter |  Default | 
| :-------- |  :------------------------- | 
| `filename` |%H:%M:%S |



  #### Set default path

```bash
  python3 index.py --defaultPath=/home/screensoot
```

| Parameter |  Default | 
| :-------- |  :------------------------- | 
| `defaultPath` | "./screenshoot/" |