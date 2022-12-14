# Projek NDT SBD

Projek ini dibuat menggunakan Vite Package Manager.
[Kalau mau liat web kaya gimana](https://izaz4141.github.io/NDT_SBD/)

## Setup

Pada Front End install dependency dengan

```
npm install --legacy-peer-deps
```

Pada folder server buat file `.env` lalu isi dengan

```
USER_NAME= user name mysql
USER_PASSWORD= password user mysql
FLASK_SECRET= random secret
```

Kemudian install Redis, dan package python di folder server dengan,

```
pip install -r requirements.txt
```

Jangan lupa buat database mysql bernama `ndt_sbd`

## Run Web Page

```
npm run dev
```

## Run Backend

Pada folder server jalankan

```
py launcher.py
```

## Push

Sebelum commit atau push project tolong jalankan command ini terlebih dahulu

```
npm run format
```

Ini berfungsi untuk memformat kode menggunakan Prettier sehingga kode menjadi rapi

## Lint

```
npm run lint
```

## Preview

```
npm run preview
```

## Production

```
npm run build
```

## Dokumentasi

The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

## Recommended IDE Setup

-   [VS Code](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) + [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
