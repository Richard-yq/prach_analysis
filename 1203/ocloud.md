# OAI gNB FHI72 容器映像檔建置與部署指南

本文件說明如何建置 OpenAirInterface (OAI) gNB 容器映像檔，並推送至私有映像倉庫以供 O-Cloud 部署使用。

---

## 1. Building the shared images

建置共用映像檔，包含：
- **ran-base**: 包含所有相依套件的基礎映像
- **ran-build-fhi72**: 編譯所有目標元件 (eNB, gNB, [nr]UE) 並支援 Fronthaul 7.2

### 1.1 Clone 原始碼並建置基礎映像

```bash
git clone <repo>
cd openairinterface5g
# default branch is develop, to change use git checkout <BRANCH>
podman build --target ran-base --tag ran-base:latest --file docker/Dockerfile.base.ubuntu22 .
# if you want to use front-haul 7.2 and RFSimulator radios
podman build --tag ran-build-fhi72:latest --file docker/Dockerfile.build.fhi72.ubuntu22 .
```

### 1.2 檢視已建置的映像檔

```bash
docker image ls
```

---

## 2. 建置 gNB FHI72 映像檔

使用 Dockerfile 建置支援 Fronthaul 7.2 的 gNB 映像：

```bash
podman build --tag oai-gnb-fhi72:latest --file docker/Dockerfile.gNB.fhi72.ubuntu22 .
```

---

## 3. 登入私有映像倉庫

登入 Harbor 映像倉庫以便後續推送映像：

```bash
podman login bmw.ece.ntust.edu.tw
```

**登入資訊：**
```
username: richardyq
```

---

## 4. 標記並推送映像至倉庫

### 4.1 建置成功訊息

```
--> 8030d031b65d
Successfully tagged localhost/oai-gnb-fhi72:latest
![alt text](image-1.png)


### 4.2 為映像加上遠端倉庫標籤

將本地映像標記為遠端倉庫路徑：

```bash
podman tag localhost/oai-gnb-fhi72:latest bmw.ece.ntust.edu.tw/richardyq/oai-gnb-fhi72-fdm-enable:latest
```

### 4.3 推送映像至遠端倉庫

```bash
podman push bmw.ece.ntust.edu.tw/richardyq/oai-gnb-fhi72-fdm-enable:latest
```



![alt text](image-2.png)

```
Getting image source signatures
Copying blob 17a70da5b0ed done   | 
Copying blob f27f344c63cf done   | 
Copying blob 525fd574c68f done   | 
Copying blob 404a524ec633 done   | 
Copying blob fd849d716c9f done   | 
Copying blob 73974f74b436 done   | 
Copying blob e43c0f7b5377 done   | 
Copying blob a9cf99ffb57c done   | 
Copying blob 71fe427cfd95 done   | 
Copying blob 969568a5a38f done   | 
Copying config 8030d031b6 done   | 
Writing manifest to image destination
```

## 5. 部署至 O-Cloud (使用 Helm)

### 5.1 Clone Helm 模板
git switch starlingx/pegatron
Values.yaml -> repo & tag
```
<!-- git clone https://github.com/motangpuar/ocloud-helm-templates.git -->
git clone https://github.com/Richard-yq/ocloud-helm-templates.git

revise config
/home/richard/ocloud-helm-templates/oai-gnb-fhi-72/templates/configmap.yaml


```



```
helm install oai-richard -n richard --create-namespace  .
```

```
helm uninstall oai-richard -n richard
```


```
```


### Access liteon
```
ssh user@192.168.8.77
user
enable
liteon168
```

### access k9s
```
ssh richard@192.168.8.53
k9s

<!-- 
dog:command
0: all pod

/oai pods -->
```





